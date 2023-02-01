from drawzero import *
import random
import time

while True:
    # отрисовка текста для выбора режима
    fill("#2E282A")
    for i in range(0, 1000, 80):
        for j in range(0, 1000, 80):
            filled_rect("#A997DF", j, i, 81, 81)
            text('#2E282A', 'Случайный город', (150, 150), 90)
            text('#2E282A', 'Введите:', (50, 300), 72)
            text('#2E282A', '"0" - если вам нужна анимация', (50, 500), 60)
            text('#2E282A', '"1" - если вам нужна раскраска', (50, 700), 60)
            text('#2E282A', '"2" - если вы не знаете, что выбрать', (50, 900), 60)
            sleep(1/55)


    # выбор режима: раскраска/цветной
    while 0 == 0:
        print('Если вам нужна анимация, введите \"0\"')
        print('Если вам нужна раскраска, введите \"1\"')
        print('Если вы не знаете, что выбрать, введите \"2\"')
        color_mode = input()
        if color_mode == "2":
            color_mode = str(random.randint(0,1))

        if color_mode == "0" or color_mode == "1":
            break
        print("UNEXPECTED INPUT VALUE. НЕДОПУСТИМЫЙ ФОРМАТ ВВОДА.")


    # переменные (house_(x,y) - координаты центра нижней части крыши)
    house_x = -100
    house_y = 120
    house_width = 90
    wall_height = 120

    def draw_all_houses():
        for row in range(250, 1200, 200):
            house_x = -75
            house_y = row
            for x_in_row in range(0, 10):
                between_houses = random.randint(100, 120)
                house_x += between_houses
                draw_house()
                sleep(1 / 40)
                house_width = random.randint(90, 110)

    # закрашивание текста фоном
    for i in range(0, 1000, 100):
        for j in range(0, 1000, 100):
            filled_rect("#2E282A", j, i, 101, 101)
            sleep(1/50)

    if color_mode == "0":

        roof_color_set = ["#AAA0EB", "#A6D2F5", "#A3DECF", "#A6F5A8", "#F3FAC0"]
        wall_color_set = ["#D2F7F0", "#C0F0D8", "#B9D9C0", "#C4F0C0", "#CCE6B8"]
        window_color_set = ["#03045e", "#023e8a", "#0077b6", "#0096c7", "#00b4d8", "#48cae4", "#90e0ef", "#ade8f4", "#caf0f8"]
        tree_leaves_color_set = ["#091e05", "#8fcf95", "#004f2d", "#9FD02C", "#B8E63C", "#5DD39E", "#348AA7", "#95F9E3", "#69EBD0", "#49D49D", "#558564", "#2AFC98", "#09E85E", "#16C172", "#214F4B"]
        tree_wood_color_set = ["#796465", "#280003", "#BAAB68", "#1A281F", "#1B2F33"]

        # массив для хранения координат деревьев

        all_tree_pos = []
        all_tree_x_y = []

        # функция для фона
        def draw_day():
            fill("#D6FF65")
            filled_rect("#B1E7F5", 0, 0, 1000, 180)

        # функция для крыши
        def draw_roof():
            roof_number = random.randint(0, 1)
            roof_color = random.randint(0, 4)
            if roof_number == 0:
                roof_x = house_x
                roof_y = house_y
                roof_rad = house_width // 2
                filled_circle(roof_color_set[roof_color], roof_x, roof_y, roof_rad)
            elif roof_number == 1:
                roof_x = house_x - (house_width // 2)
                roof_y = house_y
                roof_height = random.randint(30, 45)
                filled_polygon(roof_color_set[roof_color], roof_x, roof_y, house_x, (roof_y-roof_height), (roof_x+house_width), roof_y)


        # функция для стены
        def draw_wall():
            wall_number = 0
            wall_color = random.randint(0, 4)
            if wall_number == 0:
                wall_x = house_x - (house_width // 2)
                wall_y = house_y
                wall_width = house_width
                wall_height = 120
                filled_rect(wall_color_set[wall_color], wall_x, wall_y, wall_width, wall_height)

        # window
        def draw_window():
            window_color = random.randint(0, 8)
            window_number = random.randint(0, 1)
            if window_number == 0:
                window_x = house_x
                window_y = house_y + (wall_height // 2)
                filled_circle("#FFFFFF", window_x, window_y, (house_width // 3))
                filled_circle(window_color_set[window_color], window_x, window_y, (house_width // 4))
            elif window_number == 1:
                window_x = house_x - (house_width // 3)
                window_y = house_y + (wall_height // 3)
                filled_rect("#FFFFFF", window_x, window_y, (house_width * 5 // 9), (wall_height * 5 // 9))
                filled_rect(window_color_set[window_color], (window_x + house_width // 10), (window_y + wall_height // 10), (house_width * 7 // 18), (wall_height * 7 // 18))

        # дерево
        def draw_tree():
            tree_x = house_x
            tree_y = house_y + (wall_height // 2)
            tree_leaves_color = random.randint(0, 14)
            tree_wood_color = random.randint(0, 4)
            filled_rect(tree_wood_color_set[tree_wood_color], house_x - 6, house_y, 12, wall_height)
            for tree_leaves in range (5):
                filled_circle(tree_leaves_color_set[tree_leaves_color], tree_x, tree_y-(tree_leaves*11), 37-(tree_leaves*2))

            tree_pos = [house_x - (house_width // 2), house_y - 30, house_width, wall_height + 40, house_x, house_y]
            all_tree_pos.append(tree_pos)


        # функция для всего дома
        def draw_house():
            house_or_not = random.randint(0, 4)
            if house_or_not == 0 or house_or_not == 1:
                draw_tree()
            else:
                draw_roof()
                draw_wall()
                draw_window()

        draw_day()

        # настройка параметров для солнца
        sun_x = 0
        sun_y = 140
        sun_rad = 40
        sun_brightness = 0
        def draw_sun():
            filled_circle("#FFFD64", sun_x, sun_y, sun_rad, alpha=sun_brightness)
            filled_circle("#E0D44F", sun_x, sun_y, sun_rad-5, alpha=sun_brightness)
            filled_circle("#F5D84C", sun_x, sun_y, sun_rad-10, alpha=sun_brightness)
            filled_circle("#DEBF4E", sun_x, sun_y, sun_rad-15, alpha=sun_brightness)
            filled_circle("#FACC57", sun_x, sun_y, sun_rad-20, alpha=sun_brightness)
        draw_sun()

        # вывод домов на экран
        for row in range (250, 1200, 200):
            house_x = -75
            house_y = row
            for x_in_row in range (0, 10):
                between_houses = random.randint(100, 120)
                house_x += between_houses
                draw_house()
                sleep(1/40)
                house_width = random.randint(90, 110)

        # анимация деревьев
        for tree_grow_days in range (2):
            for tree_grow in range(len(all_tree_pos)):
                filled_rect("#D6FF65", all_tree_pos[tree_grow][0], all_tree_pos[tree_grow][1], all_tree_pos[tree_grow][2], all_tree_pos[tree_grow][3])
                house_x = all_tree_pos[tree_grow][4]
                house_y = all_tree_pos[tree_grow][5]
                draw_tree()
                sleep(1/20)

        # анимация солнца
        for sun_days in range(2):
            for sun_move in range (0, 500):
                sun_x = sun_move
                sun_y -= 1/7
                draw_sun()
                sleep(1/180)
                filled_rect("#B1E7F5", 0, 0, 1000, 180)
                sun_brightness = 80 + (sun_move / 50)
                sun_rad -= 1/50
            for sun_move in range (500, 1000):
                sun_x = sun_move
                sun_y += 1/7
                draw_sun()
                sleep(1/180)
                filled_rect("#B1E7F5", 0, 0, 1000, 180)
                sun_brightness = 80 + (sun_move / 50)
                sun_rad += 1/50
            for sun_move in range (1000, 500, -1):
                sun_x = sun_move
                sun_y -= 1/7
                draw_sun()
                sleep(1/180)
                filled_rect("#B1E7F5", 0, 0, 1000, 180)
                sun_brightness = 80 + (sun_move / 50)
                sun_rad -= 1/50
            for sun_move in range (500, 0, -1):
                sun_x = sun_move
                sun_y += 1/7
                draw_sun()
                sleep(1/180)
                filled_rect("#B1E7F5", 0, 0, 1000, 180)
                sun_brightness = 80 + (sun_move / 50)
                sun_rad += 1/50

        draw_sun()

        # завершение программы
        sleep(1)
        for i in range(50):
            filled_rect("#2E282A", 0, 0, 1000, 1000, alpha=(i*2))
            sleep(1/20)

        for i in range(501):
            filled_rect("#FFFFFF", 0, i, 1000, 1)
            filled_rect("#FFFFFF", 0, 1000-i, 1000, 1)
            sleep(1/200)

        for i in range(501):
            filled_rect('#2E282A', i, 0, 1, 1000)
            filled_rect('#2E282A', 1000-i, 0, 1, 1000)
            sleep(1/200)




    else:

        # функция для фона
        def draw_day():
            fill("#FFFFFF")
            filled_rect("#000000", 0, 0, 1000, 180)
            filled_rect("#FFFFFF", 0, 0, 1000, 179)


        # функция для крыши
        def draw_roof():
            roof_number = random.randint(0, 1)
            if roof_number == 0:
                roof_x = house_x
                roof_y = house_y
                roof_rad = house_width // 2
                filled_circle("#000000", roof_x, roof_y, roof_rad)
                filled_circle("#FFFFFF", roof_x, roof_y, roof_rad-1.5)
            elif roof_number == 1:
                roof_x = house_x - (house_width // 2)
                roof_y = house_y
                roof_height = random.randint(30, 45)
                filled_polygon("#000000", roof_x, roof_y, house_x, (roof_y - roof_height),
                                (roof_x + house_width), roof_y)
                filled_polygon("#FFFFFF", roof_x+4, roof_y, house_x, (roof_y - roof_height)+4,
                            (roof_x + house_width)-4, roof_y)

        # функция для крыши
        def draw_wall():
            wall_number = 0
            if wall_number == 0:
                wall_x = house_x - (house_width // 2)
                wall_y = house_y
                wall_width = house_width
                wall_height = 120
                filled_rect("#000000", wall_x, wall_y, wall_width, wall_height)
                filled_rect("#FFFFFF", wall_x+2, wall_y+2, wall_width-5.5, wall_height-5.5)

        # функция для окна
        def draw_window():
            window_number = random.randint(0, 1)
            if window_number == 0:
                window_x = house_x
                window_y = house_y + (wall_height // 2)
                filled_circle("#000000", window_x, window_y, (house_width // 3))
                filled_circle("#FFFFFF", window_x, window_y, (house_width // 3)-2)
                filled_circle("#000000", window_x, window_y, (house_width // 4))
                filled_circle("#FFFFFF", window_x, window_y, (house_width // 4)-2)
            elif window_number == 1:
                window_x = house_x - (house_width // 3)
                window_y = house_y + (wall_height // 3)
                filled_rect("#000000", window_x, window_y, (house_width * 5 // 9), (wall_height * 5 // 9))
                filled_rect("#FFFFFF", window_x+2, window_y+2, (house_width * 5 // 9)-5, (wall_height * 5 // 9)-5)

        # функция для всего дома
        def draw_house():
                house_or_not = random.randint(2, 4)
                if house_or_not == 0 or house_or_not == 1:
                    draw_tree()
                else:
                    draw_roof()
                    draw_wall()
                    draw_window()

        # вывод домов на экран
        draw_day()
        for row in range (250, 1200, 200):
            house_x = -75
            house_y = row
            for x_in_row in range (0, 10):
                between_houses = random.randint(100, 120)
                house_x += between_houses
                draw_house()
                sleep(1/40)
                house_width = random.randint(90, 110)

        filled_circle("#000000", 800, 60, 50)
        filled_circle("#FFFFFF", 820, 60, 40)


        sleep(10)
