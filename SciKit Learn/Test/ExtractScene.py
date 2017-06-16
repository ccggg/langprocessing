import os
from io import open

old_dir = 'Z:/My Documents/Python/SciKit Learn/Test/txt'
new_dir = 'Z:/My Documents/Python/SciKit Learn/Test/scenes'
strings = ('[Scene:')

for file in os.listdir(old_dir):
    with open(old_dir + '/' + file, 'r', encoding='utf-8-sig') as open_file:
        f = open(new_dir + '/' + file, 'w+', encoding='utf-8-sig')
        for line in open_file:
            if "[Scene:" in line:
                line = line.replace('[Scene:','')
                line = line.replace(']','')
                line = line.lstrip(' ')
                f.write(line)
