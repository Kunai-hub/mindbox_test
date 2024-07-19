# -*- coding: utf-8 -*-
import math
from unittest import TestCase


def area_circle(radius):
    """Вычисляет площадь круга по радиусу.

    :param radius: Радиус круга в единицах.
    :return: Площадь круга в квадратных единицах.
    """

    return math.pi * radius ** 2


def area_triangle(a, b, c):
    """Вычисляет площадь треугольника по трем сторонам.

    :param a: Первая сторона треугольника в единицах.
    :param b: Вторая сторона треугольника в единицах.
    :param c: Третья сторона треугольника в единицах.
    :return: Площадь треугольника в квадратных единицах.
    """

    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))


def area_figure(figure_type, *args):
    """Вычисляет площадь фигуры по типу фигуры и переданным аргументам.

    :param figure_type: Тип фигуры (например, "круг", "треугольник").
    :param args: *args: Аргументы, необходимые для вычисления площади.
    :return: Площадь фигуры в квадратных единицах.
    """

    if figure_type == 'круг':
        return area_circle(*args)
    elif figure_type == 'треугольник':
        return area_triangle(*args)
    else:
        raise ValueError(f'Неподдерживаемый тип фигуры: {figure_type}')


def is_right_triangle(*args):
    """Проверяет, является ли треугольник прямоугольным.

    :param args: *args: Аргументы, необходимые для вычисления площади.
    :return: True, если треугольник прямоугольный, иначе False.
    """

    a, b, c = sorted(args)
    return a > 0 and a ** 2 + b ** 2 == c ** 2


class TestArea(TestCase):
    """
    Класс для тестов.
    """

    def test_area_circle(self):
        self.assertEqual(area_circle(5), 78.53981633974483)

    def test_area_triangle(self):
        self.assertEqual(area_triangle(3, 4, 5), 6.0)

    def test_area_figure_circle(self):
        self.assertEqual(area_figure('круг', 5), 78.53981633974483)

    def test_area_figure_triangle(self):
        self.assertEqual(area_figure('треугольник', 3, 4, 5), 6.0)

    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(5, 4, 3))
        self.assertFalse(is_right_triangle(3, 5, 5))

# Легкость добавления других фигур.


def area_square(side):
    return side ** 2


def area_figure_v2(figure_type, *args):
    if figure_type == 'круг':
        return area_circle(*args)
    elif figure_type == 'треугольник':
        return area_triangle(*args)
    elif figure_type == 'квадрат':
        return area_square(*args)
    else:
        raise ValueError(f'Неподдерживаемый тип фигуры: {figure_type}')
