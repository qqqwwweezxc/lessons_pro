from bank_account import BankAccount
import pytest

@pytest.fixture
def account():
    return BankAccount(100)


@pytest.mark.parametrize(
    "amount, expected",
    [
        (50, 150),
        (100, 200),
        (0.5, 100.5),
    ],
)
def test_deposit(account, amount, expected):
    account.deposit(amount)
    assert account.get_balance() == expected


@pytest.mark.parametrize(
    "amount, expected",
    [
        (50, 50),
        (30, 70),
    ],
)
def test_withdraw(account, amount, expected):
    account.withdraw(amount)
    assert account.get_balance() == expected


def test_withdraw_insufficient(account):
    with pytest.raises(ValueError):
        account.withdraw(1000)


def test_withdraw_skip_if_empty():
    acc = BankAccount(0)

    if acc.get_balance() == 0:
        pytest.skip("Account is empty")

    acc.withdraw(10)
