def cartesian_product(lists):

    result = [[]]

    for lst in lists:

        result = [x + [y] for x in result for y in lst]
    return result

K, M = map(int, input().split())

k_lists = []

for k in range(K):

    k_lists.append(list(map(lambda x: x**2, list(map(int, input().split()))[1:])))


all_combinations = cartesian_product(k_lists)


max_mod_sum = max([sum(comb) % M for comb in all_combinations])

print(max_mod_sum)
