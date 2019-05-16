# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年05月16日 星期四 18时16分46秒

def gradient_a(a, b):
    return 10*a + 6*b - 8

def gradient_b(a, b):
    return 6*a + 4*b - 6

def update(a, b):
    return (a - 0.1 * gradient_a(a, b), b - 0.1 * gradient_b(a, b))

w = (0, 0)
for i in range(100):
    w = update(w[0], w[1])
    print(w)
