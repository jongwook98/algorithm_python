from collections import deque

S = int(input())
emoji = 1

clipboard = 0
Que = deque()

check = [[False] * 1001 for _ in range(1001)]
check[emoji][clipboard] = True
cnt = 1

method = [emoji, clipboard, 0]
Que.append(method)

while True:
    cur_state = Que.popleft()
    emoji = cur_state[0]
    clipboard = cur_state[1]

    if clipboard != 0:
        if emoji + clipboard == S:
            print(cur_state[2] + 1)
            break

        elif emoji+clipboard <= 1000:
            if check[emoji+clipboard][clipboard] == False:
                method = [emoji+clipboard, clipboard, cur_state[2] + 1]
                Que.append(method)
                check[emoji+clipboard][clipboard] = True

    if check[emoji][emoji] == False:
        method = [emoji, emoji, cur_state[2] + 1]
        Que.append(method)
        check[emoji][emoji] = True

    if emoji-1 == S:
        print(cur_state[2] + 1)
        break

    elif emoji-1 >= 0:
        if check[emoji-1][clipboard] == False:
            method = [emoji-1, clipboard, cur_state[2] + 1]
            Que.append(method)
            check[emoji-1][clipboard] = True