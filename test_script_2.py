import csv
import os

import pytest

from script_2 import generate_csv

test_data = [("test_1", 12), ("test_2", 1000), ("test_3", 10000)]


@pytest.mark.parametrize("filename, n_rows", test_data)
def test_generate_csv(filename, n_rows):
    generate_csv(filename=filename, rows_limit=n_rows)
    with open(f"{filename}.csv", "r") as f:
        file = csv.reader(f, delimiter=",", quotechar="|")
        assert sum(1 for row in file) == n_rows
        os.remove(f"{filename}.csv")
