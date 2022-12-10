import re
import copy

input = iter(open("input_files/day05.txt","r").read().splitlines())
crates=[]
stacks=[]

for line in input:
    if not line:
        break
    if line.startswith(" 1"):
        stacks = [[] for _ in re.findall("\d",line)]
        continue
    for c,v in enumerate(line[1::4]):
        crates.append((c,v))

for c,v in crates:
    if not v.isspace():
        stacks[c].insert(0,v)

rearrangement_procedure = list(map(lambda line: re.findall("\d+",line), input))
stacks2=copy.deepcopy(stacks)

for r in rearrangement_procedure:
    pop = [stacks[int(r[1])-1].pop() for _ in range(int(r[0]))]
    for p in pop: stacks[int(r[2])-1].append(p)
    pop2 = [stacks2[int(r[1])-1].pop() for _ in range(int(r[0]))][::-1]
    for p in pop2: stacks2[int(r[2])-1].append(p)

print("crate ends up on top of each stack (part 1):", "".join(s[-1] for s in stacks))
print("crate ends up on top of each stack (part 2):", "".join(s[-1] for s in stacks2))