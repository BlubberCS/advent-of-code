
input = list(map(lambda x: x.strip(), open("input_files/day03.txt", "r").readlines()))

def sum_priorities(l):
    sum_p=0
    for i in l:
        if i.isupper():
            sum_p+=ord(i)-38
        else:
            sum_p+=ord(i)-96
    return sum_p

items=[]
for rucksack in input:
    items.append([l for l in rucksack[:len(rucksack)//2] if l in rucksack[len(rucksack)//2:]][0])

input_tuples = [tuple(input[i:i+3]) for i in range(0,len(input),3)]
badges=[]
for rucksack1,rucksack2,rucksack3 in input_tuples:
    badges.append([l for l in rucksack1 if l in rucksack2 and l in rucksack3][0])

print("sum of the priorities:", sum_priorities(items))
print("sum of the priorities (three-Elf group):", sum_priorities(badges))