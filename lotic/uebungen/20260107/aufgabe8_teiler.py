user_input = input('Bitte gib eine ganze Zahl ein: ')
number = 0
try:
    number = int(user_input)
except:
    print('-_-')
div_list = []
for i in range (1, number+1):
    if number % i == 0:
        div_list.append(i)

print(div_list)
