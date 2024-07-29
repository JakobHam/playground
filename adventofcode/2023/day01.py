import os
import re
from word2number import w2n
<<<<<<< HEAD
=======


def replace_written_digits(text):
    digits_words_pattern = re.compile(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|)+\b', re.IGNORECASE)
    
    def convert_match_to_digit(match):
        word_digit = match.group(0)
        try:
            return str(w2n.word_to_num(word_digit))
        except ValueError:
            return word_digit
    result = digits_words_pattern.sub(convert_match_to_digit, text)
    return result
>>>>>>> 1118d8298db2c990eca3bc801dd0dd62cc7f3735

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'source.txt')

digit_pattern = re.compile(r'\d')

sum = 0

file = open(file_path, 'r', encoding='utf-8')

for line in file:
    line = line.strip()
    line = replace_written_digits(line)
    digits = digit_pattern.findall(line)
    number = digits[0] + digits[-1]
    sum = sum + int(number)
print(sum)