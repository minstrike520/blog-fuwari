---
title: Cloudflare Basics
tags:
  - IT-Basics
  - Cloudflare
category: IT筆記
published: 2025-12-30 23:41:00
updated: 2025-12-30 23:41:00
---
在沒有固定外部 IP（Public IP）且位於 NAT（如宿舍、公司內部網路）後方的環境下，最現代、安全且簡單的解決方案是使用 **Cloudflare Tunnel**。

這項技術會在你的樹莓派與 Cloudflare 伺服器之間建立一條加密通道。當使用者訪問你的網域時，Cloudflare 會將流量透過這條通道導向你的樹莓派，你**不需要**在路由器上設定 Port Forwarding。

---

## 【伺服器端】安裝

首先，在裝置上安裝 Cloudflare 提供的工具 `cloudflared`。這個套件沒有在官方的套件庫裡面，所以要自己抓 `.deb` 下來安裝。

```bash
sudo apt update && sudo apt install curl -y
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64.deb -o cloudflared.deb
sudo dpkg -i cloudflared.deb
```

使用瀏覽器登入 Cloudflare 進行授權與設定。

```bash
cloudflared tunnel login
```

建立隧道。

```bash
cloudflared tunnel create <tunnel name>
```

執行後會得到 Tunnel ID。

在 `~/.cloudflared/` 資料夾下建立設定檔，告訴 Cloudflare 如何轉發流量。

```yaml
tunnel: <您的 Tunnel ID>
credentials-file: /home/pi/.cloudflared/<Tunnel ID>.json

ingress:
  - hostname: mydomain.com
    service: http://localhost:80
  - service: http_status:404
```

將你的網域指向這個隧道，並啟動它：

```bash
cloudflared tunnel route dns pi-server mydomain.com
cloudflared tunnel run <tunnel name>
```

## 【伺服器端】啟動服務

`cloudflared` 支援 systemd service，但需要手動安裝。

```bash
sudo cloudflared service install
# sudo systemctl enable --now cloudflared
```

## 【客戶端】SSH 導流

在 `$HOME/.ssh/config` 加入以下條件。

```bash
echo \
"Host ssh.mydomain.com
	ProxyCommand cloudflared access ssh --hostname %h" \
| tee -a $HOME/.ssh/config > /dev/null
```

注意：在沒有設定導流的情況下，對 `ssh.mydomain.com` 的連線會毫無回應，SSH 也不會報錯。