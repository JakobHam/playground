import os
import re
from word2number import w2n
<<<<<<< HEAD
=======

>>>>>>> 184f3f26061d94140eb6302bb7fc6bca13da4e8d

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'source.txt')

digit_pattern = re.compile(r'\d')

sum = 0

file = open(file_path, 'r', encoding='utf-8')

for line in file:
    line = line.strip()
    line = w2n.word_to_num(line)
    digits = digit_pattern.findall(line)
    number = digits[0] + digits[-1]
    sum = sum + int(number)
print(sum)