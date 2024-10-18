def Second_Lowest(lst):
    lowest_score = lst[0][1]
    second_lowest_score = next(s for n,s in lst if s > lowest_score)
    loosers = [n for n,s in lst if s == second_lowest_score]
    for l in sorted(loosers):
        print(l)

if __name__ == '__main__':
    Students_Scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Students_Scores.append([name,score])
    sorted_score = sorted(Students_Scores, key=lambda x: x[1], reverse=False)
    Second_Lowest(sorted_score)
    
