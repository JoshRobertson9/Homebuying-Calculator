# Existing Modules
import pytest
import os

# My Modules
import home_functions as hf


# Mortgage Rate Calc Tests
def test_misc_value():
    assert round(hf.mortgage_rate_calc(400_000, 80_000, 6, 30),2) == 1918.56


def test_zero_interst():
    assert round(hf.mortgage_rate_calc(400_000, 80_000, 0.00000000, 30),2) == 888.89

