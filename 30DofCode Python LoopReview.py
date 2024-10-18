N = int(input())

for T in range(0, N):
    S = input()
    even=""
    odd=""
    current_index=0
    if len(S) >= 2 and len(S) <= 10000:
        for elements in S:
            index = S.index(elements, current_index, len(S))
            if (index % 2 == 0 or index == 0):
                even = even + S[index]
                current_index = index+1
            elif (index % 2 != 0 or index != 0):
                odd = odd + S[index]
                current_index = index+1
    print(f'{even} {odd}')
