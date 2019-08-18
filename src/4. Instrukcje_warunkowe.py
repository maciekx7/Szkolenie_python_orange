x = 5
y = 4
z = 6

if x > y:
    print(f'x({x}) > y({y})')
elif x < y:
    print(f'x({x}) < y({y})')
else:
    print(f'x({x}) = y({y})')

print("--------------------")


if x>y and x>z:
    print("x jest wieksze od y i z")
elif x>y or x>z:
    print("x jest wieksze od y LUB z")
else:
    print("jest inaczej!")