import math

def mercator_ufa():

    # координаты Уфы в градусах, минутах и секундах
    latitude_d = 54
    latitude_m = 44
    latitude_s = 35

    longitude_d = 55
    longitude_m = 58
    longitude_s = 4

    # переводим в десятичные градусы
    latitude = latitude_d + latitude_m / 60 + latitude_s / 3600
    longitude = longitude_d + longitude_m / 60 + longitude_s / 3600

    print('Широта в градусах:', round(latitude, 3))
    print('Долгота в градусах:', round(longitude,3))

    # радиус Земли в метрах
    r = 6378137.0

    # перевод в Меркатор
    x = r * longitude * math.pi / 180
    y = r * math.log(math.tan(math.pi / 4 + latitude * math.pi / 360))

    print('Меркатор X = ' + str(round(x,3)) + " м")
    print('Меркатор Y = ' + str(round(y,3)) + " м")

def main():
    mercator_ufa()

if __name__ == '__main__':
    main()