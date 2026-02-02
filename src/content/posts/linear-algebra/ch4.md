---
title: "Linear Algebra Chapter 4: Subspaces and Their Properties"
published: 2025-11-02
category: linear-algebra
---
[課程總覽](../)
## 4-1 Subspaces
> [!Abstract] DEF. Subspace
> 對於 $\mathbb{R}^{n}$，以下三個性質定義一個子空間 $W$。
> 1. 零向量：$W$ 必有元素 $\mathbf{0}_{n}$。
> 2. 向量加法封閉性。
> 3. 純量乘法封閉性。

THR.
對於所有 $\mathbb{R}^{n}$ 的非空子集合，他們的向量空間都是 $\mathbb{R}^{n}$ 的子空間。
ALT: 對於任意向量集合，若非空，則向量空間必為實數空間的 subspace。
/THR.

> [!Abstract] DEF. Null Space
> 矩陣 $A$ 的 Null space 表示方程式 $A\mathbf{x} =\mathbf{0}$ 中 $\mathbf{x}$ 的解的集合。
> $$
> \text{null}(A) := \{ \mathbf{x} \ | \ A \mathbf{x} = \mathbf{0} \}
> $$

$\text{Null}\ A$ 跟 $\text{null}(A)$ 說的是同一件事。

> [!Abstract] DEF. Column Space
> 一個矩陣的 column space 即為其各 column 之集合的 span。
> $$
> \text{col}(A) := \text{span}(\{ \mathbf{a}_{1}, \mathbf{a_{2}}, \mathbf{a_{3}}, \dots, \mathbf{a}_{n} \})
> $$
> with $A = [\mathbf{a}_{1} \mathbf{a}_{2} \dots \mathbf{a}_{n}]$.

根據以上定義，我們可以得到一些性質。
1. 線性變換的 range 即為其 standard matrix 的 column space。
2. 因此，對於線性變換 $T:\mathbb{R}^{n} \to \mathbb{R}^{m}$，其 range 為 $\mathbb{R}^{m}$ 的子空間。
3. 線性變換的 null space 等於其矩陣的 null space。

## 4.2 Basis
> [!Abstract] DEF. Basis
> 對於 $\mathbb{R}^{n}$ 的子空間 $V$，其 basis 定義為它的「線性獨立的」「生成集合」。

註：以下兩者為等價敘述。
1. $V$ 為 $S$ 的 span
2. $S$ 為 $V$ 的 generating set

舉例：標準向量集合 $\{ \mathbf{e}_{1}, \mathbf{e}_{2}, \dots, \mathbf{e}_{n} \}$ 為實數空間 $\mathbb{R}^{n}$ 的 basis。
1. 線性獨立
2. 生成集合：$\text{span}(\{ \mathbf{e}_{1}, \mathbf{e}_{2}, \dots,  \mathbf{e}_{n} \}) = \mathbb{R}^{n}$

> [!Note] Theorem
pivot columns 集合為其 column space 的 basis。

## 4.4 Coordinate System

> [!Note] THR.
> 對於子空間 $V$ 以及其一基底 $\mathcal{B}$，任何 $V$ 的向量 $\mathbf{v}$ 必可表示為唯一的 $\mathcal{B}$ 的線性組合；即，存在 $a_{1},a_{2},\dots, a_{k}$ 使得
> $$
> \mathbf{v} = a_{1} \mathbf{b}_{1} + a_{2} \mathbf{b}_{2} + \dots + a_{k} \mathbf{b}_{k}.
> $$
> 或寫作
> $$
> \mathbf{v} = B \vec{a}
> $$

SKIPPED. DEF. Coordinate Vector (of $\mathbf{v}$ relative to $\mathcal{B}$)

依照定義，可以得知自然的表示方式即為相對於「標準基底（standard basis）$\mathcal{E}$」的座標向量，即
$$
[\mathbf{v}]_{\mathcal{E} } = \mathbf{v}.
$$

THR. Bases Transformation
設 $B$ 每一行為 $\mathcal{B}$ 的一個向量。則 $B$ 必可逆，且 for every vector $\mathbf{v} \in \mathbb{R}^{n}$,
$$
\mathbf{v} = B[\mathbf{v}]_{\mathcal{B} }.
$$
/THR


![[Screenshot_2025-11-11-10-00-37-516_com.miui.gallery-edit.jpg]]

## 4.5
**Theorem 4.12**
THR. Linear Operation in Different Coordinate Systems
Note: $A$ is the standard matrix of the linear operation $T$
$$
[T]_{\mathcal{B} } = B^{-1} A B
$$
or
$$
A = B[T]_{\mathcal{B} } B^{-1}
$$

