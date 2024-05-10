def add_n(n):
    def partial(x):
        return x+n
    return partial


add_three = add_n(3)

print(add_three(5))