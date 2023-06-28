
def company_logo(logo):
    logo_char = {}
    # count no of character in the word
    for character in logo:
        if character not in logo_char:
            logo_char[character] = 1
        else:
            logo_char[character] += 1
    # sort the keys alphabetically
    sorted_alpha = list(logo_char.keys())
    sorted_alpha.sort()
    sorted_alpha = {i: logo_char[i] for i in sorted_alpha}
    # sort values in dictionary
    sorted_logo = sorted(sorted_alpha.items(), key= lambda x: x[1], reverse=True)
    # print the first three characters
    for i in range(0, 3):
        print(sorted_logo[i][0], sorted_logo[i][1])
if __name__ == '__main__':
    s = input()
    company_logo(s)
"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

 has at least  distinct characters
Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters."""