# https://www.hackerrank.com/challenges/text-alignment/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    line_thickness = int(input())
    # Draw the first part
    for i in range(1, line_thickness*2, 2):
        line = "H" * i
        if i % 2 == 1:
            thickness = (line_thickness * 2) - 1
            print(line.center(thickness, " "))
        else:
            thickness = (line_thickness * 2)
            print(line.center(thickness, " "))

    # Draw the second part
    edge_distance = line_thickness // 2
    thickness = (line_thickness * 5) + edge_distance
    for i in range(line_thickness+1):
        print(f"{'H'*line_thickness}{' '*line_thickness*3}{'H'*line_thickness}".rjust(thickness, " "))

    # Draw the middle
    for i in range(edge_distance+1):
        print("{}".format("H"*line_thickness*5).center(thickness+edge_distance, " "))

    # repeat the second part for this part
    for i in range(line_thickness+1):
        print(f"{'H'*line_thickness}{' '*line_thickness*3}{'H'*line_thickness}".rjust(thickness, " "))

    # rjust the first part for this last part
    thickness = (line_thickness * 5) + (edge_distance * 2) + 1
    for i in range(line_thickness*2-1, 0, -2):
        thickness -= 1
        line = "H" * i
        if i % 2 == 1:
            # thickness = (line_thickness * 2) - 1
            print(line.rjust(thickness, " "))
        else:
            thickness = (line_thickness * 2)
            print(line.rjust(thickness, " "))
