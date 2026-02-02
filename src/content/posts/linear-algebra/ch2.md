---
title: "Linear Algebra - Chapter 2: Matrices and Linear Transformations"
published: 2025-10-21 10:00:00
category: linear-algebra
---
[課程總覽](../)
## 2-1 Matrix Multiplication
- 矩陣乘法可以用 matrix-vector product 來定義。
- 矩陣沒有交換律。
- $\mathbf{u}^{T}\mathbf{v}$ 所得為一個 $1\times 1$ 矩陣 $[ \mathbf{u} \cdot \mathbf{v}]$。所以要取純量時記得用點積，不要用矩陣乘法。
- 對稱矩陣：$A^{T}=A$

## 2-3 Invertibility and Elementary Matrices
> [!Abstract] DEF. Inverse
> $$
A A^{-1} = A^{-1} A = I_{n}
> $$

### 逆矩陣的唯一性
證明方法：先假設他不唯一，設第三個矩陣也符合逆矩陣的定義，然後推得它與原本的逆矩陣相等。

### 元素矩陣
即從單位矩陣進行一次 e.r.o. 得來。

### $A^{-1}B$ 特殊算法
$$
[A\ B] \to [I_{n}\ C], \ C = A^{-1} B
$$

## Linear Transformation
定義：「保留**向量加法**與**純量乘法**者為線性變換。」
向量加法 vector addition
$$
T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})
$$
純量乘法 scalar multiplication
$$
T(c \mathbf{u}) = c \cdot T(\mathbf{u})
$$
零向量
$$
T(\mathbf{0}) = \mathbf{0}
$$
然而，反過來則不一定：
$$
T(X) = \mathbf{0} \not\implies X = \mathbf{0}
$$

### Standard Matrix
此詞彙沒有在
$$
A = [T(\mathbf{e}_{1}) T(\mathbf{e}_{2}) \dots T(\mathbf{e}_{n})]
$$

## 2.8 Composition and Invertibility of Linear Transformations
