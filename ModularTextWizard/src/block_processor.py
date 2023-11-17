from functools import reduce


def block_processor(text, *blocks):
    return reduce(lambda processed_text, block: block(processed_text), blocks, text)
