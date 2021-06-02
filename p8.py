# program to generate random logs and write in a file
# once the file reaches 2Mb open new file and continue writing

import os

file_number = 1
file_size = 0
while True:
    if file_size < 2e+6:
        try:
            file = open('test%d.txt' % file_number, 'w+')
        except():
            pass
        file = open('test%d.txt' % file_number)
        text = file.read() + 'hello world!!!\nthis is a program to generate random logs and write in a file, ' \
                             'once the file reaches 2Mb open new file and continue writing'

        file = open('test%d.txt' % file_number, 'w')
        file.write(text)
        file.close()

    file_size = os.stat('test%d.txt' % file_number) .st_size
    if file_size > 2e+6:
        file_number += 1
        file_size = 0




