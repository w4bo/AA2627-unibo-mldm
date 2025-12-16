---
subtitle: Bayesian classifier
---

# Basics

* They are a probabilistic approach to solving classification problems
  * In many applications, the relationship between attribute values and that of the class is not deterministic
    * Noise in data
    * Presence of features of the phenomenon not modeled by the attributes (hidden variables)
    * Difficulty in quantifying certain aspects of the phenomenon
  * For example, predicting whether a person is at heart risk depends heavily on his or her diet and physical activity but, people who have a healthy diet and exercise regularly may still have heart problems
    * There are other factors such as heritability, alcohol abuse
    * It is difficult to say how "healthy" a diet is and whether training is "adequate“
  * All this introduces uncertainty about the outcome of the prediction
* Bayesian classifiers model probabilistic relationships between attributes and the classification attribute


# Recalls of statistics

**Conditional probability**: probability that event c will occur knowing that event a has occurred

- $P(C|A)=\frac{P(A,C)}{P(A)}$
- $P(A|C)=\frac{P(A,C)}{P(C)}$
- $P(A,C)=\frac{P(A|C)}{P(C)}$

**Bayes' theorem**:

- $P(C|A)=\frac{P(A|C)\cdot P(C)}{P(A)}$

**Absolute Probability Theorem**

- $P(A=a)=\sum_{i=1}^n P(A=a, B=b_i)=\sum_{i=1}^n P(A=a, B=b_i)\cdot P(B=b_i)$
- $b_i$ denotes one of the $n$ values that can be taken by $B$


# Bayes Theorem: an example

Let us suppose

* A doctor knows that meningitis causes neck soreness in 50% of cases
* The a priori probability that any patient has meningitis is 1/50,000
* The a priori probability that any patient has neck soreness is 1/20

If a patient reports neck soreness, what is the probability that he or she has meningitis?

$P(M|S)=\frac{P(S|M)\cdot P(M)}{P(S)} = \frac{0.5 \cdot \frac{1}{50000}}{\frac{1}{20}}=2\cdot 10^4=\frac{1}{5000}$

# Bayes Theorem: an example

Let us suppose that in the bachelor degree program, smoking students are 15% while in the master's program 23%. If 1/5 of the total number of students are enrolled in the master's program what is the probability that a student who smokes is enrolled in the master's program?

# Bayesian Classifiers Principle

Let $\boldsymbol{A}=(A_1, A_2,...,A_n)$ be the vector describing the set of attributes, and let $C$ be the class variable.

If $C$ is non-deterministically related to the values taken by $\boldsymbol{A}$ we can treat the two variables as random variables and capture their probabilistic relationships using $P(C|\boldsymbol{A})$

During the training phase we learn the probabilistic ties $P(C|\boldsymbol{A})$ for each combination of values assumed by $\boldsymbol{A}$ and $C$

Knowing these probabilities, a test record a can be classified by finding the label of class $c$ that maximizes the a posteriori probability $P(\boldsymbol{C}=c|A_1=a_1,..,A_n=a_n)$

# Bayesian Classifiers Principle (cont.)

::::{.columns}
:::{.column width=50%}
![Training Data](./img/dt/image1.png)
:::
:::{.column width=50%}
$\boldsymbol{A}=(Refund=Yes, Marital Status=Married, Taxable Income=60K)$

Solving the classifier problem means computing:

$P(Evade=No|\boldsymbol{A})$ and $P(Evade=Yes|\boldsymbol{A})$

* if $P(Evade=No | A) > P(Evade=Yes| A)\rightarrow$ No
* if $P(Evade=Yes| A) > P(Evade=No| A)\rightarrow$ Yes
:::
::::

# Bayesian Classifiers Principle (cont.)

Calculating $P(C|A)$ for every possible value of $C$ and $\boldsymbol{A}$ requires a very large training set even for a small number of attributes

- Bayes' theorem is useful here because it allows the a posteriori probability $P(C|\boldsymbol{A})$ to be expressed in terms of $P(\boldsymbol{A}|C)$, $P(C)$, and $P(\boldsymbol{A})$

$P(C|A_1A_2...A_n)=\frac{P(A_1A_2...A_n|C)\cdot P(C)}{P(A_1A_2...A_n)}$

- Since $P(\boldsymbol{A})$ is constant in this formula, the problem of maximizing the a posteriori probability is equivalent to choosing the value of $C$ that maximizes

$P(A_1A_2...A_n|C)\cdot P(C)$

How to estimate $P(A_1A_2...A_n|C) \rightarrow$ __Naïve Bayes__

# Naïve Bayes

Assume independence between $A_i$ attributes when the class is known (__conditional independence__):

* Given three random variables $X$, $Y$ and $Z$, $X$ is said to be independent of $Y$ given $Z$ if $P(X|Y,Z)=P(X|Z)$
* In other words, if the value taken by $Z$ is known, knowing the value of $Y$ does not affect the value taken by $X$

Due to stochastic independence we can write:

