---
title: Git Basics
published: 2024-11-12
tags:
  - IT-Basics
  - Git
category: IT筆記
---
*遷移自 HackMD*

也請參考：[GitHub CLI](../github-cli/)

## 版本控管

### Undo Uncommitted Changes

[StackOverflow Discussion](https://stackoverflow.com/questions/14075581/git-undo-all-uncommitted-or-unsaved-changes)

This will unstage all files you might have staged with `git add`:

```bash
git reset
```
    
This will revert all local uncommitted changes (should be executed in repo root):

```bash
git checkout .
```
    
  You can also revert uncommitted changes only to particular file or directory:
  
```bash
git checkout [some_dir|file.txt]
```

### Ignoring Files

[reference](https://stackoverflow.com/questions/13541615/how-to-remove-files-that-are-listed-in-the-gitignore-but-still-on-the-repositor)

**REMOVE ALL SPECIFIED IN `.gitignore` FROM REPOSITORY**

```bash!
git rm --cached `git ls-files -i -c --exclude-from=.gitignore`
```

## 雜項

### \<ERROR\> RPC Failed

[Reference](https://stackoverflow.com/questions/77816301/git-error-rpc-failed-http-400-curl-22-the-requested-url-returned-error-400)

本解決方案的原理是將推送的大小限制調大，避免因為push/pull的流量太大而讓Git產生buffer塞爆的問題。

```bash
git config --global http.postBuffer 524288000
```

### Show Non-Alphabetic Characters

[Reference](https://blog.miniasp.com/post/2017/09/17/Git-for-Windows-Command-Prompt-Display-Chinese-Issues)

在Git剛設定完時，如果推送了非英文的內容，commit log或者status就可能會出現「亂碼」。不過別緊張，有可能是Git的設定預設值造成的。

``` bash
git config --global core.quotepath false
```

這個設定的意思是「要不要把非標準字元輸出為代碼」。設定為否的話，系統才會嘗試把原本的字元顯示出來。至於如果還是亂碼，那就要去研究locale是否設定妥當。

## 遠端控管

### Push Local Repo to GitHub

首先要先在GitHub開啟一個**空的**repo，名稱隨意，不過建議使用跟本地repo差不多的名字。

接著要[使用GitHub CLI來做授權登入](../github-cli)。

然後，在本地的commit：

```bash!
cd LOCAL_REPO_DIR/
git init .
git config --global --add safe.directory $(pwd -P)
git add .
git commit -m "init"
```

設定＆推送：

```bash!
git remote add origin <ORIGIN_URL>
git push --set-upstream origin master
```

