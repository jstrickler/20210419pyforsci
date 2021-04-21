

# def divmod(a, b):
#     return a // b, a % b

print(divmod(18, 4))
print(divmod(365, 90))

values = 43, 8

print(divmod(*values))

def spam(a, b, c, d):
    print(a, b, c, d)

spam(5, *values, 10)
# spam(5, 43, 8, 10)
