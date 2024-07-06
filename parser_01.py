

def parse_string(text: str):
    result = parse_array(0, text)
    return result


def skip_spaces(index: int, text: str):
    while text[index] in " \t\r\n":
        index += 1
    return index


def parse_array(index: int, text: str):
    i = index
    i = skip_spaces(i, text)

    if text[i] != '[':
        return None
    i += 1

    array = []
    while True:
        item, i = parse_array_item(i, text)
        if item is None:
            break
        array.append(item)

    if text[i] != ']':
        return None, index

    return array, i + 1


def parse_array_item(index: int, text: str):
    index = skip_spaces(index, text)

    if text[index] in "],":
        return None, index

    item = ""
    while text[index] not in "], ":
        item += text[index]
        index += 1

    index = skip_spaces(index, text)

    if text[index] in ",":
        index += 1

    index = skip_spaces(index, text)

    return item, index


def main():
    raw_string = "[ the, data, banana ]"
    result = parse_string(raw_string)
    print(result)

    raw_string = "[ the, data, banana, ]"
    result = parse_string(raw_string)
    print(result)


if __name__ == '__main__':
    main()
