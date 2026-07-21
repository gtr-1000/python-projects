class CardCounter:
    """Tracks a running Blackjack card count and advises Bet or Hold.

    Encapsulating `count` as an instance attribute (instead of a global
    variable) means each CardCounter has its own independent count, and
    nothing outside the class can accidentally overwrite it.
    """

    def __init__(self) -> None:
        self.count = 0

    def add_card(self, card: int | str) -> str:
        """Update the running count based on the given card, and return
        the current count and decision as a string, e.g. '-3 Hold'.
        """
        normalized = self._normalize(card)

        match normalized:
            case 2 | 3 | 4 | 5 | 6:
                self.count += 1
            case 7 | 8 | 9:
                pass
            case 10 | "J" | "Q" | "K" | "A":
                self.count -= 1
            case _:
                raise ValueError(f"Invalid card: {card!r}")

        return self.decision()

    def decision(self) -> str:
        status = "Bet" if self.count > 0 else "Hold"
        return f"{self.count} {status}"

    @staticmethod
    def _normalize(card: int | str) -> int | str:
        if isinstance(card, str):
            return card.strip().upper()
        return card


def parse_card(raw: str) -> int | str:
    """Convert user input (always a string) into a number or a face-card
    string, the same shape the exercise expects `card` to arrive as.
    """
    raw = raw.strip()
    return int(raw) if raw.isdigit() else raw.upper()


if __name__ == "__main__":
    counter = CardCounter()
    print("Enter cards one at a time (2-10, J, Q, K, A). Type 'quit' to stop.")

    while True:
        raw_input_value = input("Card: ")
        if raw_input_value.strip().lower() == "quit":
            break

        try:
            card = parse_card(raw_input_value)
            print(counter.add_card(card))
        except ValueError as error:
            print(error)
