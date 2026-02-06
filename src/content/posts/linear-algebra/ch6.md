---
title: "Linear Algebra Chapter 6: Orthogonality"
published: 2025-12-14
category: 大學修課
tags:
  - linear-algebra
---
[課程總覽](../)
## 6.1 Geometry of Vectors
### 6.1.1 Distances
**DEF. norm**
$$
\lVert \mathbf{v} \rVert  = \sqrt{ {v_{1}}^{2} + {v_{2}}^{2} + \dots + {v_{k}}^{2} }
$$

**DEF. distance**
$$
\text{distance of } \mathbf{u}, \mathbf{v} = \lVert \mathbf{u} - \mathbf{v} \rVert
$$
---

### 6.1.2 Dot Product
**DEF. dot product**
$$
\mathbf{u} \cdot \mathbf{v} = u_{1} v_{1} + u_{2} v_{2} + \dots + u_{k} v_{k}
$$

**Matrix represntation of dot product**
$$
\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^{T} \mathbf{v}
$$


**THR.** basic properties of dot product operation of vectors

For all vectors $\mathbf{u}$ and $\mathbf{v}$, and $\mathbf{w}$ in $\mathbb{R}^{n}$ and every scalar $c$,
1. $\mathbf{u} \cdot \mathbf{u} = \lVert \mathbf{u} \rVert^{2}$
2. $\mathbf{u}\cdot \mathbf{u}=0$ if and only if $\mathbf{u}=\mathbf{0}$
3. $\mathbf{u}\cdot \mathbf{v}=\mathbf{v}\cdot \mathbf{u}$
4. $\mathbf{u}\cdot(\mathbf{v} + \mathbf{w}) =\mathbf{u}\cdot \mathbf{v}+\mathbf{u}\cdot \mathbf{w}$
5. $(\mathbf{v}+\mathbf{w})\cdot \mathbf{u}=\mathbf{v}\cdot \mathbf{u}+\mathbf{w}\cdot \mathbf{u}$
6. $(c\mathbf{u})\cdot \mathbf{v}=c(\mathbf{u}\cdot \mathbf{v})=\mathbf{u}\cdot(c\mathbf{v})$
7. $\lVert c\mathbf{u} \rVert=\left| c \right|\ \lVert \mathbf{u} \rVert$

Note: (3) shows commutative property of dot product; (4), (5) together show that dot product distributes over addition.

**THR.** Pythagorean Theorem in $\mathbb{R}^{n}$

Let $\mathbf{u}$ and $\mathbf{v}$ be vectors in $\mathbb{R}^{n}$.
Then $\mathbf{u}$ and $\mathbf{v}$ are **orthogonal** if and only if
$$
\lVert \mathbf{u} + \mathbf{v} \rVert ^{2} = \lVert \mathbf{u} \rVert ^{2} + \lVert \mathbf{v} \rVert ^{2}
$$

---

### Orthogonal Projection of a Vector on a Line
**DEF. orthogonal projection**

The orthogonal projection from $P(\mathbf{u})$ to $\mathcal{L}(\mathbf{v})$ is given by
$$
\mathbf{w} = \left( \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert ^{2}} \right)\mathbf{v}
$$

**DEF. distance from a point to a line**
$$
\text{distance from } P(\mathbf{u}) \text{ to } \mathcal{L} (\mathbf{v})  = \lVert \mathbf{u} - \mathbf{w} \rVert
$$

---

### 6.1.4 Cauchy-Schwarz and Triangle Inequalities
**THR.** Cauchy-Schwarz Inequality

For any vectors $\mathbf{u}$ and $\mathbf{v}$ in $\mathbb{R}^{n}$,
$$
\left| \mathbf{u} \cdot \mathbf{v} \right|  \le \lVert \mathbf{u} \rVert  \lVert \mathbf{v} \rVert .
$$

## 6.2 Orthogonal Vectors
**DEF. orthogonal set**

- every pair of distinct vectors in the set is orthogonal

**DEF. orthonormal set**

- the set is an orthogonal one consisting entirely of unit vectors

**THR.**

- Any orthogonal set of nonzero vectors is linearly independent.

**DEF. orthogonal basis**

- an orthogonal set that is also a basis for a subspace of $\mathbb{R}^{n}$

is called ~ for the subspace.

