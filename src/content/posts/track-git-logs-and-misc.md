---
title: Git Logs
published: 2024-11-12
tags:
  - Git
category: IT筆記
---
*遷移自 HackMD*

因為我個人的筆記定期就會進行commit(至少在2024 7月之前每天commit兩次以上)，所以以前的筆記怎麼安放都可以用git來追蹤，那麼在此就記錄一下怎麼做：

- 把筆記空間的repo clone到一個新資料夾
- 用 `git log` 或者 GitHub 頁面來查找想要backtrace到的commit節點的SHA碼
- 在新clone下來的repo中 `git checkout <COMMIT_SHA>` 

這樣就可以得到特定時間的筆記空間狀態囉！

另外，如果想要找出某篇**特定文字**的歷史，這些文字卻又沒辦法透過log單個檔案的歷史來追蹤(比如，可能該段落經過複製貼上)，則可以在回復到舊版本時，使用如下模式的指令：

`grep <PATTERN> <VAULT_DIR> -r`

就可以找到該文字的來源(if any)啦！