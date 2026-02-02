---
title: "Linear Algebra Chapter 5: Eigenvalues, Eigenvectors, and Diagonalization"
published: 2025-12-03
category: linear-algebra
---
[課程總覽](../)
## Eigenvector
線性運算的特徵向量 / eigenvalue of a linear operation
$$
T(\mathbf{v}) = \lambda \mathbf{v}
$$
矩陣的特徵向量 / eigenvalue of a matrix
$$
A\mathbf{v} = \lambda \mathbf{v}
$$
## Eigenvalue
The **characteristic polynomial** is defined as below.
- $f(t) = a_n t^n + a_{n-1}t^{n-1} + \dots + a_1t + a_0 I_n$
- $f(t) = \det(A-tI_{n})$

Eigenvalues must satisfy the following equation of $t$ (**characteristic equation**):
$$
f(t) = 0
$$

## Multiplicity
Multiplicity of $\lambda$: the maximum $k$ for the term $(t-\lambda)^{k}$ in the characteristic polynomial.

**Theorem**. The dimension of the eigenspace must not be greater than its multiplicity.

## Diagonalizable
A matrix $A$ is called diagonalizable if there exists 
- a diagonal matrix $D$
- an invertible $P$
such that
$$
A = PDP^{-1}.
$$

**Corollary**.
$$
A^{m} = PD^{m}P^{-1}.
$$

## Propositions about Diagonalization
- The set of column vectors of $P$ is a basis of $\mathbb{R}^{n}$.
- The set of column vectors of $P$ consists of eigenvectors of $A$.
- Entries of $D$ consists of eigenvalues corresponding to column vectors of $P$. 

**Theorem**. For any two eigenvectors, if their corresponding eigenvalues are distinct, they are linearly independent.

## Diagonalizability
1. The number of eigenvalues, taking multiplicity into consideration, is equal to the dimension.
2. Dimension of eigenspace = multiplicity

**Theorem**. 
- Linear operation $T$ is diagonalizable
if and only if
- there exists a basis $\mathcal{B}$ such that $[T]_{\mathcal{B}}$ is diagonal.

Note: $[T]_{\mathcal{B}}=B^{-1}AB$.