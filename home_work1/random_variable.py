import datetime
import math
import psutil

def random_number():
    a = str(datetime.datetime.now().timestamp() * 1000000)
    c = math.pi % 1
    m = 34536253534535
    s = psutil.cpu_times().user
    e = float(a[::-1])
    s = (e * s + c) % m / 10000
    print(s)


if __name__ == '__main__':
    random_number()

