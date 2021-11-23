import random


def with_sc(c):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = c.get()
    global p
    p = "".join(random.sample(s, passlen))


def without_sc(c):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passlen = c.get()
    global p
    p = "".join(random.sample(s, passlen))
