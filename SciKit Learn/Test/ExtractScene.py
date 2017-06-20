import os
from io import open

import re

old_dir = 'Z:/My Documents/Python/SciKit Learn/Test/txt'
new_dir = 'Z:/My Documents/Python/SciKit Learn/Test/scenes'
start_string = ('[Scene:')

for file in os.listdir(old_dir):
    with open(old_dir + '/' + file, 'r', encoding='utf-8-sig') as open_file:
        f = open(new_dir + '/' + file, 'w+', encoding='utf-8-sig')
        for line in open_file:
            if ">[Scene:" in line:
                line = line.replace(']','')
                line = line.encode('ascii', 'ignore')
                line = line.lstrip(' ')
                if '>[Scene:' in line:
                    line = line.split('>[Scene: ')[1]
                f.write(unicode(line))
