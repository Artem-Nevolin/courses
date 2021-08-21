def main():
    x, y = 100, 100
    width, height = 200, 200
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Нарисовать домик полной ширины  width и высоты height от опорной точки (x,y),
    которая находиться в середине нижней точки фундамента
    Parameters..---
    ----------
    x координата x середины домика
    y координата y низа фундамента
    width полная ширина домика (фундамент или вылеты крыши включены)
    height полная высота домика

    Returns None
    -------

    """

    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height
    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height, width, roof_height)
    print('Типа рисую домик ...', x, y, width, height)


def draw_house_foundation(x, y, width, height):
    """
        Нарисовать основание домика полной ширины  width и высоты height от опорной точки (x,y),
        которая находиться в середине нижней точки фундамента
        Parameters
        ----------
        x координата x середины фундамента
        y координата y низа фундамента
        width полная ширина фундамента (фундамент или вылеты крыши включены)
        height полная высота фундамента

        Returns None
        -------

        """
    print('Типа рисую основание ...', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    print('Типа рисую стены ...', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    print('Типа рисую крышу ...', x, y, width, height)
    pass


main()


