---
title: 03 Mathematical Induction
published: 2025-04-07
category: 大學修課
tags:
  - discrete-math
---
[課程總覽](../)
# Euclidean Algorithm
## Basic Recurrence
$$
\text{gcd}(a,b) = \left\{\begin{aligned}
 & b & \text{if }r = 0 \\
 & a & \text{otherwise}
\end{aligned}\right.\ \ \ \text{where } a = b\cdot k + r, 0\le r < b
$$
with an arbitary $k$.
證明：${\text{gcd}(a,b) = \text{gcd}(b,r)}$.
> 可以將問題拆解為「兩式互相小於等於對方」的兩個小命題，來簡化證明難度。

命題一，${\text{gcd}(a,b) \le \text{gcd}(b,r)}$.
- Let ${d \in \text{common divisor}(a,b)}$.
- ${\implies a = k_{1}d \land b = k_{2}d}$, ${\exists k_{1}, k_{2} \in \mathbb{Z}}$.
- ${a = bk + r \implies r = (k_{1} - kk_{2})d}$ ${\implies d | r}$.
- ${\implies \forall d' \in \text{common divisor(a,b)} \implies d' | r}$.
	- Every common divisor of $a$ and $b$ is a divisor of $r$, which surely contains ${\text{gcd}(a,b)}$.
（略命題二。）故得證 $\blacksquare$

## Estimating Steps Needed in Euclidean Algorithm
Let ${r_{0}  = a}$, ${r_{1} = b}$; ${r_{0} \ge r_{1}}$.
$$
\begin{array}. 
r_{0} = r_{1}k_{1} + r_{2} \\
r_{1} = r_{2}k_{2} + r_{3} \\
r_{2} = r_{3}k_{3} + r_{4} \\
\dots \\
r_{n - 1} = r_{n}k_{n} + 0
\end{array}
$$
我們想知道這個遞迴式共花了多少步完成。或者說，我們想求 $n$ 的值。
在以上描述輾轉相除法的遞迴關係式中，我們可以觀察到 ${r_{i} \ge r_{i + 1} + r_{i + 2}}$，比如 ${r_{0} \ge r_{1} + r_{2}}$等。這之中還輕易地得到 ${r_{i} \ge r_{i + 1}}$，因此可以說：
$$
r_{n} \ge 2\cdot r_{n + 2},
$$
或者 ${r_{n + 2} \le \frac{1}{2}r_{n}}$。平均來說，也可說 $r_{n + 1} \le \frac{1}{2^{ 1/ 2}}r_{n}$。試著將這個新的遞迴不等式串起來：
$$
r_{n} \le \frac{1}{2^{1/2}} r_{n - 1} \le \frac{1}{2^{2 / 2}} r_{n - 2} \le \dots \le \frac{1}{2^{n / 2}}r_{0} ,
$$
而我們可以單獨將頭尾抽出來看，得一*指數遞減關係*：
$$
r_{n} \le \frac{r_{0}}{2^{n/2}}.
$$
設想一數 $x$，使得
$$
\frac{r_{0}}{2^{x/2}} < 1
$$
成立。那麼，考慮原本的遞減關係，當 $n$ 等於 $x$ 時，遞減關係必然成立：
$$
r_{x} \le \frac{r_{0}}{2^{x/2}} < 1,
$$
故若一數 $x$ 符合不等式 ${\frac{r_{0}}{2^{x/2}} < 1}$，則 $x$ 可作為 $n$ 之上界：
$$
n \le x = 2\log r_{0} + 1.\ \blacksquare
$$
> 可以說，找到的 $x$ 是一個保守解，這也是他作為「$n$ 的上界」的含意。
# Mathematical Induction
## Well-ordering Axiom
Let $S$ be a set with some positive integers. Then if
$$
\left\{\begin{aligned}
 & 1 \in S \\
 & \forall n \in \mathbb{N},\ n \in S \implies n + 1 \in S
\end{aligned}\right.\ ,
$$
then $S$ is the set of all positive integers, namely $\mathbb{N}$.
在這個公理之中便使用了數學歸納的概念。

## Weak Mathematical Induction
若要證明一個初階邏輯式$P(n)$對於所有$n \ge x$皆成立，則：
$$
P(x) = \text{true} \land \forall k > x,\ P(k) \implies P(k + 1)
$$

## Strong Mathematical Induction
$$
P(x) = \text{true} \land \forall k > x,\ P(x) \land P(x + 1) \land \dots \land P(k) \implies P(k + 1)
$$

## Lame's Theorem


# Generating function
## Infinite Sum vs. Closed Form
1. Infinite sum: ${1 + x + x^{2} + \dots + x^{n} + \dots}$
2. Closed form: $\frac{1}{1 - x}$

---

例：自然數數列 $1,2,3,4,5,\dots$

列出生成函數 $A(x)= 1 + 2x + 3x^{2} + 4x^{3} + \dots$
**法一**，轉換為一連串的closed form：
$$
\begin{aligned}
= 1 + x + x^{2} + x^{3} + \dots &  \left( \frac{1}{1-x} \right)\\
+ x + x^{2} + x^{3} + \dots &  \left( \frac{x}{1 - x} \right)\\
+x^{2} + x^{3} + \dots &  \left( \frac{x^{2}}{1 - x} \right) \\
+\dots.\ \square
\end{aligned}
$$
**法二**，兩邊微分：
$$
\begin{aligned}
 & (1 + x + x^{2} + x^{3} + x^{4}+ \dots)' \\
 = & 1 + 2x + 3x^{2} + 4x^{3}+ \dots;
\end{aligned}
$$
另一邊：
$$
\left( \frac{1}{1 - x} \right)' = \frac{1}{(1 - x)^{2}}.\ \square
$$

## Solving Linear Recurrence by Generating Function
數列 $\{ a_{n} \}$ 之生成函數乃其Formal power series:
$$
\sum ^{n}_{i=0} a_{i} x^{i} = a_{0} + a_{1}x + a_{2}x^{2} + \dots + a_{n}x^{n} + \dots
$$

---

例：給予一數列之遞迴關係 ${a_{n} = 8 a_{n - 1} + 10^{n}, a_{0} = 6}$，求數列之一般式。

推導：
$$
\begin{aligned}
A(x) & = a_{0} + a_{1}x + \dots \\
 & = a_{0} + \sum ^{\infty}_{i = 1} (8a_{i - 1} + 10^{i}) x_{i} \\
 & = a_{0} + 8\sum ^{\infty}_{i = 1} a_{i-1} x^{i} + \sum ^{\infty}_{i = 1} 10^{i}x^{i} .\\
\end{aligned}
$$
前式的 $a_{i-1}x^{i}$ 可以寫為 ${x\cdot a_{i-1}x^{i-1}}$，可提出 $x$；後式的 $10^{i}x^{i}$ 則可寫為 ${(10x)^{i}}$，而變成無窮等比級數：
$$
\begin{aligned}
A(x) & = \dots \\
 & = 6 + 8xA(x) + \frac{10x}{1 - 10x}.
\end{aligned}
$$
等式兩邊消除了所有的無窮級數，而兩邊都有 $A(x)$。只消移項整理即可得 $A(x)$：
$$
\begin{aligned}
 & (1 - 8x) A(x) = 6 + \frac{10x}{1 -10x}, \\
 & A(x) = \frac{6 - 50x}{(1 - 8x)(1 - 10x)} \underset{\text{(1)}}{=} \frac{1}{1-8x} + \frac{5}{1 - 10x}.
\end{aligned}
$$
接著，即可依照closed form來將其還原為一般項，
$$
\frac{1}{1 - 8x} = 1 + 8x + (8x)^{2} + \dots,
$$
$$
\frac{5}{1 - 10x} = 5 + 5\cdot 10x + 5\cdot (10x)^{2} + \dots
$$
而分別可以還原回一般式 ${8^{n}}$ 與 $5\cdot 10^{n}$。因此，便可以得一般項 ${a_{n} = 8^{n} +5\cdot 10^{n}}$。$\blacksquare$

**重點**
1. 在推導時重複出現原式，可以移項整理，消去麻煩的式子
2. $x$的一次分式是很有價值的。有他就可以構成無窮等比(closed form)。因此遇到可以拆分的二次分式（形如$\frac{1}{()()}$）的話要多留意一下。
## Manipulating Generating Function
給兩個生成函式 ${A(x), B(x)}$ 分別對應到數列 $a_{0}, a_{1}, a_{2}, \dots, a_{n}$ 跟 ${b_{0}, b_{1}, b_{2}, \dots, b_{n}}$。
一、乘以 $x$ 會達成「位移」(shifting)的效果：
$$
xA(x) \leftrightarrow  0, a_{0}, a_{1}, \dots, a_{n-1}, \dots
$$
二、生成函式的加法：
$$
A(x) + B(x) \leftrightarrow  a_{0} + b_{0},\ a_{1} + b_{1},\ a_{2} + b_{2}, \dots
$$
三、生成函數的乘法：
$$
A(x)\cdot B(x) \leftrightarrow  a_{0}b_{0},\ a_{0} b_{1} + a_{1}b_{0},\ a_{0}b_{2} + a_{1}b_{1} + a_{2}b_{0}, \dots
$$
我們可以說，兩個生成函數相乘，即得他們對應數列（此處為 ${\{ a_{n} \}}$ 與 ${\{ b_{n} \}}$）的**卷積(convolution)**。
提示：${A(x)\cdot B(x) = (a_{0} + a_{1}x + a_{2}x^{2} + \dots)(b_{0} + b_{1}x + b_{2}x^{2} + \dots)}$

---

例：計算費氏數列 ${f_{n} = f_{n - 1} + f_{n - 2}; f_{0} = 0, f_{1} = 1}$的一般項。

$$
\begin{aligned}
F(x) & = \sum ^{\infty}_{i = 0} f_{i}x^{i} \\
 & = f_{0} + f_{1} x + \sum ^{\infty}_{i = 2} f_{i} x^{i} \\
 & = x + \sum ^{\infty}_{i = 2} (f_{i - 1} + f_{i - 2})x^{i} \\
 & = x + \sum ^{\infty}_{i = 2}f_{i - 1} x^{i} + \sum ^{\infty}_{i = 2}f_{i - 2} x^{i} \\
 & = x + x \sum ^{\infty} _{i=2}f_{i - 1}x^{i - 1} + x^{2} \sum ^{\infty}_{i = 2}f_{i - 2} x^{i - 2}
\end{aligned}
$$
此時，兩個無窮級數事實上都可以轉換為生成函數 $F(x)$。
- 前式：${\sum ^{\infty}_{i = 2}f_{i - 1}x^{i - 1} = \sum ^{\infty}_{i  = 1} f_{i}x^{i} = F(x) - f_{0} = F(x)}$；
- 後式：${\sum ^{\infty}_{i = 2}f_{i - 2}x^{i - 2} = \sum ^{\infty}_{i = 0}f_{i}x^{i} = F(x)}$。
$$
\begin{aligned}
F(x) & = \dots \\
 & = x + xF(x) + x^{2} F(x)
\end{aligned}
$$
移項之後得 ${F(x) = \frac{x}{1 - x-x^{2}} = \frac{-x}{x^{2} + x - 1}}$，有兩個方法可解。

法一，用公式法分解二次式，然後再拆解分式：
$$
F(x) = \frac{-x}{\left( x - \frac{-1 + \sqrt{ 5 }}{2} \right)\left( x - \frac{-1 - \sqrt{ 5 }}{2} \right)} = \frac{c_{1}}{x + \frac{1 - \sqrt{ 5 }}{2}} + \frac{c_{2}}{x + \frac{1 + \sqrt{ 5 }}{2}}.\ \square
$$

法二，將式子拆解為兩個乘法項，前後個別求一般式，然後解卷積：
$$
F(x) = \frac{-x}{\left( x - \frac{-1 + \sqrt{ 5 }}{2} \right)\left( x - \frac{-1 - \sqrt{ 5 }}{2} \right)} =\frac{-x}{x - \frac{-1 + \sqrt{ 5 }}{2}} \cdot \frac{1}{x + \frac{1 + \sqrt{ 5 }}{2}} = \frac{\frac{2}{-1 + \sqrt{ 5 }}x}{1 - \frac{2}{-1 + \sqrt{ 5 }}x}\cdot \frac{1}{1 + \frac{2}{1 + \sqrt{ 5 }}x}.
$$
而這個方法比起法一來說更加麻煩。$\square$