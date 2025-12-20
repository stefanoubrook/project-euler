class Card:
    def __init__(self, card_string: str):
        rank_char = card_string[0]
        self.suit = card_string[1]

        rank_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        if rank_char in rank_map:
            self.rank = rank_map[rank_char]
        else:
            self.rank = int(rank_char)

    def __lt__(self, other: "Card") -> bool:
        return self.rank < other.rank

    def __repr__(self):
        return f"Card({self.rank},{self.suit})"


class Hand:
    def __init__(self, cards: list[Card]):
        self.cards = cards
        self.cards.sort(reverse=True)

    def __repr__(self):
        return f"Hand({self.cards})"

    def _get_score(self) -> tuple[int, ...]:
        # Checks if hand is a flush
        suits = {card.suit for card in self.cards}
        flush = len(suits) == 1
        # Checks for straight
        ranks = [card.rank for card in self.cards]
        unique_ranks = set(ranks)
        straight = (len(unique_ranks) == 5) and (max(ranks) - min(ranks) == 4)
        # Checks longest 'of a kind' including pair and sets highest kind
        of_a_kind = {r: 0 for r in range(2, 15)}
        for card in self.cards:
            of_a_kind[card.rank] += 1
        sorted_of_a_kind = sorted(
            of_a_kind.items(), key=lambda x: (x[1], x[0]), reverse=True
        )
        best_rank, best_count = sorted_of_a_kind[0]
        second_rank, second_count = sorted_of_a_kind[1]
        # Straight Flush
        if flush and straight:
            return (9, self.cards[0].rank)
        # 4 of a kind
        elif best_count == 4:
            return (
                8,
                best_rank,
                *[card.rank for card in self.cards if card.rank != best_rank],
            )
        # Full house
        elif best_count == 3 and second_count == 2:
            return (7, best_rank, second_rank)
        # Flush
        elif flush:
            return (6, *[card.rank for card in self.cards])
        # Straight
        elif straight:
            return (5, self.cards[0].rank)
        # 3 of a kind
        elif best_count == 3:
            remaining_cards3: list[int] = []
            for card in self.cards:
                if card.rank != best_rank:
                    remaining_cards3.append(card.rank)
            return (4, *remaining_cards3)
        # 2 pair
        elif best_count == 2 and second_count == 2:
            return (
                3,
                best_rank,
                second_rank,
                *[
                    card.rank
                    for card in self.cards
                    if (card.rank != best_rank and card.rank != second_rank)
                ],
            )
        # pair
        elif best_count == 2:
            return (
                2,
                best_rank,
                *[card.rank for card in self.cards if card.rank != best_rank],
            )
        else:
            return (1, *ranks)

    def __gt__(self, other):
        rank1 = self._get_score()
        rank2 = other._get_score()
        return rank1 > rank2


def solve(games: list[tuple[Hand, Hand]]) -> int:
    solution = 0
    for i in range(len(games)):
        if i < 5:
            print(f"Hand {i}:")
            print(f"  P1: {games[i][0].cards} -> {games[i][0]._get_score()}")
            print(f"  P2: {games[i][1].cards} -> {games[i][1]._get_score()}")
            print(f"  P1 Wins? {games[i][0]._get_score() > games[i][1]._get_score()}")
            print("-" * 20)
        if games[i][0] > games[i][1]:
            solution += 1
    return solution


def hands_loader(path: str) -> list[list[str]]:
    with open(path, "r") as f:
        data: str = f.read()
        # creates list of lists of cards
        card_game: list[list[str]] = [line.split() for line in data.splitlines()]
        return card_game


def games_to_hands(games_str: list[list[str]]) -> list[tuple[Hand, Hand]]:
    games = []
    for i in range(len(games_str)):
        hand_1 = Hand([Card(x) for x in games_str[i][:5]])
        hand_2 = Hand([Card(x) for x in games_str[i][5:]])
        games.append((hand_1, hand_2))
    return games


if __name__ == "__main__":
    print(solve(games_to_hands(hands_loader("inputs/054_poker.txt"))))
