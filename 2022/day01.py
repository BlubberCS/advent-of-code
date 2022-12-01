all_calories=[]
calorie=[]

for line in open("input_files/day01.txt", "r"): 
    if line.strip(): 
        calorie.append(int(line))
    else:
        all_calories.append(sum(calorie))
        calorie.clear()

print("Elf most Calories", max(all_calories))
print("top three Elves total Calories", sum(sorted(all_calories)[-3:]))