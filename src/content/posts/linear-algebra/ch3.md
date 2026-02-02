---
title: "Linear Algebra - Chapter 3: Determinants"
published: 2025-10-21
category: linear-algebra
---
[課程總覽](../)
## 3-1 Cofactors
### Motivation: Determinants in 2x2 Matrices
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix} \begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix} = \begin{bmatrix}
a d - b c  & 0 \\
0 & a d - b c 
\end{bmatrix} = (ad - b c) I_{2}
$$
左右顛倒，關係依舊。由此可證得二階反方陣公式，並將係數 $ad - b c$ 命名為「determinant」。

### Defninition of Determinant
一階 determinant 就是該元素自身。
二階 determinant 為 $ad -bc$。

### Cofactor Expansion
定義一個新的表記：$A_{ij}$ 表示將 $A$ 之第 $i$ row 跟第 $j$ column 移除所得之新矩陣。如此即可形式化定義三階以上的 determinant：
$$
\det A = a_{11} A_{11} - a_{12} A_{12} + \dots + (-1)^{1+n} \cdot a_{1n} A_{1n}
$$
- $(-1)^{1+n}$ 說了一件事，正負相間是從 $1,1$ i.e. 左上角開始起算，從別的角度算的話，只要該邊大小為偶數就會算錯喔。

**Cofactor**: 以上 $A_{ij}$ 的值還可以表記為 $c_{ij}$，讀做「$(i,j)$ cofactor of $A$」。（CALLOUT: *p203*）
$$
c_{i j } = (-1)^{i + j}
$$
### A Special Case
> [!Note] Theorem
> $$
> M = \begin{bmatrix}
> A & B \\
> O & I_{n}
> \end{bmatrix}
> $$
> 對於以上形式的矩陣，當 $A$ 為方陣，則 $\det M = \det A$ 成立。

再舉個 trivial case：
> [!Quote] 類對角矩陣
> 
> $$
> \det \begin{bmatrix}
> C & O \\
> O' &  I_{n}
> \end{bmatrix} = \det \begin{bmatrix}
> I_{m} & O' \\
> O  & C
> \end{bmatrix} = \det C
> $$

### Triangular Matrices
> [!Note] Theorem
>對於上下三角矩陣 $M$，其 determinant 為其對角線項目的積。


## 3-2 Properties of Determinants
### Elementary Operations and Determinants

| 運算   | 結果  |
| ---- | --- |
| 行交換  | 變號  |
| 同行縮放 | 縮放  |
| 異行消長 | 不變  |
依照這些性質，結合 3-1 所述三角矩陣，可以得到以下計算 determinant 的方法：
> [!Quote] 利用上三角矩陣計算 determinant
> 透過對 $R$ 進行一系列基礎列運算，可得上三角矩陣 $U$，而
> $$
> \det R = (-1)^{r} \cdot u_{11} u_{22} \dots u_{nn}
> $$
> $r$ 是行交換的次數。

### Four Properties of Determinants
1. 若且唯若：「可逆」與「determinant 不為零」
2. 對方陣乘法具有分配律
3. 轉置不改變
4. 反方陣變倒數

> [!Quote] 利用**分配律**以及**基礎運算矩陣**對矩陣進行元素化
> 已知列運算可用矩陣來表示，又，列運算必能將矩陣化為 $I_{n}$，則
> $$
> A = E_{k} E_{k-1} \dots E_{2}E_{1}
> $$
> 再根據 determinant 對方陣乘法的分配律，
> $$
> \det A = (\det E_{k}) (\det E_{k - 1})\dots (\det E_{2})(\det E_{1})
> $$

- 同理，「轉置不改變」這個性質也可以透過這樣的關係式證得。
## Cramer's Rule 
> [!Note] Theorem
> $A$, $\mathbf{b}$; $M_{i}$: replace column $i$ of $A$ by $\mathbf{b}$.
> Then, equation $A\mathbf{x} = \mathbf{b}$ has unique solution $\mathbf{u}$ where $u_{j} = \frac{\det M_{j}}{\det A} \forall j$.

**PROOF**
$$
A\mathbf{u} = \mathbf{b}. \ \mathbf{u} = A^{-1} \mathbf{b}.
$$
Let $U_{i}$: replace column $i$ of $I_{n}$ bt $\mathbf{u}$.
Then
$$
\begin{aligned}
AU_{i} & = A[\mathbf{e}_{1}\ \mathbf{e}_{2} \dots  \mathbf{e}_{i - 1}\ \mathbf{u}\ \mathbf{e}_{i+1}  \dots \mathbf{e}_{n} ]  \\
 & = [A\mathbf{e}_{1} \ A\mathbf{e}_{2} \dots A \mathbf{u}  \dots A\mathbf{e}_{n}] \\
 & = [\mathbf{a}_{1} \ \mathbf{a}_{2} \dots \mathbf{b} \ \mathbf{a}_{n}] \\
 & = M_{i}
\end{aligned}
$$
(cofactor expansion)
$$
\det U_{i} = u_{i} \cdot \det I_{n - 1} = u_{i}
$$
$$
(\det A)(\det U_{i} )  = \det M_{i}
$$
$$
u_{i} = \frac{\det A}{\det M_{i}} \ \blacksquare
$$