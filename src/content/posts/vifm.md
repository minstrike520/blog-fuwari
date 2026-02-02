---
title: Vifm
published: 2026-01-27
tags:
  - TUI-apps
  - Vim
category: IT筆記
---
[Archlinux Wiki - Vifm](https://wiki.archlinuxcn.org/zh-tw/Vifm)

今天在用 [Paru](https://github.com/Morganamilo/paru) 安裝應用程式的時候，覺得 pager 用預設的 less 太單調了想換成 [bat](https://github.com/sharkdp/bat)。調了一下他的設定檔（`$HOME/.config/paru/paru.conf` or `/etc/paru.conf`）意外發現它預設的檔案管理員是「`vifm`」。好奇查了查，發現竟然還是 TUI 應用。這便引起了我研究的興致。

## 概述

Vifm 是個為 vim 使用者而生的檔案管理器。不僅是視窗導引與 vim 相同，連設定檔（`vifmrc`）、指令稿（如自訂按鍵）等等的設定方式都與 vim 十分相似。

更方便的是，vifm 與 GUI 的檔案管理員不同，開啟檔案時的「體驗」不會中斷：編輯器不用開啟新視窗，手也不用離開鍵盤——應該說，是連操作模式都不用改。

在需要頻繁切換資料夾時，使用起來會比用 [NvimTree](https://github.com/nvim-tree/nvim-tree.lua) 更順暢。

## 檔案管理操作

Vifm 既然是個檔案管理器，那就少不了移動、複製貼上、刪除等等的功能。這些功能都有直觀的指令可以達成。

有趣的是，和 NvimTree 不同，在 Vifm 中並不會有「檔案暫存區」這種東西。

Vifm 預設的兩個檢視頁面的作用在此顯現出來：如果輸入了 `:copy`，檔案並不會進入「待貼上」的狀態，而是直接從當前頁面的資料夾貼到另一個頁面的資料夾。比如，左邊在 `/etc/`，右邊在 `~/.config/`，我在左邊對著 `vifm/` 輸入 `:copy`，就會立刻執行 `cp /etc/vifm ~/.config/`。


| 指令       | 意義           |
| -------- | ------------ |
| `copy`   |              |
| `move`   |              |
| `delete` |              |
| `link`   |              |
| `view`   | toggle 預覽功能。 |


## 設定檔

vifm 的設定文件存放在 `~/.config/vifm/`。主要設定檔是 `vifmrc`。

### 改變預設編輯器

在 `vifmrc` 中搜尋「edit files」應該可以發現有一些預設設定。他最高優先級是使用 vim。我這樣修改來覆蓋掉他的選項：

```diff
+if 1
+    set vicmd=nvim
+elseif executable('vim')
-if executable('vim')
    set vicmd=vim
elseif executable('nvim')
    set vicmd=nvim
elseif executable('elvis')
    set vicmd=elvis\ -G\ termcap
elseif executable('vile')
    set vicmd=vile
elseif $EDITOR != ''
    echo 'Note: using `'.$EDITOR.'` as an editor'
    let &vicmd = $EDITOR
endif
```

### 顯示隱藏檔案

[Code Yarn - How to show hidden files in Vifm](https://codeyarns.com/tech/2014-09-10-how-to-show-hidden-files-in-vifm.html)

視窗指令切換可以用以下熱鍵。注意到（如果沒有設置 `windo`）顯示/不顯示的設定會留至下一次啟動 `vifm`。

| 指令   | 作用  |
| ---- | --- |
| `za` | 切換  |
| `zo` | 顯示  |
| `zm` | 不顯示 |

[GitHub/vifm - Issue#5: option to set "show hidden/dotfiles" by default](https://github.com/vifm/vifm/issues/5)

在 `vifmrc` 中設置 `windo` 指令可以在 vifm 啟動時固定開啟/關閉顯示隱藏檔案。

```
windo normal zo
```

### 離開時自動 cd 到目錄

[Vifm Wiki - How to set shell working directory after leaving Vifm](https://wiki.vifm.info/index.php/How_to_set_shell_working_directory_after_leaving_Vifm)

在 `.bashrc` 加入以下指令：

```shell
vicd()
{
    local dst="$(command vifm --choose-dir - "$@")"
    if [ -z "$dst" ]; then
        echo 'Directory picking cancelled/failed'
        return 1
    fi
    cd "$dst"
}
```

然後，想要造成這個效果時，改使用 `vicd` 來打開 Vifm。