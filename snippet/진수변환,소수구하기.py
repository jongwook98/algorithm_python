# 나머지를 저장하여 연산이 끝난후 역변환하면 진수변환 완료

def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
# 에라토스테네스의 체

def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True