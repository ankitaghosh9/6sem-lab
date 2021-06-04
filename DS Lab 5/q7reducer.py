#!/usr/bin/env python

from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
even=0
odd=0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            #print ('%s\t%s' % (current_word, current_count))

            if (int(current_word) %2==0):
                even +=current_count
            else:
                odd+=current_count
        current_count = count
        current_word = word

if current_word == word:
    #print ('%s\t%s\t' % (current_word, current_count))
    if (int(current_word) %2==0):
        even +=current_count
    else:
        odd+=current_count

print("EVEN COUNT = ",even)
print("ODD COUNT = ",odd)
