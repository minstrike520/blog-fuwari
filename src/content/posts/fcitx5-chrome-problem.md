---
title: fcitx5 與 Chrome 的相容性問題
published: 2026-01-12
tags:
  - Linux
  - 輸入法
category: IT 除錯紀錄
---
# Chrome, Obsidian

我剛開始嘗試 Linux 作為個人作業系統時大約是 2025 年暑假。那個時候，使用 Obsidian、Chrome 時都沒辦法直接使用 fcitx5，而要加上一串旗標才能動。直至今日 Chrome 不用加就可以用輸入法了，但 Obsidian 還是需要手動加上。

ref: [https://github.com/fcitx/fcitx5/issues/1067](https://github.com/fcitx/fcitx5/issues/1067)

```bash
--enable-features=UseOzonePlatform --ozone-platform=wayland --enable-wayland-ime
```

加上以上旗標即可運作。

# OnlyOffice

```bash
XMODIFIERS=@im=fcitx
```
