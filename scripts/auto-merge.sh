#!/bin/bash

# MADE BY GEMINI 3.1 PRO
# auto-merge.sh
# 此腳本會自動合併指定的分支。
# 若在 package.json 發生衝突，會透過 Python 自動選擇版本較高的套件，
# 並藉由 `pnpm install` 重新產生 pnpm-lock.yaml 來解決鎖定檔衝突，最後完成合併。

if [ "$#" -eq 0 ]; then
    echo "用法: $0 <branch1> [branch2 ...]"
    echo "範例: $0 origin/dependabot-npm_and_yarn-*"
    exit 1
fi

for branch in "$@"; do
  echo "正在合併 $branch..."
  git merge "$branch" --no-edit || {
    echo "偵測到衝突，嘗試自動解決 package.json 中的套件版本衝突..."
    
    python3 -c '
import re
import sys

try:
    with open("package.json", "r") as f:
        content = f.read()
except FileNotFoundError:
    sys.exit(0)

def replacer(match):
    block = match.group(0)
    lines = block.split("\n")
    head_lines = []
    other_lines = []
    mode = None
    
    for line in lines:
        if line.startswith("<<<<<<<"): 
            mode = "HEAD"
        elif line.startswith("======="): 
            mode = "OTHER"
        elif line.startswith(">>>>>>>"): 
            break
        else:
            if mode == "HEAD": head_lines.append(line)
            elif mode == "OTHER": other_lines.append(line)

    def parse(lines_arr):
        d = {}
        for l in lines_arr:
            l_str = l.strip()
            if l_str: d[l_str.split(":")[0]] = l
        return d
        
    hd = parse(head_lines)
    od = parse(other_lines)
    
    for k in od:
        if k not in hd: 
            hd[k] = od[k]
        else:
            v1 = re.search(r"[\d\.]+", hd[k])
            v2 = re.search(r"[\d\.]+", od[k])
            if v1 and v2:
                try:
                    vf1 = [int(x) for x in v1.group(0).split(".")]
                    vf2 = [int(x) for x in v2.group(0).split(".")]
                    if vf2 > vf1: hd[k] = od[k]
                except Exception:
                    pass
                    
    res = [hd[k] for k in sorted(hd.keys())]
    return "\n".join(res)

new_content = re.sub(r"<<<<<<< HEAD.*?>>>>>>> [^\n]+", replacer, content, flags=re.DOTALL)
with open("package.json", "w") as f:
    f.write(new_content)
'
    
    echo "執行 pnpm install 來修正 pnpm-lock.yaml..."
    pnpm install --no-frozen-lockfile
    
    echo "將修正的檔案加入暫存區並提交..."
    git add package.json pnpm-lock.yaml
    
    # 檢查是否還有未解決的衝突檔案 (如合併到其他的檔案時)
    if git ls-files -u | grep -q .; then
        echo "錯誤: 仍然有未解決的衝突。請手動解決！"
        git status
        exit 1
    fi
    
    git commit --no-edit
  }
done

echo "🎉 所選分支已全數合併完畢！"
