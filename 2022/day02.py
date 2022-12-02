"""
First column        Second column
A -> Rock           X -> Rock
B -> Paper          Y -> Paper
C -> Scissor        Z -> Scissor

Score 
Rock -> 1   
Paper -> 2
Scissor -> 3
lose -> 0           X -> lose
draw -> 3           Y -> draw
win -> 6            Z -> win
"""

ldw_map = {
    "A":"ZXY",
    "B":"XYZ",
    "C":"YZX"
}

shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

ldw_index_map = {
    "X": 0,
    "Y": 1,
    "Z": 2
}

ldw_score=[0,3,6]

input = map(lambda x: x.strip().split(), open("input_files/day02.txt", "r").readlines())
score1=0
score2=0

for p1,p2 in input:
    score1+=ldw_score[ldw_map[p1].index(p2)]+shape_score[p2]
    score2+=ldw_score[ldw_index_map[p2]]+shape_score[ldw_map[p1][ldw_index_map[p2]]]

print("total score:", score1)
print("total score:", score2)