from time import sleep

value = 15
end = 25
inc = 0.1

for i in range(value*10, end*10, int(inc*10)):
    value = i/10
    print(value)
value = end
print(value)