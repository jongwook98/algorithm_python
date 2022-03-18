# ㅋㅋ 틀림.
# 나머지 연산
# (A + B) % M = ((A % M) + (B % M)) % M
# (A * B) % M = ((A % M) * (B % M)) % M
# (A - B) % M = ((A % M) - (B % M)) % M python 의 경우 음수의 결과가 자동으로 양수로 변환됨

A, B, C = map(int, input().split())
print((A+B)%C, ((A%C)+(B%C))%C,(A*B)%C, ((A%C)*(B%C))%C, sep='\n')