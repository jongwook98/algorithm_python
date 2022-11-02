def solution(alp, cop, problems):

    inf = int(1e4)

    max_alp, max_cop = 0, 0
    for aq, cq, ar, cr, cost in problems:
        max_alp = max(max_alp, aq)
        max_cop = max(max_cop, cq)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    dp = [[inf for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for aq, cq, ar, cr, cost in problems:
                if i >= aq and j >= cq:
                    up_al, up_co = i + ar, j + cr
                    if up_al > max_alp:
                        up_al = max_alp
                    if up_co > max_cop:
                        up_co = max_cop

                    dp[up_al][up_co] = min(dp[up_al][up_co], dp[i][j] + cost)

    print(*dp)
    answer = dp[-1][-1]
    return answer