from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/ 

def test_chance():
        actual = Yatzy.chance(1, 2, 3, 4, 5)
        expected = 15
        assert actual == expected

def test_yatzy_sameNumber():
        assert 50 == Yatzy.yatzy([4,4,4,4,4])
        assert 50 == Yatzy.yatzy([6,6,6,6,6])

def test_yatzy_oneDiferentNumber():
        assert 0 == Yatzy.yatzy([4,4,4,4,5])
        assert 0 == Yatzy.yatzy([6,6,6,6,3])

def test_ones_atLeastOne():
        numbers = [1,2,1,3,4]
        expected = 2
        actual = Yatzy.ones(*numbers)
        assert actual == expected

def test_ones_noOne():
        numbers = [2,2,4,3,4]
        expected = 0
        actual = Yatzy.ones(*numbers)
        assert actual == expected

def test_twoPair():
        


