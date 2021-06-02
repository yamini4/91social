# a script which can read the files line by line with .log and print it into a file
import re
log_file_path = r"C:\Users\navee\Desktop\intern\social\Lib\sample.log"
regex = '(<property name="(.*?)">(.*?)<\/property>)'

match_list = []
file = open(log_file_path, 'r')
for line in file:
    for match in re.finditer(regex, line, re.S):
        match_text = match.group()
        match_list.append(match_text)
        print(match_text)

