
x = 100  # (file) global variable
y = 50



def spam():
    print("in spam(): x is", x)
    z = "zoril"  # local variable
    print("z:", z)

spam()
print(x, y)




