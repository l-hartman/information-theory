#!/usr/bin/env python3
from collections import OrderedDict
from operator import itemgetter

def p2():
    syms = OrderedDict([('A', 0.9), ('B', 0.08), ('C', 0.02)])

    two_ext_probs = []
    for cond in syms.items():
        for pred in syms.items():
            prob = conditional_prob(cond, pred)

            two_ext_probs.append((prob, cond[0]+pred[0]))
    two_ext_probs.sort(key=itemgetter(0), reverse=True)

    for item in two_ext_probs:
        print(item)

def conditional_prob(cond, pred):
    """Return prob(pred|cond) for an independent event"""
    return cond[1] * pred[1]


def p3():
    a_given_a = 0.8
    a_given_b = 0.6
    b_given_a = 0.2
    b_given_b = 0.4

    prob_a = 0.75
    prob_b = 0.25

    prob_aa = a_given_a * prob_a
    prob_ab = b_given_a * prob_a
    prob_ba = a_given_b * prob_b
    prob_bb = b_given_b * prob_b

    init_huffman = [(prob_aa, 'aa'), (prob_ba, 'ba'), (prob_ab, 'ab'), (prob_bb, 'bb')]
    for item in init_huffman:
        print(item)


def p4():
    a_given_a = 0.8
    a_given_b = 0.6
    b_given_a = 0.2
    b_given_b = 0.4

    prob_a = 0.75
    prob_b = 0.25

    prob_aa = a_given_a * prob_a
    prob_ab = b_given_a * prob_a
    prob_ba = a_given_b * prob_b
    prob_bb = b_given_b * prob_b

    prob_aaa = prob_aa * prob_a
    prob_aab = prob_aa * prob_b
    prob_aba = prob_ab * prob_a
    prob_abb = prob_ab * prob_b
    prob_baa = prob_ba * prob_a
    prob_bab = prob_ba * prob_b
    prob_bba = prob_bb * prob_a
    prob_bbb = prob_bb * prob_b

    init_huffman = [(prob_aaa, "aaa"), (prob_aab, "aab"),(prob_aba, 'aba'), (prob_abb,'abb'), (prob_baa, 'baa'), (prob_bab, 'bab'), (prob_bba,'bba'), (prob_bbb, 'bbb')]
    init_huffman.sort(key=itemgetter(0), reverse=True)

    for item in init_huffman:
        print(item)



if __name__ == "__main__":
    #p2()
    #p3()
    p4()
