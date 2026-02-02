---
title: 正則表達式—速查
published: 2026-01-26
tags:
  - 正規表達式
  - 形式語言
category: IT筆記
---
## 表示式參照表

### 字元指定

| 名稱               | 用處         |
| :--- | :------------- |
| `^`              | 字串開始處      |
| `$`              | 字串結束處      |
| `.`              | 非換行任意字元    |
| `\d` = `[0-9]`   | 數字         |
| `[a-z]`, `[A-Z]` | 英文         |
| `\D`             | 等價 `[^\d]` |
| `\s`             | 空白字元       |
| `\w`                                                                         | 單詞字元     |
 
### 字元集合

| 名稱       | 用處            |
| :--- | :------------- |
| `[abc]`  | a 或 b 或 c     |
| `[^abc]` | a,b,c 以外的任意字元 |

### 次數指定

| 名稱      | 用處                    |
| :--- | :------------- |
| `{n}`   | 發生 $n$ 次              |
| `{n,}`  | 至少發生 $n$ 次            |
| `{n,m}` | 至少發生 $n$ 次，至多發生 $m$ 次 |
| `+`     | 等價 `{0,}`             |
| `*`     | 等價 `{1,}`             |
| `?`     | 等價 `{0,1}`            |

### 子字串

`\1`：Python, sed

| 名稱      | 用處    |
| :--- | :------------- |
| `()`    | 取得    |
| `(?:)`  | 非取得   |
| `(?=)`  | 向前預查  |
| `(?!)`  | 向前反預查 |
| `(?<=)` | 向後預查  |
| `(?<!)` | 向後反預查 |

## Python 界面參照表

**搜尋**

| 名稱                    | 用處          | 回傳               |
| :-------------------- | :---------- | :--------------- |
| `re.compile()`        | 獲得可復用的表達式物件 | `re.Pattern`     |
| `(re\|pat).match()`   | 從字串頭開始配對    | `re.Match`       |
| `(re\|pat).search()`  | 搜尋第一個出現     | `re.Match`       |
| `(re\|pat).findall()` | 搜尋所有出現      | `List[re.Match]` |

## Python 實作範例

### 搜尋（search）

```python
import re
m = re.search(r"(myapp) ([0-9]\.[0-9])", "program version: myapp 5.5", re.NOFLAG)
print(m.group()) # myapp 5.5
print(m.group(2)) # 5.5
print(m.groups()) # ("myapp", 5.5) # (type: tuple)
```

### 完全符合（match）

```python
import re
m = re.match("AB", "ABCDE") # m = None
m = re.match("ABCDE", "ABCDE") # m = <re.Match object...>
```