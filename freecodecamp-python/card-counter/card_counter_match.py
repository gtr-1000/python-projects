count = 0


def normalize(card: int | str) -> int | str:
    if isinstance(card, str):
        return card.strip().upper()
    return card


def card_counter(card: int | str) -> str:
    global count

    normalized = normalize(card)

    match normalized:
        case 2 | 3 | 4 | 5 | 6:
            count += 1
        case 7 | 8 | 9:
            pass
        case 10 | "J" | "Q" | "K" | "A":
            count -= 1

    status = "Bet" if count > 0 else "Hold"
    return f"{count} {status}"


if __name__ == "__main__":
    print(card_counter(5))
    print(card_counter("k"))
    print(card_counter(10))
