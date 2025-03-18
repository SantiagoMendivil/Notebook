"""Scoping our Functions"""
import random

# No parameters, No Return Value


def print_hello() -> None:
    print("Hello World!")

# Parameters, No Return Value


def print_name(name: str) -> None:
    print(f"Hello {name}!")


# No parameters, Return Value


def get_random_number() -> int:
    return random.randint(1, 10)


# Parameters, Return Value


def calc_sale_price(amount: float, member: bool) -> float:
    if member:
        amount = amount - (amount * 0.15)
    else:
        amount = amount - (amount * 0.05)
    amount = round(amount, 2)
    return amount
