import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_string", type = str, help = "input a string")
args = parser.parse_args()

s = args.input_string

file_path = "./standard.txt"

number_of_lines = 1
output_level = []

for i in range(8):
    output_level.append([])

for ch in s:
    ascii_code = ord(ch)
    start_line = (ascii_code - 32) * 8 + (ascii_code - 32) + 2
    num_lines = 8

    with open(file_path, "r") as file:
        lines = file.readlines()

        selected_lines = lines[start_line - 1:start_line - 1 + num_lines]

    temp = (number_of_lines - 1) * 8
    for line in selected_lines:
        output_level[temp].append(line)
        temp += 1
        print(line, end=" ")
    
# print(output_level[0])
# print(output_level[1][0])
    
# for i in range(8):
    # for j in range(len(output_level[i])):
        # print(f"{output_level[i][j]}", end = "")
    # print(f"\n")
    