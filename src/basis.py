def code(xs: list[int], basis: int) -> int:
    r = 0
    for x in xs:
        r *= basis
        r += x
    return r


def decode(r: int, basis: int) -> list[int]:
    xs = []
    while r > 0:
        rem = r % basis
        if rem == 0:
            rem = basis
            r //= basis
            r -= 1
        else:
            r //= basis
        xs.append(rem)
    return list(reversed(xs))
