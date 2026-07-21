count = 0

LOW_CARDS = {2, 3, 4, 5, 6}
HIGH_CARDS = {10, "J", "Q", "K", "A"}


def normalize(card: int | str) -> int | str:
    if isinstance(card, str):
        return card.strip().upper()
    return card


def card_counter(card: int | str) -> str:
    global count

    normalized = normalize(card)

    if normalized in LOW_CARDS:
        count += 1
    elif normalized in HIGH_CARDS:
        count -= 1

    status = "Bet" if count > 0 else "Hold"
    return f"{count} {status}"


if __name__ == "__main__":
    print(card_counter(5))
    print(card_counter("k"))
    print(card_counter(10))
