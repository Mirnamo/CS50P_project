from project import game1, game2

def test_game1():

    assert game1("rock") != "you win"
    assert game1("paper") != "you lose"

def test_game2():

    assert game2("1") != "Wrong answer"
    assert game2("2") != "Good job!"