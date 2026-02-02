---
title: 網管筆記
published: 2026-01-06
tags:
  - 網路管理
category: IT筆記
---
資料參考：

- [howarde8 - iThome 鐵人賽：網路通訊隨意聊](https://ithelp.ithome.com.tw/users/20128159/ironman/6699)
- [Johnny Huang - 網路概論](https://jonny-huang.github.io/else/01_net_01/)

# OSI Model

OSI：Open Systems Interconnection (Model)

本模型將資料劃分成七個 layer：

1. Physical Layer
2. Data Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

# L2/MAC

## L2 Switch
點對點的連接。按照來源地址（MAC）將資料往相鄰的裝置發送。管理一張 **MAC-埠表**表示相鄰的裝置。

# L3/IP
## IP Address
IP：Internet Protocol Address

## IP 存在的意義

MAC 只能根據埠來尋找裝置，而當連接組態有所變動時就會失效。而 IP 是一種層級式的位址，讓我們可以根據需要劃分分區。

## 網段

網段即一段連續的 IP 位址。例：`0.0.0.0/8` 即限制前 8 位元的網段；`192.168.0.0/24` 即限制前 24 位元的網段。

## ARP
ARP：Addresss Resolution Protocol

ARP 表示將 IP「解析」為 MAC。在一台裝置上會儲存自己所連接的裝置的 MAC-IP 表。當系統內有人請求一個沒儲存過的 IP，該裝置就會在網路中發起廣播，請求該 IP 的 MAC，然後再新增進表格中。

# Gateway
## routing table

表示特定 IP 的資料所需經過的節點。表格的鍵是「位址／網段（DST）」，值是「出口 IP（PERFSRC）」。

除此之外，表格還有一欄顯示「Gateway」。無顯示或顯示「on link」的表示該裝置可以直接取得 MAC；除此之外有顯示 IP 者，則表示會送往該閘道器進行轉送。


# DHCP

DHCP：Dynamic Host Configuration Protocol

1. DHCP Discover (C)
2. DHCP Offer (S)
3. DHCP Request (C)
4. DHCP ACK (S)


# Routing

傳統的 (L2) Switch 只能點對點進行資料交換，針對一個「從起點到終點有很多路徑可以選擇」的情境則無法應對；這種情況則需要 router。

## NAT

NAT：Network Address Translation

路由器在轉送封包之前，會先將來源 IP 轉成外部 IP，這樣遠端才能正常地將回應封包傳回來。

一個路由器會連接多個裝置，此時從外部來的封包要傳給哪個裝置，是路由器需要處理的事。注意到以 TCP/IP 協定傳送的封包會註記埠號，遠端便能根據來源標記的埠號回傳，接著路由器便能轉送到該埠號對應的裝置。

> 雖然 IP 位址是遠端主機，但是從目的端的 MAC 位址就知道，其實我們電腦面對的始終都是路由器。

> 雖然地址填寫的是門牌號碼，但我們寄送者要寄東西時，去的始終都是郵局。

注意到 router 跟 gateway 主要的差別是，router 會將資料中的 IP 改掉再發送，而 gateway 只會將資料直接轉發。

## Port Forwarding

當我們有 router 的存取權時，可以在 routing table 上加入一個固定規則：當接收到特定埠號的封包時，便用 NAT 解析成特定裝置。

例：固定將目標埠號為 443 的外部請求轉發到某一台伺服器。

## NAT Traversal

例：ngrok

1. 建立通道。伺服器向 ngrok 發送「開始連線」的封包。
2. 取得網址。ngrok 為伺服器分配一個網址。
3. 轉發。網際網路中有人向該網址發出請求時，ngrok 會透過通道將該請求轉發給裝伺服器。

