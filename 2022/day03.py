
input = map(lambda x: x.strip(), open("input_files/day03.txt", "r").readlines())
sum=0

for rucksack in input:
    letter=[letter for letter in rucksack[slice(0,len(rucksack)//2)] if letter in rucksack[slice(len(rucksack)//2,len(rucksack))]][0]
    if letter.isupper():
        sum+=ord(letter)-38
    else:
        sum+=ord(letter)-96

print("sum of the priorities", sum)