def func(x):
    x = x + 1
    print(x)

def func2(x):
    y = x.copy()
    x.append(1)

    # for element in x:
    #     element = element+1
    print(x)

x = 1
print(x)
func(x)
print(x)

y = [1,2]
print(y)
func2(y)
print(y)