**DEF. orthonormal basis**

- an orthonormal set that is also a basis

**THR.** representation of a vector in terms of an orthogonal (or orthonormal) basis
- Let $\{ \mathbf{v}_{1}, \mathbf{v}_{2}, \dots, \mathbf{v}_{k} \}$ be an orthogonal basis for a subspace $V$ of $\mathbb{R}^{n}$.
- Let $\mathbf{u}$ be a vector in $V$.

Then
$$
\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}_{1}}{\lVert \mathbf{v}_{1} \rVert ^{2}} \mathbf{v}_{1} + \frac{\mathbf{u}\cdot \mathbf{v}_{2}}{\lVert \mathbf{v}_{2} \rVert ^{2}} \mathbf{v}_{2} + \dots +  \frac{\mathbf{u}\cdot \mathbf{v}_{k}}{\lVert \mathbf{v}_{k} \rVert ^{2}}\mathbf{v}_{k}
$$

Furthermore, if the orthogonal basis is an orthonormal basis for $V$, then
$$
\mathbf{u} = (\mathbf{u} \cdot \mathbf{v}_{1}) \mathbf{v}_{1} + (\mathbf{u} \cdot \mathbf{v}_{2}) \mathbf{v}_{2} + \dots + (\mathbf{u} \cdot \mathbf{v}_{k}) \mathbf{v}_{k}
$$

 **THR.**
 
 Every subspace of $\mathbb{R}^{n}$ has an orthogonal, and hence an orthogonal, basis.

---

**DEF. The Gram-Schmidt Process**

The process converts a basis to the orthogonal basis for the same subspace of $\mathbb{R}^{n}$.
- input: basis $S=\{ \mathbf{u}_{1},\mathbf{u}_{2},\dots,\mathbf{u}_{k} \}$
- output: orthogonal basis $S'=\{ \mathbf{v}_{1} , \mathbf{v}_{2},\dots,\mathbf{v}_{k}\}$

$$
\begin{aligned}
& \mathbf{v}_{1} = \mathbf{u}_{1}\\
& \mathbf{v}_{2} = \mathbf{u}_{2} - \frac{\mathbf{u}_{2} \cdot \mathbf{v}_{1}}{\lVert \mathbf{v}_{1} \rVert ^{2}} \mathbf{v_{1} }\\
& \mathbf{v}_{3} = \mathbf{u}_{3} - \frac{\mathbf{u}_{3}  \cdot \mathbf{v}_{1}}{\lVert \mathbf{v}_{1} \rVert ^{2}} \mathbf{v}_{1} - \frac{\mathbf{u}_{3} \cdot \mathbf{v}_{2}}{\lVert \mathbf{v}_{2} \rVert ^{2}} \mathbf{v}_{2}\\
& \vdots\\
&
\mathbf{v}_{k} = \mathbf{u}_{k} - \frac{\mathbf{u}_{k} \cdot \mathbf{v}_{1}}{\lVert \mathbf{v}_{1} \rVert ^{2}}\mathbf{v_{1}} - \frac{ \mathbf{u}_{k} \cdot \mathbf{v}_{2}}{\lVert \mathbf{v}_{2} \rVert ^{2}} \mathbf{v}_{2} - \dots - \frac{\mathbf{u}_{k} \cdot \mathbf{v}_{k - 1}}{\lVert \mathbf{v}_{k - 1} \rVert ^{2}} \mathbf{v}_{k - 1} 
\end{aligned}
$$

**THR.**

- Let $\{ \mathbf{u}_{1},\mathbf{u}_{2},\dots,\mathbf{u}_{k} \}$ be a basis for a subspace $W$ for $\mathbb{R}^{n}$.

Then the output of the Gram-Schmidt Process $\{ \mathbf{v}_{1},\mathbf{v}_{2},\dots,\mathbf{v}_{k} \}$ is an orthogonal set of nonzero vectors such that
$$
\text{span}\{ \mathbf{v}_{1},\mathbf{v}_{2},\dots,\mathbf{v}_{i} \} = \text{span}\{ \mathbf{u}_{1},\mathbf{u}_{2},\dots,\mathbf{u}_{i} \}
$$
for each $1\le i\le k$.
So $\{ \mathbf{v}_{1},\mathbf{v}_{2},\dots,\mathbf{v}_{k} \}$ is an orthogonal basis for $W$.

