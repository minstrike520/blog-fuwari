---
title: 【雜記】Termux
published: 2024-11-12
tags:
  - Termux
  - Android
category: IT筆記
---
*遷移自 HackMD*

## Termux Widget
[Termux:Widget official Github page](https://github.com/termux/termux-widget?tab=readme-ov-file#Installation)

![img-termux-miscs-1](img-termux-miscs-1.png)

- Download Termux:Widget installation apk from [Termux:Widget GitHub Release Page](https://github.com/termux/termux-widget/releases)
- Install the apk
```bash
# at Termux ~/
mkdir .shortcuts
chmod 700 -R .shortcuts/
```
- Then move the desired scripts into the `.shortcuts/` folder
- (At Android Home Page) Create a widget
- The scripts should show on the widget list (as shown above)

## 改字型
[Reference(Youtube vid)](https://youtu.be/yfAtL6Ji684?si=37HHouwYfZDkBw5b)
```bash
cp <the ttf chosen> ~/.termux/font.ttf
```

## ESC Key
Editing `~/.termux/termux.properties`
```bash
#...
# Back Key
back-key=escape
#...
```

## Login Script and MOTD(Message of Today)
[Reference](https://www.reddit.com/r/termux/comments/bgdrrh/personalizing_your_termux_greeting_instructions/)
- `~/../usr/etc/motd`
- `~/../usr/etc/termux-login.sh`

## Host sshd Service
**HOSTING**
```bash
passwd # 設定termux的密碼(如果已設定則可略過)
pkg install openssh
sshd
```
**CONNECTING FROM CLIENT**
不像一般的sshd埠號開放22，Termux對外開放的埠固定為8022。
```
ssh u0_a256@<IP_ADDR> -p 8022
```