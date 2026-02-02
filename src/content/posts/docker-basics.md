---
title: Docker Basics
tags:
  - IT-Basics
  - Docker
category: IT筆記
published: 2025-12-30 16:04:00
---
## 更新

官網有對個別系統的安裝方式做出解釋，比如 [Debian](https://docs.docker.com/engine/install/debian/)。

## 啟用

啟動 docker.service（使用 systemd 的場合）。這邊也可以執行一次 `enable` 或 `enable --now`，就會開機自動啟動。不過我個人習慣手動開啟。（應該多少能加快一點開機速度吧？）

```bash
systemctl start docker
```

## 權限設定

如果沒有特別設定，Docker 的執行是需要 root 權限的。但是每次執行指令，就算只是 `docker ps`　這樣微不足道的指令也要 root 實在是有點麻煩。為此 Docker 有一個特別機制，它會在系統裡面使用「Docker」群組，只要是加入了這個群組的使用者，使用 `docker` 指令都不用 `sudo`。

首先，檢查系統是否已經有名為 `docker` 的群組。如果沒有就手動新增一個：

```shell
sudo groupadd docker
```

將使用者加入 `docker` 群組：

```shell
sudo usermod -aG docker $USER
```

系統要重新啟動，設定才會永久生效。如果想要暫時生效，可以臨時以 `docker` 群組身份登入（只在當前的 shell 環境有效）：

```shell
newgrp docker
```

## 映像檔管理

從官方「<ruby>映像檔倉庫<rt>registry</rt></ruby>」下載現成的 image。

```bash
docker pull <IMAGE_NAME>
```

根據 `./Dockerfile` 來建置 image。

```bash
docker build -t <IMAGE_NAME> .
```

產生一次性的容器，並在其中執行指令（此處為 `/bin/sh`）。

```bash
docker run --rm -it --entrypoint /bin/sh <IMAGE_NAME>
```

## 容器管理

啟動非活躍狀態的 container。

```bash
docker start <CONTAINER_NAME>
```

中止活躍狀態的 container。

```bash
docker stop <CONTAINER_NAME>
```

產生一個新的 container 並執行。相當於 `docker create` 跟 `docker start`。

```bash
docker run --name <CONTAINER_NAME> <IMAGE_NAME> 
```

執行 container 內的指令。

```bash
docker exec -it <CONTAINER_NAME> <COMMAND ...>
```

執行一個新的 container 並指派一個指令，該 container 會隨著指令結束而自動移除。

```bash
docker run --rm -it --entrypoint /bin/sh <IMAGE_NAME>
```