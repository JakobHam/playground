import os


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'source.txt')

file = open(file_path, 'r', encoding='utf-8')

print(file)

print('Hello World')