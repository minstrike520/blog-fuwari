---
title: '[Notes] Pacman Commands'
published: 2026-01-08
updated: 2026-01-08
tags:
  - Arch_Linux
category: IT筆記
---
- **原生/外來套件**：`-n` (Native), `-m` (Foreign)
- **指定/依賴**：`-e` (Explicit), `-d` (Dependency)

`-i` 可以顯示套件的所有資訊。

```
$ LANG= pacman -Qi pacman  
Name            : pacman  
Version         : 7.1.0.r7.gb9f7d4a-1  
Description     : A library-based package manager with dependency support  
Architecture    : x86_64  
URL             : https://www.archlinux.org/pacman/  
Licenses        : GPL-2.0-or-later  
Groups          : None  
Provides        : libalpm.so=16-64  
Depends On      : bash  coreutils  curl  libcurl.so=4-64  gawk  gettext  glibc  gnupg  gpgme  libgpgme.so=45-64  grep  libarchive  libarchive.so=13-64  
                 openssl  libcrypto.so=3-64  pacman-mirrorlist  systemd  libmakepkg-dropins  
Optional Deps   : base-devel: required to use makepkg [installed]  
                 perl-locale-gettext: translation support in makepkg-template  
Required By     : archlinux-keyring  base  base-devel  pacseek  yay  
Optional For    : None  
Conflicts With  : None  
Replaces        : None  
Installed Size  : 5.01 MiB  
Packager        : Antonio Rojas <arojas@archlinux.org>  
Build Date      : Fri Dec 12 21:03:39 2025  
Install Date    : Wed Jan 7 10:46:00 2026  
Install Reason  : Installed as a dependency for another package  
Install Script  : No  
Validated By    : Signature
```

可以運用 grep 等搜尋機能來進行更細緻的篩選。

比如，以下指令可以篩選出「屬於 plasma 群組的套件」。註，`grep -B <number>` 的含意是在輸出時把搜尋結果前 `<number>` 行的上文也一併輸出。

```bash
LANG= pacman -Qi | grep -B 15 "Groups          : plasma" | grep Name
```
