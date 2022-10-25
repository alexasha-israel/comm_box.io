import urllib.request
import aggregator
import matcher
from helper import FILE_NAME, URL, AMOUNT_OF_ROWS


def main():

    get_text_file()
    process_file(FILE_NAME)

def get_text_file():
    urllib.request.urlretrieve(URL, filename=FILE_NAME)

def process_file(file_name: str, lines_per_block: int = AMOUNT_OF_ROWS):
    lines_in_block = 0
    block_line_offset = 0
    line_index = 0
    block = ""
    results = dict()
    with open(file_name) as f:
        # This treats f as iterable object
        for line in f:
            line_index += 1
            lines_in_block += 1
            block += line
            if lines_in_block >= lines_per_block:
                aggregator.aggregate(block_line_offset, block, matcher.match(block), results)
                # Reset the block, next block starts from the next line
                block_line_offset = line_index
                lines_in_block = 0
                block = ""

    # Process the last block
    if lines_in_block > 0:
        data = "\n".join(block)
        aggregator.aggregate(block_line_offset, data, matcher.match(data), results)

    aggregator.do_print(results)


if __name__ == "__main__":
    main()
