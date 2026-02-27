---
title: 【三分鐘熱度】用程式寫音樂—Strudel
description: 三分鐘熱度的音樂製作探索。
published: 2026-02-27
tags:
  - 音樂製作
  - Strudel
category: hobby
draft: false
---
<center>＝＝＝施工中＝＝＝</center>

[Strudel 官方 Playground](https://strudel.cc/)

[Strudel 官方教學](https://strudel.cc/workshop/getting-started/)

## 啥是 Live Coding Music

直翻的話，live coding music 應該叫做「即時編程音樂」。就是一個利用程式語言來編曲的音樂製作方式。

## 之前的經驗

之前曾經嘗試過用 [Sonic Pi](https://sonic-pi.net/)（一樣是 live coding 的音樂製作軟體），但是用一用覺得不怎麼順手。

## 實際作品

```strudel
// @title FM youtube @by glossing

// samples('github:glossings/samples/main/fmdemo')

setcpm(130 / 4)

// To unmute anything below, just remove the underscore after
// the $

// FM basicsnote("<~ [0 1] 2 0 ~ [2 3] 4 0 ~ [4 5] [6 5] [6 5] [6 7] [7 6] 5 0 ~>*8").scale('e:minor').sound("sine")
// note("<~ [0 1] 2 0 4 [0 1] 2 0 4 ~ [4 5] [4 3] [2 ~] [2 1] 0 ~>*8")
// note('<0 1 2 ~ 0 ~ ~ ~ 2 3 4 ~ 0 ~>*16')
$: note(`<
             
2  ~  0  ~  ~  ~  2  3
4  ~  0  ~  ~  ~  4  5
6  6b 6  6b 6  7  6  5
4  ~  0  ~  ~  ~  0  1>*16`)
  .scale('e:minor').sound("sine")
//  .decay(0.5)
// .sustain(0.1)
  .room(2)

$: note("<7 4 7 4 9 6 7 4>*4").scale('e2:minor').sound('sine')
```
