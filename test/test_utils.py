from topo.cogo import Point, acimut_dist, gms  # pyright: ignore[reportMissingImports]


def test_punto() -> None:
    A1 = Point(100, 200, "cam")
    assert Point(100, 200, "cam") == A1
    return


def test_gms() -> None:
    assert gms(39.51) == "039-30-36"
    return


def test_acimut() -> None:
    p191 = Point(1061912.027, 862535.415)
    p192 = Point(1061608.151, 862535.214)

    assert acimut_dist(p191, p192) == ('269-57-44', 303.8761)
    return
