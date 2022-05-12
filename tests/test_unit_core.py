from beerlog.core import add_beer_to_database, get_beers_from_database


def test_add_beer_to_database():
    assert add_beer_to_database("Blue Moon", "Witbier", 10, 3, 6)


# o ideal eh ter apenas um assert
def test_get_beers_from_database():
    """
    Teste AAA:
        Faço meus arranjos, atuo e verifico se deu certo a atuação
    """
    # -> Arrange
    assert add_beer_to_database("Blue Moon", "Witbier", 10, 3, 6)
    # -> Act
    results = get_beers_from_database()
    # -> Assert
    assert len(results) > 0
