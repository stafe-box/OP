import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Постарался сделать более читаемым код.
# Можно, пожалуйста, подробнее, что конкретно не читаемо было для Вас.
# Как бы Вы это написали, а лучше на примере из 05_snowfall.py

# кол-во снежинок
snowflakes_count = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

sd.resolution = (1200, 600)

# высота с которой будут падать снежинки
y = 600

snowflakes = {}
snowflake_size = {'min': 5, 'max': 30}

# заполняем словарь с параметрами снежинок
for i in range(snowflakes_count):
    snowflakes[i] = {'length': sd.random_number(snowflake_size['min'], snowflake_size['max']),
                     'x': sd.random_number(0, sd.resolution[0]),
                     'y': y,
                     'factor_a': sd.random_number(1, 10)/10,
                     'factor_b': sd.random_number(1, 10)/10,
                     'factor_c': sd.random_number(1, 120)
                     }

while True:

    sd.start_drawing()

    for snowflake_num, snowflake_parameter in snowflakes.items():

        start_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=start_point,
                     length=snowflake_parameter['length'],
                     color=sd.background_color,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        snowflake_parameter['x'] += sd.random_number(0, 2)
        snowflake_parameter['y'] -= snowflake_size['max'] + 1 - snowflake_parameter['length']

        next_point = sd.get_point(snowflake_parameter['x'], snowflake_parameter['y'])
        sd.snowflake(center=next_point,
                     length=snowflake_parameter['length'],
                     color=sd.COLOR_WHITE,
                     factor_a=snowflake_parameter['factor_a'],
                     factor_b=snowflake_parameter['factor_b'],
                     factor_c=snowflake_parameter['factor_c'])

        if snowflake_parameter['y'] < 50:
            snowflake_parameter['y'] = y
            snowflake_parameter['length'] = sd.random_number(snowflake_size['min'], snowflake_size['max'])
            snowflake_parameter['x'] = sd.random_number(0, sd.resolution[0])

    sd.finish_drawing()
    sd.sleep(0.01)

    if sd.user_want_exit():
        break

sd.pause()
