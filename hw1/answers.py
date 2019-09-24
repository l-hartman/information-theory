#!/usr/bin/env python3

"""
Luke Hartman
13-9-19
CPSC 410
HW1 #1-3
"""

import numpy as np


def information(xs):
    base = 2
    i = lambda x: -1 * (np.log(x) / np.log(base))
    return i(xs)


def zero_memory_src_entropy(xs):
    xs_info = information(xs)
    return sum([a * b for a, b in zip(xs, xs_info)])


def fst_order_markov_src_entropy(transition_matrix, symbol_probs):
    items = []
    for index, symbol_prob in enumerate(symbol_probs):
        row_sum = 0
        for prob in transition_matrix[index]:
            row_sum += state_probability(prob)
        items.append(-1 * symbol_prob * row_sum)
    return sum(items)


def state_probability(prob):
    return prob * np.log(prob)


def problem1():
    p_A = 0.9
    p_B = 0.08
    p_C = 0.02

    symbol_probs = [p_A, p_B, p_C]

    entropy = zero_memory_src_entropy(symbol_probs)
    print("problem 1: ", entropy)


def problem2():
    # probabilities of two-dice sums
    probs = [
        0.0278,
        0.0556,
        0.0833,
        0.1111,
        0.1389,
        0.1667,
        0.1389,
        0.1111,
        0.0833,
        0.0556,
        0.0278,
    ]
    print("problem 2:", zero_memory_src_entropy(probs))


def problem3():
    A_given_A = 0.8
    A_given_B = 0.6
    B_given_B = 0.4
    B_given_A = 0.2

    transition_matrix = np.array([[A_given_A, B_given_A], [A_given_B, B_given_B]])

    # 3a. Determine P(a) and P(b)
    p_a = 0.6 / 0.8
    p_b = 1 - p_a
    symbol_probs = [p_a, p_b]
    print("problem 3a:")
    print("\tP(A): ", p_a, "\n\tP(B): ", p_b)

    # 3b. Determine the entropy of the source
    source_entropy = fst_order_markov_src_entropy(transition_matrix, symbol_probs)
    print("problem 3b.")
    print("\tsource entropy: ", source_entropy)

    # 3c. Determine the entropy of the adjoint source
    adjoint_entropy = sum([-1 * state_probability(prob) for prob in symbol_probs])
    print("problem 3c.")
    print("\tadjoint source entropy: ", adjoint_entropy)


problem1()
problem2()
problem3()
