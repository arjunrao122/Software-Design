from src.get_all_blocks import get_all_blocks # pragma: no cover
from src.block_processor import block_processor # pragma: no cover


def main(): # pragma: no cover
    print("Available blocks are:")

    available_blocks = get_all_blocks()

    for block_name in available_blocks:
        print(block_name.__name__ + "\n", end="")

    number_of_blocks = int(input("Choose number of blocks:"))

    blocks = []

    for number in range(number_of_blocks):
        print("Specify blocks to be used in order: ")
        block = input(f'Specify block {number+1}: ')
        blocks.append(block)

    input_text = input("Enter text to be processed: ")

    user_blocks = []

    for block_name in available_blocks:
        if block_name.__name__ in blocks:
            user_blocks.append(block_name)

    print(block_processor(input_text, *user_blocks))


main()  # pragma: no cover

