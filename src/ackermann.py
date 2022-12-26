def Astart(x: int, z: int) -> int:
    if z == 1:
        return x
    elif z == 2:
        return 0
    else:
        return 1


def A(x: int, y: int, z: int) -> int:
    if z == 1:
        return y + x
    elif z == 2:
        return y * x
    elif z == 3:
        return x**y
    elif y > 0 and z > 0:
        return A(x, A(x, y - 1, z), z - 1)
    elif z == 0:
        return y + 1
    else:
        assert y == 0
        return Astart(x, z)
