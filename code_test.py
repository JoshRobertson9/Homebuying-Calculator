# Existing Modules
#import pytest
#import os
from decimal import Decimal
import subprocess

# My Modules
import home_functions as hf


# Mortgage Rate Calc Tests
def test_misc_value():
    assert round(hf.mortgage_rate_calc(400_000, 80_000, 6, 30), 2) == Decimal(1_918.56)


def test_zero_interest():
    assert round(hf.mortgage_rate_calc(400_000, 80_000, 0.00000000, 30),2) == 888.89


def test_zero_loan():
    assert round(hf.mortgage_rate_calc(400_000, 400_000, 6, 30),2) == 0


def test_zero_term():
    assert round(hf.mortgage_rate_calc(400_000, 80_000, 6, 0),2) == Decimal(320_000.00)


if __name__ == "__main__":
    subprocess.run(["pytest", "--no-header", "-vv"])


