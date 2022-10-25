from typing import Any, Mapping, Sequence


def aggregate(block_line_offset: int, data: str, matches: Mapping[str, int], results: Mapping[str, Any]):
    # Input needs to be broken into individual strings so that we can figure our their lengths
    block_lines = data.split("\n")
    block_lines = [x + "\n" for x in block_lines]
    # Now, we take the matches dictionary and sort individual values per index
    sorted_matches = sorted(matches.items(), key=lambda x: x[1])
    # Now, we will walk the block lines and the matches
    total_length = 0
    line_index = -1
    for match, offset in sorted_matches:
        while total_length < offset:
            line_index += 1
            total_length += len(block_lines[line_index])
        # Now we found the line which contained the match: add it to the results
        # Note that we need to account for offset within a BIG data string
        # needing to be converted to an offset *WITHIN* a matching line
        item = [block_line_offset + line_index, offset - total_length + len(block_lines[line_index])]
        if match in results:
            results[match].append(item)
        else:
            results[match] = [item]


def do_print(results: Mapping[str, Sequence[Sequence[int]]]):
    for word in results:
        print("{} ->:".format(word))
        first = True
        block = ""
        for offset in results[word]:
            if first:
                block += "[[lineOffset={}, charOffset={}]".format(offset[0], offset[1])
            else:
                block += ", [lineOffset={}, charOffset={}]".format(offset[0], offset[1])
            first = False
        print("{}]\n".format(block))


