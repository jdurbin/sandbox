#!/usr/bin/env python

import string
import random


def seqgen(size, chars=['ACTG']):
    return ''.join(random.choice(chars) for _ in range(size))


print(seqgen(20))