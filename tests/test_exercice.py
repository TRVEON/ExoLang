import pytest 
from python.exercices.exercice import *

@pytest.mark.parametrize("n, expected",[
    (0,"even"),
    (1,"odd"),
    (5,"odd"),
    (10,"even"),
])
def test_even_odd(n, expected):
    #Arrange

    #Act
    result = even_odd(n)

    #Assert
    assert result == expected


@pytest.mark.parametrize("n, expected",[
    (3,"fizz"),
    (5,"buzz"),
    (15,"fizzbuzz"),
])
def test_fizz_buzz(n, expected):
    #Arrange

    #Act
    result = fizz_buzz(n)

    #Assert
    assert result == expected


@pytest.mark.parametrize("n, expected",[
    (0,0),
    (1,1),
    (2,1),
    (3,2),
    (4,3),
    (5,5),
    (6,8),
    (7,13),
    (8,21),
    (9,34),
    (10,55),
])
def test_fibonacci(n, expected):
    #Arrange

    #Act
    result = fibonacci(n)

    #Assert
    assert result == expected


@pytest.mark.parametrize("word, expected",[
    ("hello",5),
    ("world",5),
    ("python",6),
    ("exercice",8),
])
def test_calcul_length(word, expected):
    #Arrange

    #Act
    result = calcul_length(word)
    #Assert
    assert result == expected

@pytest.mark.parametrize("list, expected",[
    ([1,2,3,4,5],[1,2,3,4,5]),
    ([5,4,3,2,1],[1,2,3,4,5]),
    ([1,3,2,5,4],[1,2,3,4,5]),
    ([1,2,3,5,4],[1,2,3,4,5]),
])
def test_sort(list, expected):
    #Arrange

    #Act
    result = sort(list)

    #Assert
    assert result == expected
