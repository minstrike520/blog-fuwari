---
title: ADB 的妙用：手機投影與控制
published: 2026-01-23
tags:
  - ADB
  - Android
category: IT筆記
---
## **手機端設定**

僅以小米 13T Pro 為例。在更多設定 > 開發者選項，打開「USB 偵錯」、「無線偵錯」、「USB 偵錯（安全設定）」。

## 連接

用無線裝置的話，要先進行配對。沒有配對的話無法連接。

```
adb pair $IP:$PORT
```

在手機端我會使用「使用配對碼配對裝置」。

```bash
adb connect $IP:$PORT 
```

## 開啟視訊通道

```
scrcpy -s $IP:$PORT --max-fps=60 --video-bit-rate 2M
```

## 解除連接

```
adb disconnect $IP:$PORT
```

也可以不指定裝置（`adb disconnect`），這樣會把所有裝置都移除。

## ADB 功能節選

旋轉螢幕：

```shell
adb shell settings put system user_rotation 1 # 橫放
adb shell settings put system user_rotation 0 # 直放
```