---
title: Promoting Arch Linux
published: 2026-03-31
draft: true
category: 雜談
tags:
  - Arch_Linux
description: 本來寫 my-linux-setup，寫一寫發現好像偏題了。
---

總之，用到現在他有幾個特性我滿喜歡的：

**一、滾動更新**

相較於許多其他 distro 的更新會分版本，Arch Linux 採用的是「<ruby>滾動式更新<rt>rolling release</rt></ruby>」：直接把所有 package 攤開讓你 `pacman -Syu` 一口氣更新，沒有「系統版本」的概念。

滾動式更新的缺點就是，系統沒辦法為你保證軟體跟驅動程式的相容性。不過可能是我運氣好，至今很少遇到嚴重的更新問題。（又或許是我沒發現某些軟體問題跟這個有關）

滾動式更新最大的好處，就是可以用內建的 package manaer 安裝接近最新的軟體。比如說，在發文當下，[Neovim](https://neovim.io/)（一個文字編輯器）在 Ubuntu Packages 的版本是 0.10.4，而在 Arch Linux
Extra 卻是 0.11.6。

**二、AUR 生態**

有時候 Arch Linux 提供的官方 package release 不會提供某些 package，有些是因為太小眾、太新還沒被收錄，有的則是授權條款不允許他放，此時在別的系統，可能我們會選擇直接用別的套件管理器來安裝，如 pip 或 npm， 但是 Arch Linux 還有 AUR。

（詳見[什麼是AUR套件庫？如何安裝Arch Linux的AUR軟體？](https://ivonblog.com/posts/archlinux-aur-introduction/)）

假如軟體是開源的，AUR 可以幫你編譯；假如軟體只開放執行檔下載，AUR 可以幫你安裝。簡而言之，就是各種想得到的、想不到的都可以在 AUR 找到。

比如常用的 Google Chrome、Visual Studio Code 都沒有在官方 package list，我會用 AUR 下載。