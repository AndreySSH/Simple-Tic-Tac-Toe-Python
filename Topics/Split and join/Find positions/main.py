sequence = input().split(' ')
x = input()

positions = [str(i) for i in range(len(sequence)) if sequence[i] == x]
print('not found' if positions == [] else ' '.join(positions))