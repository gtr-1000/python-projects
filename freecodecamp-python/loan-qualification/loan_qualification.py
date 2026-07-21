TIERS = [
    {
        "min_income": 60000,
        "min_credit_score": 700,
        "message": "You qualify for a duplex, condo, and car loan.",
    },
    {
        "min_income": 45000,
        "min_credit_score": 680,
        "message": "You qualify for a condo and car loan.",
    },
    {
        "min_income": 30000,
        "min_credit_score": 650,
        "message": "You qualify for a car loan.",
    },
]


def get_loan_message(annual_income: float, credit_score: int) -> str:
    """Return a message describing which loans the person qualifies for,
    based on the strictest tier they meet.

    >>> get_loan_message(85000, 850)
    'You qualify for a duplex, condo, and car loan.'
    >>> get_loan_message(25000, 550)
    "You don't qualify for any loans."
    """
    for tier in TIERS:
        if annual_income >= tier["min_income"] and credit_score >= tier["min_credit_score"]:
            return tier["message"]

    return "You don't qualify for any loans."


if __name__ == "__main__":
    print(get_loan_message(85000, 850))
    print(get_loan_message(65000, 690))
    print(get_loan_message(45000, 660))
    print(get_loan_message(25000, 550))
