# Card Counting Assistant — Python

Three versions of the same Blackjack card counter, going beyond a direct translation of the JavaScript version to demonstrate idiomatic Python and compare approaches — the same spirit as the `switch` vs array comparison in the JS version.

## The three files

- **`card_counter_match.py`** — simple function, global `count`, uses `match`/`case`. The most direct Python equivalent of the original exercise.
- **`card_counter_sets.py`** — same structure, but groups cards using `set` + `in` instead of `match`. The Python equivalent of the JS array + `.includes()` version.
- **`card_counter.py`** — a more complete, "production-style" rewrite: encapsulates `count` in a class and adds an interactive input loop with validation. See below for details.

## `match` / `case` vs `set` + `in`

Python's `match` statement (available from Python 3.10) is the closest equivalent to JS's `switch`. Instead of stacking multiple `case` labels without a `break` to group values (JS's fallthrough), Python groups them directly with `|` (or):

```python
match normalized:
    case 2 | 3 | 4 | 5 | 6:
        count += 1
    case 10 | "J" | "Q" | "K" | "A":
        count -= 1
```

The `set` + `in` version instead defines the groups as data and asks "does this value belong to this group?":

```python
LOW_CARDS = {2, 3, 4, 5, 6}
HIGH_CARDS = {10, "J", "Q", "K", "A"}

if normalized in LOW_CARDS:
    count += 1
elif normalized in HIGH_CARDS:
    count -= 1
```

**Why `set` and not `list` here?** A `set` is Python's idiomatic choice when you only care about membership ("is this value in the group?"), not order or duplicates. Checking `in` on a `set` is also faster than on a `list` for larger groups, since sets use hashing internally instead of scanning item by item. A `list` would work too (`[2, 3, 4, 5, 6]`), but `set` communicates the intent more precisely.

## `card_counter.py` — a class instead of a global variable

The original exercise stores `count` as a global variable, which any part of the program can read or overwrite unexpectedly — a common source of bugs as a codebase grows. Here, `count` is an instance attribute of a `CardCounter` class: each `CardCounter()` you create keeps its own independent, protected count.

```python
counter = CardCounter()
counter.add_card(5)   # "1 Bet"
counter.add_card("K") # "0 Hold"
```

**An interactive input loop**

Instead of hardcoding a handful of test calls, the script reads cards from the user one at a time via `input()`, until they type `quit`. Since `input()` always returns a string, `parse_card()` converts numeric strings to `int` and normalizes face cards to uppercase before they reach the counter.

**Basic input validation**

An invalid card (anything that isn't 2-10, J, Q, K, or A) raises a `ValueError` with a clear message, caught in the main loop and printed without crashing the program — so a typo doesn't end the session.

## Usage

```
$ python card_counter.py
Enter cards one at a time (2-10, J, Q, K, A). Type 'quit' to stop.
Card: 5
1 Bet
Card: k
0 Hold
Card: quit
```

## Takeaway

The counting logic (which cards raise, lower, or leave the count unchanged) is identical across all three files. What changes is the design: `match` vs `set` membership for comparing values, and a global variable vs an encapsulated class for holding state. All are valid — the class-based version with an input loop is the one that reads most like a small real tool rather than an exercise.
