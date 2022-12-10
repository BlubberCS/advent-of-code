import re

input=open("input_files/day10.txt", "r").read().splitlines()
X=1
cycle=0
cycles_multiplied=[20,60,100,140,180,220]
instruction=[]
part1=0
tmp_CRT=""
CRT=""

def drawCRT():
    global tmp_CRT
    if X - 1 <= len(tmp_CRT) <= X + 1:
        tmp_CRT+="#"
    else:
        tmp_CRT+="."
        
for line in input: 
    if line == "noop": instruction.append("noop")
    else:
        instruction.append("addx")
        instruction.append(int(re.findall("-?\d+",line)[0]))

while instruction:
    cycle+=1
    el=instruction.pop(0)
    drawCRT()
    if cycle in cycles_multiplied: 
        part1+=X*cycle
    if cycle % 40==0:
        CRT+=tmp_CRT
        tmp_CRT=""
    if type(el) == int:
        X+=el

print("sum of these six signal strengths:", part1)
for idx in range(0, len(CRT), 40):
    print((CRT[idx:idx + 40]).replace("."," "))