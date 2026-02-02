---
title: Python
published: 2026-02-02
tags:
  - Scripts
category: Python
---
## Hexo-Astro Transformation

> 撰寫一個python腳本，讀取一個檔案，並按照以下規則修改這個檔案：
> 按此規則取代： `/category:\n  - (.*)/category: $1`
> 按此規則取代： `/date: /published: ` 

> 請用argparse加入指定資料夾的功能，然後讀取該資料夾下的所有md檔進行處理

```python
import os
import re
import argparse

def process_file(file_path):
    """處理單一檔案的取代邏輯"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 規則 1: 將 category 換行清單轉為單行
        p1 = r"category:\n\s*-\s*(.*)"
        r1 = r"category: \1"
        new_content = re.sub(p1, r1, content)

        # 規則 2: date -> published
        new_content = new_content.replace("date: ", "published: ")

        # 只有在內容有變動時才寫入，減少硬碟 I/O
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False

    except Exception as e:
        print(f"處理 {file_path} 時發生錯誤: {e}")
        return False

def main():
    # 設定 argparse
    parser = argparse.ArgumentParser(description="批次修改 Markdown 檔案的 Front Matter 格式")
    parser.add_argument("dir", help="指定要處理的資料夾路徑")
    
    args = parser.parse_args()
    target_dir = args.dir

    if not os.path.isdir(target_dir):
        print(f"錯誤：'{target_dir}' 不是一個有效的資料夾。")
        return

    # 執行批次處理
    count = 0
    files = [f for f in os.listdir(target_dir) if f.endswith('.md')]
    
    print(f"開始處理資料夾：{target_dir}，共找到 {len(files)} 個 .md 檔...")

    for filename in files:
        file_path = os.path.join(target_dir, filename)
        if process_file(file_path):
            print(f" [已修改] {filename}")
            count += 1
        else:
            print(f" [無變動] {filename}")

    print(f"\n處理完成！總計修改了 {count} 個檔案。")

if __name__ == "__main__":
    main()
```

---

## Image Supply Dash

> 撰寫一個python腳本，指定一個D資料夾，指定一個markdown。從markdown裡面尋找pattern `![](.*)`，當這個pattern取得的 `$1` 在D資料夾存在一個同名檔案、且檔案名含有空格時，修改檔名將空格替換為dash，並且同步修改markdown裡面的對應引用。 

```python
import os
import re
from pathlib import Path

def fix_markdown_image_spaces(target_dir, md_file_path):
    # 檢查路徑是否存在
    if not os.path.exists(target_dir):
        print(f"錯誤: 找不到目錄 {target_dir}")
        return
    if not os.path.exists(md_file_path):
        print(f"錯誤: 找不到 Markdown 檔案 {md_file_path}")
        return

    # 讀取 Markdown 內容
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 正則表達式解釋:
    # !\[(.*?)\] : 匹配圖片的 alt text (如 ![Description])
    # \((.*?)\)   : 匹配括號內的內容 (即檔案路徑)
    pattern = r'!\[(.*?)\]\((.*?)\)'

    count = 0

    def rename_callback(match):
        nonlocal count
        alt_text = match.group(1)
        original_link = match.group(2)
        
        # 取得純檔名 (避免路徑中包含子目錄的干擾)
        filename = os.path.basename(original_link)
        
        # 檢查檔名中是否有空格
        if ' ' in filename:
            old_file_path = os.path.join(target_dir, filename)
            
            # 如果在指定資料夾內確實存在這個含空格的檔案
            if os.path.isfile(old_file_path):
                new_filename = filename.replace(' ', '-')
                new_file_path = os.path.join(target_dir, new_filename)
                
                try:
                    # 執行實際的檔案更名
                    os.rename(old_file_path, new_file_path)
                    print(f"成功更名: '{filename}' -> '{new_filename}'")
                    
                    # 更新 Markdown 中的引用路徑 (保持原本的目錄結構，只改檔名)
                    new_link = original_link.replace(filename, new_filename)
                    count += 1
                    return f'![{alt_text}]({new_link})'
                except Exception as e:
                    print(f"更名失敗 {filename}: {e}")
        
        # 如果沒條件不符合，回傳原始字串
        return match.group(0)

    # 執行替換
    new_content = re.sub(pattern, rename_callback, content)

    # 寫回 Markdown 檔案
    if count > 0:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"\n處理完成！共修改了 {count} 處引用並更換了對應檔案。")
    else:
        print("\n未發現需要更換的檔案或引用。")

# --- 設定區域 ---
if __name__ == "__main__":
    # 請在此指定你的 D 資料夾路徑
    D_FOLDER = r'C:/path/to/your/folder' 
    
    # 請在此指定你的 Markdown 檔案路徑
    MD_FILE = r'C:/path/to/your/note.md'

    fix_markdown_image_spaces(D_FOLDER, MD_FILE)
```

## Collect Image by Markdown

> 撰寫一個python腳本，指定一個S資料夾、D資料夾，指定一個markdown。從markdown裡面尋找pattern `![](.*)`，當這個pattern取得的 `$1` 在S資料夾存在一個同名檔案時，將其移到D資料夾。

```python
import os
import re
import shutil
from pathlib import Path

def move_markdown_images(source_dir, dest_dir, md_path):
    # 確保路徑物件化
    source_folder = Path(source_dir)
    dest_folder = Path(dest_dir)
    markdown_file = Path(md_path)

    # 檢查目的地資料夾是否存在，不存在則建立
    if not dest_folder.exists():
        dest_folder.mkdir(parents=True)
        print(f"已建立目的地資料夾: {dest_folder}")

    # 正則表達式：尋找 ![](path/to/image.png)
    # 這個 Pattern 會捕捉 () 裡面的內容
    pattern = r'!\[.*?\]\((.*?)\)'

    if not markdown_file.exists():
        print(f"錯誤：找不到 Markdown 檔案 {md_path}")
        return

    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 尋找所有匹配項
        matches = re.findall(pattern, content)
        
        # 移除重複的檔案名稱
        unique_matches = set(matches)
        
        moved_count = 0
        for img_path_str in unique_matches:
            # 取得檔名（排除路徑部分，例如 images/pic.jpg 只取 pic.jpg）
            filename = os.path.basename(img_path_str)
            
            # 定義在 S 資料夾中的完整路徑
            src_file_path = source_folder / filename
            dest_file_path = dest_folder / filename

            # 檢查檔案是否存在於來源資料夾
            if src_file_path.exists():
                print(f"正在移動: {filename}")
                shutil.move(str(src_file_path), str(dest_file_path))
                moved_count += 1
            else:
                print(f"略過：{filename} 不在來源資料夾中")

        print("-" * 30)
        print(f"處理完成！共移動了 {moved_count} 個檔案。")

    except Exception as e:
        print(f"執行時發生錯誤: {e}")

# --- 設定區域 ---
if __name__ == "__main__":
    S_FOLDER = "./source_images"  # 來源資料夾路徑
    D_FOLDER = "./used_images"    # 目的地資料夾路徑
    MD_FILE = "notes.md"         # Markdown 檔案路徑

    move_markdown_images(S_FOLDER, D_FOLDER, MD_FILE)
```