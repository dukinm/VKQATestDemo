import pytest

# Негативный тест на ошибку деления на 0
def test_float_zero_division():
    try:
        assert float(0) / 0
    except ZeroDivisionError:
        pass


def test_float_sum():
    assert float(1) + float(1) == float(2)


def test_float_division():
    assert float(12) / float(4) == float(3)


def test_set_issubset():
    assert {'gopher'}.issubset({'dog', 'gopher'}) == True


def test_set_pop():
    animals = {'dog', 'gopher'}
    animals.pop()
    assert animals == {'gopher'} or animals == {'dog'}

# Тест с параметрами, используем два множества, чтобы убедиться, что результат не зависит от набора данных
@pytest.mark.parametrize(
    "test_set, set_data",
    [
        ("animals", {'dog', 'gopher'}),
        ("planets", {'Venus', 'Earth'}),
    ]
)
def test_set_difference(test_set, set_data):
    new_set = {}
    difference = {}
    if test_set == "animals":
        new_set = {'cat', 'dog'}
        difference = {'cat'}
    if test_set == "planets":
        new_set = {'Venus', 'Mars'}
        difference = {'Mars'}
    assert new_set.difference(set_data) == difference
