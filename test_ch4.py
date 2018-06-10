import ch4


class TestRouting:
    a = ch4.DirectedNode('a')
    b = a.add_next('b')
    # notice c is not attached to d
    c = a.add_next('c')
    d = b.add_next('d')

    def test_is_directed_route_two_hops(cls):
        assert ch4.is_directed_route(cls.a, cls.d)

    def test_is_no_directed_route(cls):
        assert not ch4.is_directed_route(cls.d, cls.a)

    def test_is_route_either_way(cls):
        assert ch4.is_route_either_way(cls.a, cls.d)

    def test_is_no_route_either_way_going_one_way_the_whole_time(cls):
        assert not ch4.is_route_either_way(cls.b, cls.c)
        assert not ch4.is_route_either_way(cls.d, cls.c)

