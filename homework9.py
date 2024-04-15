# 1 вариант
list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
list_2 = (1, 2, 3, 4, 5)
cars_count = 0
for i in list_:
    for j in list_2:
        print('Я езжу на автомобиле марки ' + i, cars_count + 10 * j)

# 2 вариант
list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
list_2 = (1, 2, 3, 4, 5)
cars_count = 0
for i in list_:
    print('Я езжу на автомобиле марки ' + i)
for j in list_2:
    print('Я езжу на автомобиле марки ' + i, cars_count + 10 * j)