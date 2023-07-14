'''https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

input_data = int(input())
and_regex = re.compile(r'(?<= )&&(?= )')
or_regex = re.compile(r'(?<=\s)\|\|(?=\s)')

for N in range(input_data):
    lines = input()
    lines = re.sub(and_regex, 'and', lines)
    lines = re.sub(or_regex, 'or', lines)
    print(lines)





