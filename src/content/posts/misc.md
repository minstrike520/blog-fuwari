---
title: 雜項筆記
published: 2026-01-23
tags:
  - 雜項
category: IT筆記
---
暫放一些還沒有整理的筆記。

---

### EFI Microsoft is Lost

Use Windows installation medium to “Repair my PC ”

### Pyright Setup in uv

```toml
[tool.pyright]
venvPath = ""
venv = ".venv"
```

### Arch Linux Update Pacman Keys

```bash
ssh-keygen  
sudo pacman-key --init  
sudo pacman-key --populate  
sudo pacman -S archlinux-keyring  
```

### Termux Nerdfont Oneline Setup

```bash
cd ~/; wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/JetBrainsMono.zip; unzip -d jfonts JetBrainsMono.zip; cp JetBrainsMonoNerdFontMono-Medium.ttf ~/.termux/font.ttf
```
  
### Ext4 DiskRecover

Software: [Ext4Magic](https://gist.github.com/coldfix/21c16e066b3ff05aa34c553d65a39e34)

### I should not write flash disk mounting data in /etc/fstab

比如 `/dev/sda1` 如果你先寫入說他是ntfs，然後下次開機你第一個插入的是ext4，那不是就衝突了？  