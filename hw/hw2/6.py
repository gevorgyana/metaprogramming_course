#!/usr/bin/env python

import os

out = set()
for path, _, _ in os.walk('.'):
    out.add(path)

print(out)
