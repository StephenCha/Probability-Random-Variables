# Relationships-between-probability-variables

Random variables are associated with each other. An example of a binary event was created and the Probability Mass Function of Bernoulli Random Variable was defined. Using the example defined earlier, I implemented a simulation program that evolved into four different RVs.

## Requirements

* Python 3
* matplotlib
* numpy
* math
* sympy

## Try Code!
``` zsh
# In zsh (your terminal)
python Random_Varables.py
```  

## Results
### Bernoulli Distribution Stem Plot

![1](https://user-images.githubusercontent.com/17807597/117300702-c78a2d80-aeb4-11eb-8520-04c6e9828163.png)

If the probability is 0.35, then the sample space S becomes S = {0, 1}

### Binomial Random Variable

#### Formula

$$
\textbf{Binomial PMF} = \binom{n}{k} p^k (1-p)^{n-k}
$$

#### Simulation

![2](https://user-images.githubusercontent.com/17807597/117301704-de7d4f80-aeb5-11eb-89cb-7ddd4bb161cc.png)

### Geometric Random Variable

#### Formula

$$
p_k = p (1-p)^k, \quad k = 0, 1, 2, \cdots
$$

#### Simulation

![3](https://user-images.githubusercontent.com/17807597/117302159-4b90e500-aeb6-11eb-9cca-3e1379fc2999.png)

### Poisson Random Variable

#### Formula

$$
P[N=k] = p_N(k) = {\alpha^k \over k!}e^{- \alpha}
$$

#### Simulation

When $\alpha = 2$,

![4](https://user-images.githubusercontent.com/17807597/117303475-b0007400-aeb7-11eb-9bfc-457e32a0642d.png)

When $\alpha = 4$,

![5](https://user-images.githubusercontent.com/17807597/117303608-db835e80-aeb7-11eb-8c87-0115212c1211.png)

### Exponential Random Variables

For α = λt, the Probability Variable at which an event first occurs in time t is zero. therefore If you put 0 in Poisson Random Variable, it is as follows.

$$
f = {e^{- \lambda t} (\lambda t)^0 \over 0!} = e^{- \lambda t}
$$

The time (random variables) t satisfied with:

$$
P(X>t) = e^{- \lambda t}
$$

CDF is as follows:

$$
P(0\leq X \leq t) = F(t) = 1- e^{- \lambda t} 
$$

PDF is as follows:

$$
f(t) = \lambda e^{- \lambda t}
$$

#### Simulation

When $\lambda = 2$, then,

![6](https://user-images.githubusercontent.com/17807597/117304984-4b461900-aeb9-11eb-8220-61681459051a.png)

