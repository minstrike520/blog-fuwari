---
title: GitHub CLI
published: 2026-01-28
tags:
  - IT-Basics
  - Git
  - GitHub
category: IT筆記
---
## GitHub Authentication

這個方法是運用GitHub的CLI來通過驗證，以將本地的Repo推送至GitHub，package名叫`gh`。

指令會發起一連串互動式的提示問答，所以只要依照自己的需求選幾個選擇題就能完成驗證。

```bash
gh auth login
```