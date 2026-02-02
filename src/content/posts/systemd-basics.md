---
title: "[Notes] Systemd Commands"
category: IT筆記
published: 2026-01-08 00:00:00
tags:
  - Systemd
---
名詞釋義：在本文中我們稱「登錄」為將服務設定為開機自動啟動。

## Systemctl
啟動並登錄。

```bash
sudo systemctl start <unit name>
```

```bash
sudo systemctl enable <unit name>
```

```bash
sudo systemctl enable --now <unit name>
```

## Journalctl

觀看所有的 log。註：加 `-r`(Reverse) 是因為預設為從最老的紀錄開始，反轉之後才是最新的。

```bash
journalctl -r [unit name]
```

```bash
journalctl -f [unit name]
```

