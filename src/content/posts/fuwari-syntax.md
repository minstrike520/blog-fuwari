---
title: Fuwari 語法總集
published: 2026-02-02
tags:
  - Fuwari
category: IT筆記
description: 將 Fuwari 的預設教學整理成單一貼文。
---
## 檔案結構

### 貼文 metadata

```yaml
title: My First Blog Post
published: 2023-09-09
description: This is the first post of my new Astro blog.
image: ./cover.jpg # Optional
tags: [Foo, Bar]
category: Front-end
draft: false
```

### 圖片

```
src/content/posts/
├── post-1.md
└── post-2/
    ├── cover.png
    └── index.md
```

## Markdown Extended

### GitHub Card

```
::github{repo="minstrike520/blog-fuwari"}
```

::github{repo="minstrike520/blog-fuwari"}

### GitHub-styled Callouts

> [!NOTE]  
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.

## 程式語法

[Expressive Code](https://expressive-code.com/key-features/syntax-highlighting/)

### 隱藏字元

```
:spoiler[你知道的太多了]
```

隱藏字元在此：「:spoiler[你知道的太多了]」

### 跳脫字元

```ansi
[1;4mStandard ANSI colors:[0m
- Dimmed:     [2;30m Black [2;31m Red [2;32m Green [2;33m Yellow [2;34m Blue [2;35m Magenta [2;36m Cyan [2;37m White [0m
- Foreground: [30m Black [31m Red [32m Green [33m Yellow [34m Blue [35m Magenta [36m Cyan [37m White [0m
- Background: [40m Black [41m Red [42m Green [43m Yellow [44m Blue [45m Magenta [46m Cyan [47m White [0m
- Reversed:   [7;30m Black [7;31m Red [7;32m Green [7;33m Yellow [7;34m Blue [7;35m Magenta [7;36m Cyan [7;37m White [0m

[1;4m8-bit colors (showing colors 160-171 as an example):[0m
- Dimmed:     [2;38;5;160m 160 [2;38;5;161m 161 [2;38;5;162m 162 [2;38;5;163m 163 [2;38;5;164m 164 [2;38;5;165m 165 [2;38;5;166m 166 [2;38;5;167m 167 [2;38;5;168m 168 [2;38;5;169m 169 [2;38;5;170m 170 [2;38;5;171m 171 [0m
- Foreground: [38;5;160m 160 [38;5;161m 161 [38;5;162m 162 [38;5;163m 163 [38;5;164m 164 [38;5;165m 165 [38;5;166m 166 [38;5;167m 167 [38;5;168m 168 [38;5;169m 169 [38;5;170m 170 [38;5;171m 171 [0m
- Background: [48;5;160m 160 [48;5;161m 161 [48;5;162m 162 [48;5;163m 163 [48;5;164m 164 [48;5;165m 165 [48;5;166m 166 [48;5;167m 167 [48;5;168m 168 [48;5;169m 169 [48;5;170m 170 [48;5;171m 171 [0m
- Reversed:   [7;38;5;160m 160 [7;38;5;161m 161 [7;38;5;162m 162 [7;38;5;163m 163 [7;38;5;164m 164 [7;38;5;165m 165 [7;38;5;166m 166 [7;38;5;167m 167 [7;38;5;168m 168 [7;38;5;169m 169 [7;38;5;170m 170 [7;38;5;171m 171 [0m

[1;4m24-bit colors (full RGB):[0m
- Dimmed:     [2;38;2;34;139;34m ForestGreen - RGB(34,139,34) [2;38;2;102;51;153m RebeccaPurple - RGB(102,51,153) [0m
- Foreground: [38;2;34;139;34m ForestGreen - RGB(34,139,34) [38;2;102;51;153m RebeccaPurple - RGB(102,51,153) [0m
- Background: [48;2;34;139;34m ForestGreen - RGB(34,139,34) [48;2;102;51;153m RebeccaPurple - RGB(102,51,153) [0m
- Reversed:   [7;38;2;34;139;34m ForestGreen - RGB(34,139,34) [7;38;2;102;51;153m RebeccaPurple - RGB(102,51,153) [0m

[1;4mFont styles:[0m
- Default
- [1mBold[0m
- [2mDimmed[0m
- [3mItalic[0m
- [4mUnderline[0m
- [7mReversed[0m
- [9mStrikethrough[0m
```

### 標注

````markdown
```js {1, 4, 7-8}
// Line 1 - targeted by line number
// Line 2
// Line 3
// Line 4 - targeted by line number
// Line 5
// Line 6
// Line 7 - targeted by range "7-8"
// Line 8 - targeted by range "7-8"
```
````


```js {1, 4, 7-8}
// Line 1 - targeted by line number
// Line 2
// Line 3
// Line 4 - targeted by line number
// Line 5
// Line 6
// Line 7 - targeted by range "7-8"
// Line 8 - targeted by range "7-8"
```

### 關閉行號

```c showLineNumbers=false
#include <stdio.h>

int main() {
    printf("this is awesome!");
	return 0;
}
```