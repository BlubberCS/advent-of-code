input = list(map(lambda x: x.strip().replace("-",",").split(","), open("input_files/day04.txt", "r").readlines()))

print("assignment pairs range fully contain:", sum([1 for pair in input if set(range(int(pair[0]),int(pair[1])+1)).issubset(range(int(pair[2]),int(pair[3])+1)) or set(range(int(pair[2]),int(pair[3])+1)).issubset(range(int(pair[0]),int(pair[1])+1))]))
print("assignment pairs ranges overlap:", sum([1 for pair in input if set(range(int(pair[0]),int(pair[1])+1)).intersection(range(int(pair[2]),int(pair[3])+1))]))