def calculate(pwrs, index, time, cost):
    index = str(index)
    return round(pwrs[index]*time*cost / 1000.00, 2)


def calc_to_text(pwrs, index, time, cost):
    dic = {
        '0': 'Утюг',
        '1': 'Телевизор',
        '2': 'Стиральная машина'
    }
    index = str(index)
    return (dic[index]+' потребляет '+str(calculate(pwrs, index, time, cost))+' рыбов')