**DEF. the QR factorization of a matrix**

## 6.3 Orthogonal Projections
**DEF. orthogonal complement**

The orthogonal complement of a nonempty subset $\mathcal{S}$ of $\mathbb{R}^{n}$, denoted by $\mathcal{S}^{\perp}$, is the set of all vectors in $\mathbb{R}^{n}$ that are orthogonal to every vector in $\mathcal{S}$.
That is,
$$
\mathcal{S}^{\perp} = \{ \mathbf{v} \in \mathbb{R}^{n} \ |\ \mathbf{v} \cdot \mathbf{u} = 0 \ \forall \mathbf{u} \in \mathcal{S}  \}
$$

**THR.** orthogonal complement = subspace

The orthogonal complement of any nonempty subset of $\mathbb{R}^{n}$ is a subspace of $\mathbb{R}^{n}$.

**THR.** complement = complement of span

For any nonempty subset $\mathcal{S}$ of $\mathbb{R}^{n}$, we have
$$
\mathcal{S} ^{\perp} = (\text{span}(\mathcal{S} ))^{\perp}.
$$
In particular, the orthogonal complement **of a basis** for a subspace is the same as the orthogonal complement of the subspace.

**THR.** complement of row = null space

For any matrix $A$, the orthogonal complement of the row space of $A$ is the null space of $A$; that is,
$$
\text{row}(A)^{\perp} = \text{null}(A).
$$

- **COR.** $\text{col}(A)^{\perp} =\text{row}(A^{T})^{\perp}=\text{null}(A^{T})$

**THR.** orthogonal decomposition theorem

Let $W$ be a subspace of $\mathbb{R}^{n}$.
Then, for any vector $\mathbf{u}$ in $\mathbb{R}^{n}$, there exist unique vectors $\mathbf{w}$ in $W$ and $\mathbf{z}$ in $W^{\perp}$ such that
$$
\mathbf{u} = \mathbf{w} + \mathbf{z}.
$$
In addition, if $\{ \mathbf{v}_{1}, \mathbf{v}_{2},\dots,\mathbf{v}_{k} \}$ is an orthonormal basis for $W$, then
$$
\mathbf{w} = (\mathbf{u}\cdot \mathbf{v}_{1}) \mathbf{v_{1}} + (\mathbf{u}\cdot \mathbf{v}_{2}) \mathbf{v}_{2} + \dots + (\mathbf{u}\cdot \mathbf{v}_{k})\mathbf{v}_{k}.
$$

**THR.**

For any subspace $W$ of $\mathbb{R}^{n}$,
$$
\text{dim}(W) + \text{dim}(W^{\perp}) = n.
$$

---

**DEF. orthogonal projection**

Let $W$ be a subspace of $\mathbb{R}^n$ and $\mathbf{u}$ be a vector in $\mathbb{R}^n$. The orthogonal projection of $\mathbf{u}$ on $W$ is the unique vector $\mathbf{w}$ in $W$ such that $\mathbf{u} - \mathbf{w}$ is in $W^\perp$.

Furthermore, the function $U_W: \mathbb{R}^n \rightarrow \mathbb{R}^n$ such that $U_W(\mathbf{u})$ is the orthogonal projection of $\mathbf{u}$ on $W$ for every $\mathbf{u}$ in $\mathbb{R}^n$ is called the orthogonal projection operator on $W$.

**THR.**

For any subspace $W$ of $\mathbb{R}^{n}$, the orthogonal projection $U_{W}$ is linear.

**DEF. orthogonal projection matrix**

The standard matrix of an orthogonal projection operator $U_{W}$ on a subspace $W$ of $\mathbb{R}^{n}$ is called the orthogonal projection matri for $W$ and is denoted
$$
P_{W}.
$$

**LEM.** linear independence => invertibility

Let $C$ be a matrix whose columns $\text{cols}(C)$ are linearly independent.
Then 
$$
C^{T}C
$$
is invertible.

**THR.** a way to obtain orthogonal projection matrix

Let $C$ be an $n\times k$ matrix whose columns form a basis for a subspace $W$ of $\mathbb{R}^{n}$.
Then
$$
P_{W} = C(C^{T}C) ^{-1} C^{T}.
$$

**DEF.**

