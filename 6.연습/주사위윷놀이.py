# 백준 사이트 누군가의 코드
# 엄청 짧게 잘했다

from sys import*
input = stdin.readline
def solve(pos, score):  #pos -> 몇 번째 주사위인지
    global horse, visit
    res = 0
    if pos == 10:return score
    b = [x[:] for x in horse]
    c = [x[:] for x in visit]
    for i in range(4):
        d, x = horse[i]       #방향, 인덱스
        prev_dice = dice[pos]
        nd = d
        nx = x + prev_dice
        if x == INF: continue
        if d == 0 and (x in [5,10,15]):     #d가 0이고(테두리), 확인할 index가 내부에 들어갈 인덱스면
            nd = x // 5                     #만약 idx가 5면 d=1, 10이면 d=2, ...
            nx = prev_dice
        if nd == 0 and nx == 20:            #d==0, x==20 이랑 d==4, x == 3 이랑 칸 중복되어서 따로 처리
            nd = 4
            nx = 3
        if nd in [1,2,3] and (len(a[nd]) <= nx):   #1,2,3 크기 넘어 갈 때
            nx = nx - len(a[nd])
            nd = 4
        if len(a[nd]) <= nx:                #도착, d=1,2,3일 때 넘은건 위에서 이미 처리됨(21 line)
            horse[i] = [0, INF]
            visit[d][x] = 0
            res = max(res, solve(pos+1, score))
        else:
            if visit[nd][nx]: continue
            horse[i] = [nd, nx]
            visit[nd][nx] = 1
            visit[d][x] = 0
            res = max(res, solve(pos+1, score + a[nd][nx]))
        horse=[x[:] for x in b]
        visit=[x[:] for x in c]
    return res

a=[[2*i for i in range(21)]]             # a[0] => 테두리
a.append([10, 13, 16, 19])  # a[1] => 5번째칸 갈 시 이동방향
a.append([20, 22, 24])      # a[2] => 10번째칸 갈 시 이동방향
a.append([30, 28, 27, 26])  # a[3] => 15번째칸 갈 시 이동방향
a.append([25, 30, 35, 40])  # a[4] => 내부에서 중복되는 놈들 처리 안해주면 visit 방문처리가 잘 안됨

INF = 1e9
dice = list(map(int,input().split())) #이동할 주사위 정보
visit=[[0]*21 for _ in range(5)]#1차:방향, 2차:인덱스
horse=[[0,0] for _ in range(4)] #1차:말 번호, 2차: [방향, 인덱스]
print(solve(0, 0))


'''
# 시간초과 나서 어차피 통과 못하겠지만

# 반복 하는 것에 대해서 함수화 하기
# 

Map = [i for i in range(2, 42, 2)]
root = [[], [13, 16, 19, 25, 30, 35, 40], [22, 24, 25, 30, 35, 40], [28, 27, 26, 25, 30, 35, 40]]
#        20  21  22  28  29  30  31    23  24  28  29  30  31    25  26  27  28  29  30  31

index_arr = [[], [20, 21, 22, 28, 29, 30, 31], [23, 24, 28, 29, 30, 31], [25, 26, 27, 28, 29, 30, 31]]

inMap = [False for _ in range(32)]

dice_ = list(map(int, input().split()))
piece = []

max_point = 0


def dfs(inMap, piece, index, point):
    global max_point

    print(piece, index, point)
    if index > 9:
        max_point = max(max_point, point)
        return

    if len(piece) < 4:
        if inMap[dice_[index] - 1] is False:
            inMap[dice_[index] - 1] = True
            piece.append(dice_[index] - 1)
            point += Map[dice_[index] - 1]

            dfs(inMap, piece, index + 1, point)

            inMap[dice_[index] - 1] = False
            piece.pop()
            point -= Map[dice_[index] - 1]

    for num, sel in enumerate(piece):
        if sel % 5 == 0 and 0 < sel < 20:
            if inMap[index_arr[sel // 5][dice_[index] - 1]] is False:
                inMap[sel] = False
                inMap[index_arr[sel // 5][dice_[index] - 1]] = True
                temp = piece[num]
                piece[num] = index_arr[sel // 5][dice_[index] - 1]
                point += root[sel // 5][dice_[index] - 1]

                dfs(inMap, piece, index + 1, point)

                inMap[sel] = True
                inMap[index_arr[sel // 5][dice_[index] - 1]] = False
                piece[num] = temp
                point -= root[sel // 5][dice_[index] - 1]

        elif sel < 20:
            if sel + dice_[index] < 20:
                if inMap[sel + dice_[index]] is False:

                    inMap[sel] = False
                    inMap[sel + dice_[index]] = True
                    temp = piece[num]
                    piece[num] = sel + dice_[index]
                    point += Map[sel + dice_[index]]

                    dfs(inMap, piece, index + 1, point)

                    inMap[sel] = True
                    inMap[sel + dice_[index]] = False
                    piece[num] = temp
                    point -= Map[sel + dice_[index]]
            else:
                # 빵점
                pass

        else:
            if sel < 23:
                pos = sel - 20
                if pos + dice_[index] < len(index_arr[1]):
                    if inMap[index_arr[1][pos + dice_[index]]] is False:

                        inMap[sel] = False
                        inMap[index_arr[1][pos + dice_[index]]] = True
                        temp = piece[num]
                        piece[num] = index_arr[1][pos + dice_[index]]
                        point += root[1][pos + dice_[index]]

                        dfs(inMap, piece, index + 1, point)

                        inMap[sel] = True
                        inMap[sel + dice_[index]] = False
                        piece[num] = temp
                        point -= root[1][pos + dice_[index]]

            elif sel < 25:
                pos = sel - 23
                if pos + dice_[index] < len(index_arr[2]):
                    if inMap[index_arr[2][pos + dice_[index]]] is False:

                        inMap[sel] = False
                        inMap[index_arr[2][pos + dice_[index]]] = True
                        temp = piece[num]
                        piece[num] = index_arr[2][pos + dice_[index]]
                        point += root[2][pos + dice_[index]]

                        dfs(inMap, piece, index + 1, point)

                        inMap[sel] = True
                        inMap[sel + dice_[index]] = False
                        piece[num] = temp
                        point -= root[2][pos + dice_[index]]

            elif sel < 28:
                pos = sel - 25
                if pos + dice_[index] < len(index_arr[3]):
                    if inMap[index_arr[3][pos + dice_[index]]] is False:
                        inMap[sel] = False
                        inMap[index_arr[3][pos + dice_[index]]] = True
                        temp = piece[num]
                        piece[num] = index_arr[3][pos + dice_[index]]
                        point += root[1][pos + dice_[index]]

                        dfs(inMap, piece, index + 1, point)

                        inMap[sel] = True
                        inMap[sel + dice_[index]] = False
                        piece[num] = temp
                        point -= root[3][pos + dice_[index]]

dfs(inMap, piece, 0, 0)
print(max_point)
'''