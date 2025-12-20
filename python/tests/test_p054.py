from solutions.p054 import games_to_hands


def test_easy():
    games = games_to_hands(
        [["AD", "KD", "QD", "JD", "TD", "2S", "5D", "7D", "9H", "TH"]]
    )
    assert games[0][0] > games[0][1]
