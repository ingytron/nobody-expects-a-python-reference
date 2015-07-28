def sumDigits(N):
    digits = 0
    if N > 10:
        digits += 1
        N = N /10
    elif N < 10 :
        digits += 1
    return digits 
