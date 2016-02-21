# -*- coding: utf-8 -*-

import sys
from collections import Counter

result = []
for value in open(sys.argv[1], 'r'):
    result.append(value.replace('\n', ''))

counter = Counter(result)

for word, cnt in counter.most_common():
    print word + ' "' + str(cnt) + '"'

