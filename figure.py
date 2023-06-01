"""
figure 모듈은 도형과 관련된 클래스 및 함수를 제공합니다.

line 클래스를 활용하여 선의 길이를 설정, 참조하며
width와 height를 매개변수로 받는
area_rectangle, area_ellipse, area_right_triangle 함수를 통해
너비와 높이에 따른 직사각형, 타원, 직각삼각형의 넓이를 반환합니다.
"""
import math

class line:
    """
    line 클래스는 선의 길이들을 저장합니다.
    외부에서 접근 불가한 필드  __width와 __height가 있으며,
    해당 필드에 수정하고 접근하기 위해
    set_length, get_length 메소드를 제공합니다.
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        """
        생성자 초기 width 값과 height 값을 받습니다.
        Args:
            width (int or float): 초기 선의 가로 길이
            height (int or float): 초기 선의 세로 길이
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """
        객체가 저장하고 있는 선의 길이를 수정합니다.
        Args:
            width (int or float): 수정하고자 하는 가로 길이
            height (int or float): 수정하고자 하는 세로 길이
        """
        self.__width = width
        self.__height = height

    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이를 반환합니다.
        Returns:
            int or float: 저장하고 있는 선의 길이
        """
        return self.__width, self.__height

def area_rectangle(width, height):
    """
    width와 height를 입력받아
    width * height인 직사각형의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 밑변의 길이
        height (int or float): 높이의 길이
    Returns:
        int or float: 직사각형의 넓이
    """
    if width <= 0 or height <= 0:
        raise ValueError

    return width * height

def area_ellipse(width, height):
    """
    width와 height를 입력받아
    width * height * pi인 타원의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 짧은 쪽 반지름 길이
        height (int or float): 긴 쪽 반지름 길이
    Returns:
        int or float: 타원의 넓이
    """
    if width <= 0 or height <= 0:
        raise ValueError

    return width * height * math.pi

def area_right_triangle(width, height):
    """
    width와 height를 입력받아
    (width * height) / 2인 직각삼각형의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 밑변의 길이
        height (int or float): 높이의 길이
    Returns:
        int or float: 직각삼각형의 넓이
    """
    if width <= 0 or height <= 0:
        raise ValueError

    return (width * height) / 2