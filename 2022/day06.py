from collections import Counter
input = open("input_files/day06.txt", "r").read().strip()

for i in range(len(input)): 
    if Counter(input[i:i+4]).most_common(1)[0][1] == 1:
        print("part 1:", i+4)
        break

for i in range(len(input)): 
    if Counter(input[i:i+14]).most_common(1)[0][1] == 1:
        print("part 1:", i+14)
        break