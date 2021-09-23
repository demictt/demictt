
def runnerup(score):
    nums = map(int, Scores)
    print(sorted(list(set(nums)))[-2])

Scores = [2, 3, 6, 6, 5]

runnerup(Scores)
