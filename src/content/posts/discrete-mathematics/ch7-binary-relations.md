---
title: 07 Binary Relations
published: 2025-06-06
category: discrete-math
---
[課程總覽](../)
### Cartesian Product
Definition.
Cartesian Product
$$
A \times B:= \{ (a,b) | a \in A, b \in B \}
$$

Proposition.
任何與空集合的笛卡爾積，皆為空集合。

### Binary Relations
Definition.
由A到B的二元關係，定義為其笛卡爾積的子集：
$$
\forall f : A \to B,\ f \in A \times B.
$$

### Properties of Relations
Definition.
1. Reflexive: 存在從a到a
2. Symmetric: 有a到b，則有b到a
3. Antisymmetric: 有a到b，則必沒有b到a（或者a=b）
4. Transitive

### Antisymmetric Property
沒有「雙向道路」，只有「無關（關係不成立）」與「單向道路（關係成立但其反關係不成立）」。
但是自指的道路是被允許的。

舉例：小於等於($\le$)即為antisymmetric relation。
$$
a \le b \land b \le a \implies a = b
$$
舉例：是...的子集也是antisymmetric relation。
$$
A \subseteq B \land B \subseteq A \implies A = B
$$

### Partition
Definition.
Partition $A$ of a set $S$:
$$
A = \{ A_{i} | i \in I \}
$$
- 每一個分割都不為空
- 相異分割毫無交集
- 所有分割聯集為$A$

### Equivalence Relation
Definition.
Equivalence Relation:
- Reflexive, Symmetric, Transitive
- 「等價關係」

Definition.
Equivalence Class to $a$ of $A$
$$
[a] = \{ x \in A | (a,x) \in R \}.
$$
where $R$ is equivalence relation.

Proposition.
對於等價關係$R$，集合$A$，物件$a,b$，以下敘述等價：
1. $aRb$
2. $[a]=[b]$
3. $[a]\cap[b] \ne \emptyset$

Proposition.
Equivalence classes of a set forms a partition of it.

Proposition.
1. 等價到分割：等價關係把元素分組，每組內互相等價，這些分組就是 partition。
2. 分割到等價：ㄍ分割給出「誰屬於同一組」的訊息，而這就足以定義一種「等價性」。

Proposition.
在此$A_{i}$為所有等價類
$$
\forall a \in A,\ a \in A_{i} \implies [a] = A_{i}.
$$
Proof.
- 分割子於等價類
- 等價類子於分割：


### Ordering
Definition.
Partial Order:
- Reflexive, Antisymmetric, Transitive

Definition.
Total Order:
- Partial Order + Every two elements are related

Proposition.
Maximum size of an antichain & minimum number of chains