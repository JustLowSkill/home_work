#Не скучай при проверке

inital_list = [1, 5, 4, 3, 5, 6, 7, 4, 5, 6, 7, 5, 4, 3, 5, 4, 3, 2, 5, 4, 5, 9, 0, 5, 7, 3,
4, 3, 7, 0, 9, 5, 0, 3, 5, 4, 3, 6, 4]
print(set(range(10))-set(inital_list))
fisrt_list = list(range(401))
second_list = [i for i in fisrt_list[100:301] if i%7==0]
print(second_list)
print(second_list[-1:-6:-1])
