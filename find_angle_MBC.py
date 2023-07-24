# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
'''
import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    #find the diagonal
    AC = math.sqrt((AB ** 2) + (BC ** 2))
    MC = AC / 2
    #find half length of diagonal
    '''use the sine rule to find angle MCB
    degrees are first converted into radians'''
    MCB = AB * math.sin(math.radians(90)) / AC
    MCB = math.asin(MCB) * 180 * 7 / 22
    # use cosine rule to find length MB
    MB = (MC ** 2 + BC ** 2) - (2 * MC * BC * math.cos(math.radians(MCB)))
    MB = math.sqrt(MB)
    # find angle MBC using sine rule
    MBC = (MC * math.sin(math.radians(MCB))) / MB
    MBC = math.asin(MBC) * 180 * 7 / 22
    # round off to nearest integer
    MBC = round(MBC)
    # the character unicode for degrees is 176
    print(f'{MBC}{chr(176)}')