The distance from a vector $\mathbf{u}$ in $\mathbb{R}^{n}$ to a subspace $W$ of $\mathbb{R}^{n}$ to be the distance between $\mathbf{u}$ and the orthogonal projection of $\mathbf{u}$ on $W$.

**THR.** closest vector property

Let $W$ be a subspace of $\mathbb{R}^{n}$ and $\mathbf{u}$ be a vector in $\mathbb{R}^{n}$. Among all vectors in $W$, the vector closest to $\mathbf{u}$ is the orthogonal projection $U_{W}(\mathbf{u})$ of $\mathbf{u}$ on $W$.

## 6.4 Least-Squares Approximations and Orthogonal Projection Matrices
### Least-Squares Approximations
$$
\mathbf{v}_{1} = \begin{bmatrix}
1 \\
1 \\
\vdots  \\
1
\end{bmatrix}, \ \mathbf{v}_{2} = \begin{bmatrix}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{bmatrix}, \ \mathbf{y} = \begin{bmatrix}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{bmatrix}, \ C = [\mathbf{v}_{1} \ \mathbf{v}_{2}]
$$


Error sum of squares
(naturally)
$$
E = [y_{1} - (a_{0} + a_{1} x_{1} ]^{2} + [y_{2} - (a_{0} + a_{1} x_{2})]^{2} + \dots + [y_{n} - (a_{0} + a_{1} x_{n})]^{2}
$$

(in terms of vectors)
$$
E = \lVert \mathbf{y} - (a_{0} \mathbf{v}_{1} + a_{1} \mathbf{v}_{2}) \rVert ^{2}
$$

Then note that
$$
\sqrt{ E } = \text{dist}(\mathbf{y}, a_{0} \mathbf{v}_{1} + a_{1} \mathbf{v}_{2})
$$
So we need to make
$$
\mathbf{w} = a_{0} \mathbf{v}_{1} + a_{1} \mathbf{v}_{2}
$$
as close to $\mathbf{y}$ as possible.

And note that
$$
\mathbf{w} \in W = \text{span}\{ \mathbf{v}_{1}, \mathbf{v}_{2} \}
$$
Then the closest $\mathbf{w}$ to $\mathbf{y}$ is the orthogonal projection of $\mathbf{y}$ onto $W$.

Note that the columns of $C$ form a basis for $W$.
Then
$$
\begin{aligned}
P_{W} \mathbf{y} &  = C(C^{T} C^{-1}) C^{T} \mathbf{y} \\
 & = \mathbf{w} = a_{0} \mathbf{v}_{1} + a_{1} \mathbf{v}_{2} = C\begin{bmatrix}
a_{0} \\
a_{1}
\end{bmatrix}
\end{aligned}
$$
$$
C\begin{bmatrix}
a_{0} \\
a_{1}
\end{bmatrix} = C(C^{T} C)^{-1} C^{T} \mathbf{y}
$$
and then
$$
C^{T}C \begin{bmatrix}
a_{0} \\
a_{1}
\end{bmatrix} = C^{T}C(C^{T}C)^{-1} C^{T}\mathbf{y} = C^{T} \mathbf{y}
$$
(normal equations)

And since columns of $C$ are linearly independent, $C^{T}C$ is invertible. (**LEM.** linear independence => invertibility)

Then
$$
\begin{bmatrix}
a_{0} \\
a_{1}
\end{bmatrix} = (C^{T} C ) C^{T} \mathbf{y}.
$$

### Inconsistent Systems of Linear Equations
A possibly inconsistent equation
$$
A\mathbf{x} = \mathbf{b}
$$

We try to obtain $\mathbf{z}$ where
$$
\lVert A\mathbf{z} - \mathbf{b} \rVert
$$
is a minimum.

Define $W$:
$$
W : = \{ A\mathbf{u} \}
$$
Then $W$ is the column space of $A$.

The vector in $W$ that is closest to $\mathbf{b}$ is the orthogonal projection of $\mathbf{b}$ onto $W$. (**THR.** closest vector property)

Then the vector $\mathbf{z}$ minimizes $\lVert A\mathbf{z} - \mathbf{b} \rVert$ if and only if $\mathbf{z}$ is a solution of
$$
A\mathbf{x} = P_{W} \mathbf{b} .
$$


### Solutions of Least Norm
