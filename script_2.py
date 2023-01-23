import csv
import logging
import random
import string

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_values():
    filename_input = input("Please type filename: ").replace(".csv", "")
    n_rows_input = int(input("Please type number of rows: "))
    return filename_input, n_rows_input


def generate_random_string() -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))


def generate_csv(
    filename: str,
    rows_limit: int,
):
    write_row_limit = 1000  # Write n lines per batch
    write_row_limit = (
        write_row_limit if rows_limit > write_row_limit else rows_limit
    )  # Case if rows limit is lower than write limit
    with open(f"{filename}.csv", "w", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        batches = (
            rows_limit // write_row_limit
            if rows_limit % write_row_limit == 0
            else rows_limit // write_row_limit + 1
        )
        logger.info(f"Writing file in {batches} batches")
        for batch in range(batches):
            logger.info(f"Writing batch {batch + 1}")
            writer.writerows(
                [[generate_random_string()] for x in range(write_row_limit)]
            )


if __name__ == "__main__":
    filename, n_rows = init_values()
    generate_csv(filename=filename, rows_limit=n_rows)
