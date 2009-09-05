#!/usr/bin/env python
print reduce(lambda y, x: y + (x<24) * x, map(int, file("count").read().split()), 0)
