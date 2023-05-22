from pytest import approx
from shadow.polyedr import Polyedr


class TestPerimetr:

    def test_1(self):
        a = Polyedr(f"data/test0.geom", 1)
        a.draw(None, 1)
        assert a.sum == approx(1.0)

    def test_2(self):
        a = Polyedr(f"data/test1.geom", 1)
        a.draw(None, 1)
        assert a.sum == approx(6.0)

    def test_3(self):
        a = Polyedr(f"data/test2.geom", 1)
        a.draw(None, 1)
        assert a.sum == approx(22.0)
