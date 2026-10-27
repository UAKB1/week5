while_bro = 1
i = 10
for_bro = 1
while i < 14:
    while_bro = while_bro * i
    i+= 1
print(while_bro)
for ece in range(10, 14):
    for_bro = for_bro * ece
print(for_bro)
if for_bro == while_bro:
    print("Both methods give the same result.")
else:
    print("The methods give different results.")    