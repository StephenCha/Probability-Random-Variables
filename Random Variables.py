import matplotlib.pylab as plt
import numpy as np
import math
import sympy as sy
from sympy import *

# Factorial Return Function
def factorial(value):
    multipl = 1
    if value == 0:
        return 1
    for i in range(1,value+1):
        multipl = i*multipl
    f = multipl
    return f

# Combination Return Function.
def Combination(n,r):
    int(n)
    int(r)
    if n<1 or r<0 or n<r:
        raise ValueError
    c = int(factorial(n) / (factorial(r)*factorial(n-r)))
    return c

# Binomial Probability Mass Function.
def Binomial_Pmf(trial, k, probability):
    n = trial # Array
    p = probability
    Binomial = Combination(n,k)*(p**k)*((1-p)**(n-k))
    return Binomial

def plot_Binomial(trial, probability):
    n = trial
    p = probability
    xbi = []
    ybi = []
    for i in range(n):
        y = Binomial_Pmf(n, i, p)
        xbi.append(i)
        ybi.append(y)
    return xbi, ybi

def ratio(a, k):
    R = a/k
    return R

def Poisson_Pmf(trial, k, probability):
    n = trial
    p = probability
    # Define constant alhpa a
    a = n * p

    if k == 0:
        return exp(-a)

    Poisson = (a**k) * exp(-a) / factorial(k)
    return Poisson

def plot_Poisson(trial,probability):
    n = trial
    p = probability
    xpo = []
    ypo = []
    for i in range(n):
        y = Poisson_Pmf(n, i, p)
        xpo.append(i)
        ypo.append(y)
    return xpo, ypo

def Exponential_Pmf(lamb, time):
    # Setting symbol operator (differential variable) t for differentiation.
    t = Symbol('t')
    # Instead of Poisson's alpha, I substitute lamba and differentiate it for the case where k=0, resulting in an explicit pmf.
    expon = sy.diff(1 - Poisson_Pmf(lamb, 0, t), t)
    temp = expon.subs(t, time) / lamb
    result = sy.exp(math.log(temp)) * lamb
    # The reason for the above process is that there is no process of converting strings to numeric types,
    # so it is calculated again after taking a natural log.
    return result

def plot_Exponential(lamb, time):
    # t = time
    t = np.linspace(0,time,100)
    l = lamb
    xex = []
    yex = []
    for i in t:
        y = Exponential_Pmf(l, i)
        xex.append(i)
        yex.append(y)
    return xex, yex

def Geometric_Pmf(success, probability):
    p = probability
    k = success
    Geometric = p*((1-p)**(k-1))
    return Geometric

def plot_Geometric(success, probability):
    k = success
    p = probability
    xge = []
    yge = []
    for i in range(k):
        y = Geometric_Pmf(i, p)
        xge.append(i)
        yge.append(y)
    return xge, yge

def main():
    n1 = int(input('Enter the number of trials with a large p: '))
    p1 = float(input('Enter the probability of trial: '))

    '''Bernoulli Random Variable'''
    xbe = [0, 1]
    ybe = [1-p1, p1]
    plt.title("Bernoulli Distribution Stem Plot")
    plt.stem(xbe, ybe, '-.')
    plt.xlabel("X : Bernoulli Random Variable")
    plt.ylabel("PMF")
    plt.show()

    '''Binomial Random Variable Plot'''
    xbi, ybi = plot_Binomial(trial = n1, probability = p1)
    plt.subplot(211)
    plt.title("Binomial Distribution Stem Plot")
    plt.stem(xbi, ybi, '-.')
    plt.xlabel("X : Binomial Random Variable")
    plt.ylabel("PMF")

    '''Geometric Random Variable Plot'''
    xge, yge = plot_Geometric(success = n1, probability = p1)
    plt.subplot(212)
    plt.title("Geometric Distribution Stem Plot")
    plt.stem(xge, yge, '-.')
    plt.xlabel("X : Geometric Random Variable")
    plt.ylabel("PMF")
    plt.show()

    n2 = int(input('Enter the number of trials with less p.: '))
    p2 = float(input('Enter the probability of trial: '))
    t = int(input('Enter how long the incident took place.: '))

    '''Poisson Random Variable Plot'''
    xpo, ypo = plot_Poisson(trial = n2, probability = p2)
    plt.subplot(211)
    plt.title("Poisson Distribution Stem Plot")
    plt.xlabel("X : Poisson Random Variable")
    plt.ylabel("PMF")
    plt.stem(xpo, ypo, '-.')

    '''Exponential Random Variable Plot'''
    l = n2 * p2
    xex, yex = plot_Exponential(lamb = l, time = t)
    plt.subplot(212)
    plt.title("Exponential Distribution Plot")
    plt.xlabel("X : Exponential Random Variable")
    plt.ylabel("PDF")
    plt.plot(xex, yex)

    plt.show()

main()