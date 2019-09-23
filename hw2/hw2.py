#!/usr/bin/env python3

from collections import OrderedDict

def p1():
    syms = OrderedDict([('A', 0.9), ('B', 0.08), ('C', 0.02)])

    # Given condition, find prob(pred)
    for cond in syms.items():
        for pred in syms.items():
            print("cond: ", cond, " pred: ", pred, end=" prob=")
            print(conditional_prob(cond, pred))

def conditional_prob(cond, pred):
    """Return prob(pred|cond) for an independent event"""
    joint_prob = cond[1] * pred[1]
    return joint_prob



if __name__ == "__main__":
    p1()
