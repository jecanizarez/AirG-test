import csv
from typing import List

new_content = []


def normalize_row(row: List, quote_char: str) -> List:
    for i, field in enumerate(row):
        if '"' in field:
            field = f'{quote_char}{field}{quote_char}'
        if ',' in field:
            field = f'{quote_char}{field}{quote_char}'
        row[i] = field
    return row


def read_csv(filename: str, delimiter: str = '|', quote_char: str = '"'):
    with open(f"{filename}.csv", "r") as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quote_char)
        for row in reader:
            new_content.append(normalize_row(row=row, quote_char=quote_char))


def write_csv(filename: str, new_delimiter: str = '|', quote_char: str = '"'):
    with open(f"{filename}.csv", "w") as f:
        writer = csv.writer(f, delimiter=new_delimiter, quotechar=quote_char, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(new_content)


if __name__ == "__main__":
    filename = input("Please type filename: ").replace(".csv", "")
    new_delimiter_in = input("Please type csv new delimiter, default: | ") or "|"
    new_quote_char = input('Please type new quote character, default: " ') or '"'
    read_csv(filename=filename)
    write_csv(filename=filename, new_delimiter=new_delimiter_in, quote_char=new_quote_char)