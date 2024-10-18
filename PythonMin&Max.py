import numpy as np

ax0, ax1 = map(int, input().split())

data = np.array([list(map(int, input().split())) for _ in range(ax0)])

result = np.max(np.min(data, axis=1))

print(result)
