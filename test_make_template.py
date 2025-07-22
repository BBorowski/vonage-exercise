#!/usr/bin/python3

import pytest
from itertools import zip_longest

from make_template import main

testdata= [
    ["tests/1_test_input", "tests/1_test_output"],
    ["tests/2_test_input", "tests/2_test_output"],
    ["tests/3_test_input", "tests/3_test_output"],
    ["tests/4_test_input", "tests/4_test_output"]]

def file_compare(actual_output, expected_output):
    with open(actual_output, mode="r") as actual_output,\
         open(expected_output, mode="r") as test_output:
        for line1, line2 in zip_longest(actual_output, test_output):
            if line1 != line2:
                return False
        return True

@pytest.mark.parametrize("test_input, expected_output", testdata)
def test_main(test_input, expected_output):
    main(test_input)
    assert file_compare("Dockerfile", expected_output)
