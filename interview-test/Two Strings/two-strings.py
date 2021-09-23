from collections import Counter

def twoStrings(s1, s2):
    string s1
    d1 = Counter(s1)
    d2 = Counter(s2)

    Cd = d1 & d2

    if len(Cd) > 0:
        return 'YES'
    else:
        return 'NO'
