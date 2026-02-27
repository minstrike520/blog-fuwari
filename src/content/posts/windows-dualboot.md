---
title: Dual Boot Windows in Arch Linux
published: 2025-09-15
tags:
  - Windows
  - 作業系統
category: IT筆記
---
Ref: [How To Dual Boot Arch Linux and Windows 11 - YouTube](https://www.youtube.com/watch?v=QTVQpvSoSIA)

```shell
sudo fdisk -l
```

gets partition detail There should be a partition called “EFI System”.

```shell
blkid
```
lists every partitions’ UUID. Note the EFI System one.

Reboot into EFI shell. Identify the EFI system partition and note its “Alias” field.

```shell
sudo pacman -S edk2-shell
cp /usr/share/edk2-shell/x64/Shell.efi /boot/efishellx64.efi
```


```shell title=/boot/loader/entries/efishellx64.conf
title	UEFI Shell x64
efi	/efishellx64.efi
```