a = "Chris"
b = 482323523
c = 19 / 6
print(a, b, c)  # print(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')
print()
print(a, b, c, sep="|")
print(a, b, c, sep='')
print(a)
print(b)
print(c)
print()

print(a, end='/')
print(b, end='/')
print(c)
print()

#  print something, but don't go to next line  (end=' ')
#  if some condition
#      print something, don't go to next line  (end=' ')
#  print something, go to next line (DEFAULT: end='\n')

print("{} {:,d} {:.2f}".format(a, b, c))
print(f"{a} {b:,d} {c:.2f} {b / c:.3f}")

m = 19
print("{:04d}".format(m))
print(f"{m:04d}")




