def maximum2(first, second):
    return max(first, second)

def maximum3(first, second, third):
    return maximum2(maximum2(first, second), third)

print(maximum3(1, 3, 5))