def format_list(x):
    if len(x) == 0:
        return " "
    elif len(x) == 1:
        return x[0]

    return ", ".join(x[:-1]) + " and " + x[-1]


print(format_list(['apple', 'banana', 'tofu', 'cats']))
print(format_list(['a', 'b', 'c', 'd']))