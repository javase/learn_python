print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))

print('\n'.join([''.join([('Sherry'[(x - y) % len('Sherry')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0else' ')for x in range(-32, 32)]) for y in range(17, -17, -1)]))
