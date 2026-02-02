---
title: NVidia 韌體更新失敗
published: 2025-06-22
tags:
  - Arch_Linux
  - NVidia顯示卡
category: IT 除錯紀錄
---
```
(29/29) checking for file conflicts                                                                               [####################################################################] 100%
error: failed to commit transaction (conflicting files)
linux-firmware-nvidia: /usr/lib/firmware/nvidia/ad103 exists in filesystem
linux-firmware-nvidia: /usr/lib/firmware/nvidia/ad104 exists in filesystem
linux-firmware-nvidia: /usr/lib/firmware/nvidia/ad106 exists in filesystem
linux-firmware-nvidia: /usr/lib/firmware/nvidia/ad107 exists in filesystem
Errors occurred, no packages were upgraded.
```

---

搜尋到以下內容：（兩小時前公告）

https://archlinux.org/news/linux-firmware-2025061312fe085f-5-upgrade-requires-manual-intervention/

執行
```bash
pacman -Rdd linux-firmware
pacman -Syu linux-firmware
```

就好了。相當於把這個套件移除再重新安裝，便可以解決這個問題。