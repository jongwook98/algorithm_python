'''
엄청 잘 짜여진 코드는 92ms
내 코드는 3332ms ㅋㅋㅋㅋㅋ..
분석

내 코드는 기본적으로 완전탐색,, 게다가 중복되는 지역을 검사하지 않음
-> 캐릭터가 가만히 있는 경우를 고려해서 생각하지 않았음

92ms 의 코드는 python set 자료구조 사용
set는 중복되는 값을 자동으로 제거해주며, set1 -= set2 이런식으로

set2 에 있는 집합을 빼주어 -> 차집합가능

+ set 는 변환 가능한 값을 가질 수 없음 -> 내부에서 값 변화 불가

'''
'''
참고 코드 	아이디 : jihun77, 제출번호 : 46765825
import sys
input=sys.stdin.readline
from collections import deque
move=[[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1],[0,0]]
arr=[]
wall=set()
for i in range(8):
    tmp=list(input().rstrip())
    for j in range(8):
        if tmp[j]=='#':
            wall.add((i,j))

q=deque([(7,0)])


for _ in range(7):
    qq=set()
    while q:
        cx,cy=q.popleft()
        
        for a,b in move:
            nx,ny=cx+a,cy+b
            if 0<=nx<8 and 0<=ny<8 and(nx,ny) not in wall:
                qq.add((nx,ny))

    wall={(x[0]+1,x[1]) for x in wall if x[0]<7}
    if not wall: #벽이없으면 무조건 갈 수 있다.
        print(1)
        exit()
    qq-=wall #벽이랑 곂치는 부분 제외하기
    if not qq: #더 나아갈 부분이 없으면 못가는거
        print(0)
        exit()
    
    for qqq in qq:
        q.append(qqq)

print(1)
'''

from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10**5)

dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

global_Map = [[deque() for _ in range(8)] for _ in range(8)]
input_Map = [list(stdin.readline().strip()) for _ in range(8)]

global_wall_num = [0 for _ in range(8)]
escape_flag = 0

for y in range(7, -1, -1):
    for x in range(8):
        if input_Map[y][x] == '#':
            global_wall_num[0] += 1
        global_Map[0][x].append(input_Map[y][x])

for s in range(7):
    for y in range(8):
        for x in range(8):
            if x + 1 < 8:
                if global_Map[s][y][x + 1] == '#':
                    global_wall_num[s + 1] += 1
                global_Map[s + 1][y].append(global_Map[s][y][x + 1])
            else:
                global_Map[s + 1][y].append('.')

def move_charter(y, x):
    global escape_flag
    global global_wall_num

    Que = deque()
    Que.append([y, x, 0])

    while len(Que):
        cur_y, cur_x, time = Que.popleft()

        if escape_flag == 0 and (time >= 8 or global_wall_num[time] == 0):
            Que.clear()
            escape_flag = 1
            return print(1)

        for i in range(9):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < 8 and 0 <= nx < 8:
                if time < 7:
                    if global_Map[time + 1][ny][nx] != '#' and global_Map[time][ny][nx] != '#':
                        Que.append([ny, nx, time + 1])

                else:
                    if global_Map[time][ny][nx] != '#':
                        Que.append([ny, nx, time + 1])

    return print(0)

if __name__=="__main__":
    move_charter(0, 0)
