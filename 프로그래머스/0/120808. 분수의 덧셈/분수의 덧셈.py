from math import gcd

def solution(numer1, denom1, numer2, denom2):
    number = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    d = gcd(number, denom)
    
    return [number // d, denom // d]