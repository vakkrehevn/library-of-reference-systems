import math


def GetCCS2PCS(X, Y, Z, O1_x=0.0, O1_y=0.0, R=10.0, P1=0.0):
    """
    Преобразует декартовы координаты (X, Y, Z) в параметрические (P, Q, Z).

    Параметры:
    X, Y, Z - декартовы координаты точки велосипедиста
    O1_x, O1_y - координаты центра окружности внутренней кривой (по умолчанию 0,0)
    R - радиус внутренней кривой (по умолчанию 10)
    P1 - длина прямого участка трека до начала кривой (2H на схеме, по умолчанию 0)

    Возвращает:
    (P, Q, Z) - параметрические координаты
    """

    M1_x, M1_y = X, Y

    dx = M1_x - O1_x
    dy = M1_y - O1_y
    dist_O1M1 = math.hypot(dx, dy)

    if dist_O1M1 == 0:
        L_x, L_y = O1_x + R, O1_y
    else:
        L_x = O1_x + R * dx / dist_O1M1
        L_y = O1_y + R * dy / dist_O1M1

    M2L = abs(dist_O1M1 - R)
    Q = math.hypot(Z, M2L)

    phi = math.atan2(L_y - O1_y, L_x - O1_x)

    if phi < 0:
        phi += 2 * math.pi

    P2 = R * phi
    P = P1 + P2

    return (P, Q, Z)