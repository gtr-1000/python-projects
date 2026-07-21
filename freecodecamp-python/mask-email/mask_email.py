def mask_email(email: str) -> str:
    """Mask the local part of an email address, keeping only the first
    and last character visible.

    >>> mask_email("apple.pie@example.com")
    'a*******e@example.com'
    >>> mask_email("info@test.dev")
    'i**o@test.dev'
    """
    local_part, domain = email.split("@")

    first_char = local_part[0]
    last_char = local_part[-1]
    middle_mask = "*" * (len(local_part) - 2)

    return f"{first_char}{middle_mask}{last_char}@{domain}"


if __name__ == "__main__":
    email = "freecodecamp@example.com"
    print(mask_email(email))
