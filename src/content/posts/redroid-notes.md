---
title: "Redroid: Linux 系統的安卓模擬器"
published: 2025-11-04
tags:
  - ADB
  - Android
category: IT筆記
---
關於 ADB 跟 scrcpy 的使用方式，可見另一篇：[ADB 的妙用：手機投影與控制](/posts/adb-and-scrcpy/)
關於 Docker 的使用方式可見[Docker Basics](/posts/docker-basics)

## 安裝

```shell
pacman -S linux-zen docker adb scrcpy python lzip

git clone https://github.com/ayasa520/redroid-script
cd redroid-script

sudo venv/bin/python redroid.py -a 11.0.0 -gmn
```

## 執行

```shell
sudo docker run -itd --rm --privileged \
    -v ~/data:/data \
    -p 5555:5555 \
    redroid/redroid:11.0.0_gapps_ndk_magisk \
	androidboot.redroid_gpu_mode=host \
	androidboot.redroid_fps=60 \
	androidboot.redroid_width=1080 \
	androidboot.redroid_height=1920 \
	ro.product.cpu.abilist=x86_64,arm64-v8a,x86,armeabi-v7a,armeabi \
    ro.product.cpu.abilist64=x86_64,arm64-v8a \
    ro.product.cpu.abilist32=x86,armeabi-v7a,armeabi \
    ro.dalvik.vm.isa.arm=x86 \
    ro.dalvik.vm.isa.arm64=x86_64 \
    ro.enable.native.bridge.exec=1 \
    ro.vendor.enable.native.bridge.exec=1 \
    ro.vendor.enable.native.bridge.exec64=1 \
    ro.dalvik.vm.native.bridge=libndk_translation.so \
    ro.ndk_translation.version=0.2.3 \
```

## 連接

```shell
adb connect localhost:5555
scrcpy -s localhost:5555 --max-fps=60 --video-bit-rate 2M
```

## 停止

```shell
adb disconnect localhost:5555; sudo docker ps -q | xargs sudo docker stop
```

## 其他小工具




```shell
sudo docker run -itd --rm --privileged     --pull always     -v ~/data11:/data     -p 5555:5555     --name redroid12     redroid/redroid:12.0.0-latest androidboot.redroid_gpu_mode=host androidboot.redroid_fps=60
```

```
sudo docker run -itd --rm --privileged \
    -v ~/data:/data \
    -p 5555:5555 \
    redroid/redroid:11.0.0_gapps \
	androidboot.redroid_gpu_mode=host \
	androidboot.redroid_fps=60
```