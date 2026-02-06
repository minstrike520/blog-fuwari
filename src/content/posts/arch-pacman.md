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
[0;1mName            :[0m pacman
[0;1mVersion         :[0m 7.1.0.r9.g54d9411-1
[0;1mDescription     :[0m A library-based package manager with dependency support
[0;1mArchitecture    :[0m x86_64
[0;1mURL             :[0m https://www.archlinux.org/pacman/
[0;1mLicenses        :[0m GPL-2.0-or-later
[0;1mGroups          :[0m None
[0;1mProvides        :[0m libalpm.so=16-64
[0;1mDepends On      :[0m bash  coreutils  curl  libcurl.so=4-64  gawk  gettext  glibc  gnupg  gpgme  libgpgme.so=45-64  grep  libarchive  libarchive.so=13-64  openssl  libcrypto.so=3-64  pacman-mirrorlist  systemd  libmakepkg-dropins
[0;1mOptional Deps   :[0m base-devel: required to use makepkg [installed]
                  perl-locale-gettext: translation support in makepkg-template
[0;1mRequired By     :[0m archlinux-keyring  base  base-devel  pacseek  paru  yay
[0;1mOptional For    :[0m None
[0;1mConflicts With  :[0m None
[0;1mReplaces        :[0m None
[0;1mInstalled Size  :[0m 5.01 MiB
[0;1mPackager        :[0m Morten Linderud <foxboron@archlinux.org>
[0;1mBuild Date      :[0m Tue Jan 13 04:27:06 2026
[0;1mInstall Date    :[0m Wed Jan 28 09:24:34 2026
[0;1mInstall Reason  :[0m Installed as a dependency for another package
[0;1mInstall Script  :[0m No
[0;1mValidated By    :[0m Signature
```

可以運用 grep 等搜尋機能來進行更細緻的篩選。

比如，以下指令可以篩選出「屬於 plasma 群組的套件」。註，`grep -B <number>` 的含意是在輸出時把搜尋結果前 `<number>` 行的上文也一併輸出。

```bash
LANG= pacman -Qi | grep -B 15 "Groups          : plasma" | grep Name
```
