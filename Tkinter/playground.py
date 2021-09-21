def add(*args):
    return sum(args)
# or
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

print(add(2,3,4,5))