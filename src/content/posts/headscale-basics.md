---
title: Headscale Basics
published: 2025-12-31 10:24:00
updated: 2025-12-31 10:24:00
tags:
  - IT-Basics
  - Tailscale
category: IT筆記
---
https://headscale.net/stable/setup/install/container

https://ettoreciarcia.com/publication/26-network-overlay/


官方的教學中有提供跑 docker container 的腳本。

```bash
docker run \
  --name headscale \
  --detach \
  --volume "$(pwd)/config:/etc/headscale" \
  --volume "$(pwd)/lib:/var/lib/headscale" \
  --volume "$(pwd)/run:/var/run/headscale" \
  --publish 127.0.0.1:8080:8080 \
  --publish 127.0.0.1:9090:9090 \
  --health-cmd "CMD headscale health" \
  docker.io/headscale/headscale:<VERSION> \
  serve --
```

確認有跑起來之後，可以使用以下 docker 指令執行 headscale 操作。 

```bash
docker exec -it headscale headscale [command]
```

## 常見指令

常用的指令如下所列。（以下內容應填入 `[command]`）

- 列出使用者 `users ls`
- 新增使用者 `users create <USER_NAME>`
- 註冊節點 `nodes register --key <CLIENT_KEY> --user <USER_NAME>`
- 列出節點 `nodes ls`

## Tailscale 對應
- 上線 `tailscale up --login-server <SERVER_ADDRESS>`
- 下線 `tailscale down`
- 登入 `tailscale login`
	- 雖然這個是拿來連接官方 VPN 的，但無意間發現，當 `up` 指令的 `to authenticate...` 提示消失時，執行這個指令之後好像會重設。

## 手機加入 Headscale 網路
設定圖標 > Accounts > 右上角按鈕 > Use an alternate server 