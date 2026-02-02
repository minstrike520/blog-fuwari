---
title: "Linear Algebra - Chapter 1: Matrices and Linear Transformations"
published: 2025-10-07
category: linear-algebra
---
[課程總覽](../)

註：本文中行＝row，列＝column。

## 1.1 Matrices
**SPEC.** Matrix
直排的是 row vector，橫排的是 column vector。
vector 預設為 column vector。
在矩陣
$$
A = [a_{i,j}]_{m \times n}
$$
中，我們會說 $m$ 是矩陣的「行數」，而 $n$ 是「列數」；$a_{i,j}$ 是矩陣第 $i$ 行第 $j$ 列的「entry」。總的來說，對行列的敘述遵循著**先行後列**的規則。
英文中稱此為「dimension = $m$ by $n$」的矩陣。

> [!Abstract] DEF. Submatrix
> 子矩陣指的是原矩陣「刪去任意數量的行或列」。舉一個極端例：空矩陣為任意矩陣的子矩陣。

> [!Abstract] DEF. Row Vector and Column Vector
行數為一（$m = 1$）時，$A$ 為一個行向量；列數為一（$n = 1$）時，$A$ 為一個列向量。
由此可知，向量在結構上是矩陣的子集合。

> [!Abstract] DEF. Equality of Two Matrices
> 兩個矩陣若大小相同且對應的 entry 皆相等，則兩者相等。
> $A = B$ if $a_{i,j} = b_{i, j}$ for every $i$ and $j$.

**SKIPPED.** Transpose of Matrices

## 1.2 Linear Combinations
> [!Abstract] DEF. Linear Combination
> 給予一個 $k$ 個元素的集合 $S$ 以及元素 $u$。若存在 $k$ 個實數 $\alpha_{1}, \alpha_{2}, \dots, \alpha_{n}$ 使得
> $$
> u = \alpha_{1} s_{1} + \alpha_{2} s_{2} + \dots \alpha_{n} s_{n},
> $$
> 則$u$ 為 $S$ 的一個線性組合。

> [!Note] Theorem
> 若 $v$ 跟 $w$ 皆為 $S$ 的線性組合，則任何 $\{ v,w \}$ 的線性組合皆為 $S$ 的線性組合。

饒舌版：則 $\{ v, w \}$ 的線性組合集合必為 $S$ 的線性組合集合的子集合。
span 版：
$$
v, w \in \text{span}(S) \implies \text{span}(\{ v, w \}) \subseteq \text{span}(S)
$$

**SKIPPED.** Identity Matrices

> [!Abstract] DEF. Rotation Matrix
> $$
> R_{\theta} = \begin{bmatrix}
> \cos \theta  &  -\sin \theta \\
> \sin \theta & \cos \theta
> \end{bmatrix}
> $$


> [!Quote] Matrix-vector Product
> $$
> A \mathbf{b} = \mathbf{a}_{1} \mathbf{b} + \mathbf{a}_{2} \mathbf{b} + \dots + \mathbf{a}_{n} \mathbf{b}
> $$
> where $\mathbf{a}_{i}$ denotes $i$-th row of matrix $A$.

## 1.3 Systems of Equations
**SKIPPED.** Elementary Row Operations

> [!Abstract] DEF. Reduced Row Echelon Form (RREF)
> 1. Leading entries 皆為 1
> 2. Zero rows 在下方
> 3. staircase property
> 4. pivot columns 中除 leading entry 之外皆為 0

若只滿足敘述 2, 3，則為 REF。

註。關於「階梯形」的形式定義
> The leading entry of a nonzero row **lies in a column** to the right of the column containing the leading entry of any preceding row.

每個 leading entry 所在的 column，都在上方（preceding）的 leading entry 的 column 的右邊。

（**特例**）結合下一節所述，可以說若一個 $n\times n$ 的矩陣 rank 為 $n$，則其 RREF 為 $I_{n}$。

## 1.4 Gaussian Elimination
- Pivot Position; Pivot Column

Rank and nullity
一個矩陣的 rank 是在他變為 RREF 之後擁有幾個非零列。 nullity 則相反，算的是該情況下擁有幾個零列。

$$\begin{array}{ccccccc} & & j & & j' & & \\ & & \vdots & & \vdots & & \\ i & \cdots & a_{i,j} & \cdots & a_{i,j'} & \cdots & \\ & & \vdots & & \vdots & & \\ & & \vdots & & \vdots & & \\ i' & \cdots & a_{i',j} & \cdots & a_{i',j'} & & = a_{i',j'} - \dfrac{a_{i',j} \times a_{i,j'}}{a_{i,j}} \\ & & \vdots & & \vdots & & \\ & & & & & & j' = j, j+1, \dots, n+1 \\ \end{array}$$
<center>
<i>
Schematic Diagram of Gaussian Elimination
</i>
</center>


## 1.5 Span of A Set of Vectors - Vector Space
$$
\text{span}(S)
$$
Span 代表的是一個集合的所有可能的線性組合。

或說，
$$
\text{span}(S) := \{ c_{1} s_{1} + c_{2} s_{2} + \dots + c_{n} s_{n} \ | \ c_{1}, c_{2}, \dots, c_{n} \in \mathbb{R} \}.
$$

反過來說，如果對於一個集合 $V$，存在若干 $g_{i}$ 使得
$$
 V = \{ c_{1}g_{1} + c_{2} g_{2} + \dots + c_{n} g_{n} \ | \ c_{1}, c_{2}, \dots, c_{n} \in \mathbb{R} \}\ 
$$
那麼 $G$ 就是 $V$ 的生成集。

## 1.6 Linear Independence
> [!Abstract] DEF. Linear Independence
> 如果對於一組向量 $\{ \mathbf{v}_{1}, \mathbf{v}_{2}, \dots, \mathbf{v}_{n} \}$ 而言，
> $$
> c_{1} \mathbf{v}_{1} + c_{2} \mathbf{v}_{2} + \dots + c_{n} \mathbf{v}_{n} = \mathbf{0}
> $$
> 中的 $c_{1}, c_{2}, \dots, c_{n}$ 的唯一解為全零的話，則稱這組向量線性獨立。否則他們線性相依。

### 線性獨立的等價敘述
1. 矩陣 $A$ 的 columns 是線性獨立的。
2. 對於 $\mathbf{R}^m$ 中的每個 $\mathbf{b}$，方程 $\mathbf{A}\mathbf{x} = \mathbf{b}$ 至多只有一個解。
3. 矩陣 $A$ 的 nullity 為零。
4. 矩陣 $A$ 的 rank 為 $n$，即 $A$ 的 column 數。
5. 矩陣 $A$ 的 RREF 的列是 $\mathbf{R}^m$ 中相異的標準向量。
6. 方程 $\mathbf{A}\mathbf{x} = \mathbf{0}$ 的唯一解是 $\mathbf{0}$。
7. 矩陣 $A$ 的每一列中都有一個 pivot column。
