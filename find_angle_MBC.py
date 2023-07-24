# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    AC = math.sqrt((AB ** 2) + (BC ** 2))
    MC = AC / 2
    MCB = AB * math.sin(math.radians(90)) / AC
    MCB = math.asin(MCB) * 180 * 7 / 22
    MB = (MC ** 2 + BC ** 2) - (2 * MC * BC * math.cos(math.radians(MCB)))
    MB = math.sqrt(MB)
    MBC = (MC * math.sin(math.radians(MCB))) / MB
    MBC = math.asin(MBC) * 180 * 7 / 22
    MBC = round(MBC)
    print(f'{MBC}{chr(176)}')