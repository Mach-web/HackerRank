# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# input_data = int(input())
# for N in range(input_data):
# line = input()
line = 'aa && as & dnj &&& bhjdc&&&&||adsd|cdo|||mkd||||gty ||'
and_regex = re.compile(r'(?<= )&&(?= )')
or_regex = re.compile(r"(?<= )\|\|(?= )")
# line = re.sub(and_regex, 'and', line)
line = re.sub(or_regex, 'or', line)
print(line)