$P(X,Y|Z)=\frac{P(X,Y,Z)}{P(Z)}=\frac{P(X,Y,Z)}{P(Y,Z)} \cdot=\frac{P(Y,Z)}{P(Z)}=P(X|Y,Z)\cdot P(Y|Z)=P(X|Z) \cdot P(Y|Z)$

# Naïve Bayes (cont.)

The assumption of independence between attributes $A_i$ when class $C$ is known allows rewriting:

$P(A_1, A_2, ..., A_n |C) = P(A_1| C) \cdot P(A_2| C) \cdot ...\cdot  P(A_n| C)$

Instead of having to calculate the conditional probability for each combination of values of $\boldsymbol{A}$, it is sufficient to calculate $P(A_k| C)$ for each $A_k$ and $C=c_j$.

The new point is classified as $C=c_{j*}$ if:

$j*=argmax_j P(C=c_j) = \Pi_{k=1}^n P(A_k=a_k|C=c_j)$

# Exercise

::::{.columns}
:::{.column width=50%}
Compute the conditional probabilities

* $P(A=1|+)$
* $P(B=1|+)$
* $P(C=1|+)$
* $P(A=1|-)$
* $P(B=1|-)$
* $P(C=1|-)$

Forecast the class value for the record $R=(A=1,B=1,C=1)$
:::
:::{.column width=50%}

| ID | A | B | C | Class |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | 0 | 1 | - |
| 2 | 1 | 0 | 1 | + |
| 3 | 0 | 1 | 0 | - |
| 4 | 1 | 0 | 0 | - |
| 5 | 1 | 0 | 1 | + |
| 6 | 0 | 0 | 1 | + |
| 7 | 1 | 1 | 0 | - |
| 8 | 0 | 0 | 0 | - |
| 9 | 0 | 1 | 0 | + |
| 10 | 1 | 1 | 1 | + |

:::
::::

# Exercise

::::{.columns}
:::{.column width=50%}
Compute the conditional probabilities

* $P(A=1|+) = 3/5 = 0.6$
* $P(B=1|+) = 2/5 = 0.4$
* $P(C=1|+) = 4/5 = 0.8$
* $P(A=1|-)$
* $P(B=1|-)$
* $P(C=1|-)$

:::
:::{.column width=50%}

| ID | A | B | C | Class |
| :-: | :-: | :-: | :-: | :-: |
| _1_ | 0 | 0 | 1 | - |
| 2 | 1 | 0 | 1 | + |
| _3_ | 0 | 1 | 0 | - |
| _4_ | 1 | 0 | 0 | - |
| 5 | 1 | 0 | 1 | + |
| 6 | 0 | 0 | 1 | + |
| _7_ | 1 | 1 | 0 | - |
| _8_ | 0 | 0 | 0 | - |
| 9 | 0 | 1 | 0 | + |
| 10 | 1 | 1 | 1 | + |

:::
::::

# Exercise (cont.)

::::{.columns}
:::{.column width=50%}
Compute the conditional probabilities

* $P(A=1|+) = 3/5 = 0.6$
* $P(B=1|+) = 2/5 = 0.4$
* $P(C=1|+) = 4/5 = 0.8$
* $P(A=1|-) = 2/5 = 0.4$
* $P(B=1|-) = 2/5 = 0.4$
* $P(C=1|-) = 1/5 = 0.2$

:::
:::{.column width=50%}

| ID | A | B | C | Class |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | 0 | 1 | - |
| _2_ | 1 | 0 | 1 | + |
| 3 | 0 | 1 | 0 | - |
| 4 | 1 | 0 | 0 | - |
| _5_ | 1 | 0 | 1 | + |
| _6_ | 0 | 0 | 1 | + |
| 7 | 1 | 1 | 0 | - |
| 8 | 0 | 0 | 0 | - |
| _9_ | 0 | 1 | 0 | + |
| _10_ | 1 | 1 | 1 | + |

:::

# Exercise (cont.)

::::{.columns}
:::{.column width=50%}

Forecast the class value for the record $R=(A=1,B=1,C=1)$

* $P(+|R) = P(A = 1|+) \cdot P(B = 1|+) \cdot P(C = 1|+) = 0.192$
* $P(-|R) = P(A = 1|−) \cdot P(B = 1|−) \cdot P(C = 1|−) = 0.032$

Since P(+|R) is larger, the record is assigned to (+) class

:::
:::{.column width=50%}

| ID | A | B | C | Class |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | 0 | 1 | - |
| 2 | 1 | 0 | 1 | + |
| 3 | 0 | 1 | 0 | - |
| 4 | 1 | 0 | 0 | - |
| 5 | 1 | 0 | 1 | + |
| 6 | 0 | 0 | 1 | + |
| 7 | 1 | 1 | 0 | - |
| 8 | 0 | 0 | 0 | - |
| 9 | 0 | 1 | 0 | + |
| 10 | 1 | 1 | 1 | + |

:::
::::
