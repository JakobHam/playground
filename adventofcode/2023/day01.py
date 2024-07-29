import os
import re

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'source.txt')

digit_pattern = re.compile(r'\d')

file = open(file_path, 'r', encoding='utf-8')

for line in file:
    line = line.strip()
    digits = digit_pattern.findall(line)
    number = digits[0] + digits[-1]
    print(number)