import random
from math import sqrt
import time
import numpy as np


class StudentTest:
    def __init__(self, compare1, compare2, arg_first=(), arg_two=()):
        self.param_list = (compare1, compare2)
        self.data = [[], []]
        self.m_list = []
        self.sd_list = []
        self.n = None
        self.text_list = {0: [], 1: []}
        self.args = {0: arg_first, 1: arg_two}

    def get_sd(self, param: list):
        m = sum(param) / len(param)
        print(f'm = {round(m, 5)}')
        self.m_list.append(m)
        dis = sum(list(map(lambda x: pow((x - m), 2), param))) / (len(param) - 1)
        sd = sqrt(dis)
        if sd < 1 / (10 * 6):
            print(f'sd = {round(sd, 6) * 1000} * 10^(-3)')
            print()
        else:
            print(f'sd = {round(sd, 6)}')
            print()
        self.sd_list.append(sd)
        return sd

    def time_test(self, it, arg=None):
        fun = self.param_list[0]
        start = time.perf_counter()
        if arg:
            for i in range(it):
                fun(arg)
        else:
            for i in range(it):
                fun()
        stop = time.perf_counter()
        print(f'Время работы функции {stop - start} секунд при {it} итерациях')

    def get_se(self):
        se = sqrt((self.sd_list[0] * self.sd_list[0]) / self.n + (self.sd_list[1] * self.sd_list[1]) / self.n)
        return se

    def get_t(self):
        s_m = sorted(self.m_list)
        t = (s_m[1] - s_m[0]) / self.get_se()
        return t

    def test(self, it, num_fun: int):
        print(f'Тест начался для {self.param_list[num_fun].__name__} функции')
        print()
        fun = self.param_list[num_fun]
        arg = self.args[num_fun]
        if arg:
            start = time.perf_counter()
            for _ in range(it):
                fun(*arg)
            stop = time.perf_counter()
            self.data[num_fun].append(round(stop - start, 5))
            self.text_list[num_fun].append(round(stop - start, 5))
        else:
            start = time.perf_counter()
            for _ in range(it):
                fun()
            stop = time.perf_counter()
            self.data[num_fun].append(round(stop - start, 5))
            self.text_list[num_fun].append(round(stop - start, 5))

    def start_test(self, it_wi_test, itr=5):
        self.n = itr
        prc = 0
        for it in range(itr):
            print(f'Выполнено {prc}%')
            print('**********************************')
            for num in range(2):
                self.test(it_wi_test, num)
            prc += 100 / itr
        print(f'Выполнено {prc}%')
        print('_____________________')
        for n, data in enumerate(self.data):
            print(f'Значения для {self.param_list[n].__name__}')
            self.get_sd(data)
        print()
        print('_____________________________________')
        m0, m1 = self.m_list
        if m0 < m1:
            print(
                f'{self.param_list[0].__name__} быстрее {self.param_list[1].__name__} в {round(m1, 6) / round(m0, 6)} раз')
        else:
            print(
                f'{self.param_list[1].__name__} быстрее {self.param_list[0].__name__} в {round(m0, 6) / round(m1, 6)} раз')
        print('----------------------------------------------------')
        print(f'Время работы функции {self.param_list[0].__name__} при {it_wi_test} итерациях')
        for n, i in enumerate(self.text_list[0]):
            print(f'{n + 1}) {i}')
        print('___________________________________________')
        print(f'Время работы функции {self.param_list[1].__name__} при {it_wi_test} итерациях')
        for n, i in enumerate(self.text_list[1]):
            print(f'{n + 1}) {i}')
        print("Среднее время работы:")
        for f in range(2):
            print(f'{self.param_list[f].__name__}: {round(self.m_list[f], 5)}')
        self.get_se()
        dif = round((self.m_list[0] - self.m_list[1]), 5)
        if dif < 1:
            print(f'{round((self.m_list[0] - self.m_list[1]) * 1000, 5)} * 10^(-3) - разница между средними значениями')
        else:
            print(f'{round((self.m_list[0] - self.m_list[1]), 5)} - разница между средними значениями')
        print("T-value = ", round(self.get_t(), 5))


def random_ch():
    lst = [1, 2, 3, 4]
    x = random.choice(lst)
    return x


def random_num():
    num = random.random()
    if num <= 0.5:
        return 0
    elif 0.5 < num < 0.75:
        return 1
    elif 0.75 < num < 0.9:
        return 2
    else:
        return 3


test = StudentTest(random_ch, random_num, False, False)
test.start_test(100000)
