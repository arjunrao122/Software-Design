from src.block_processor import block_processor
from src.get_all_blocks import get_all_blocks


def run_text_processor():
    blocks = list(get_all_blocks())
    for i, block in enumerate(blocks, 1):
        print(f"{i}. {block.__name__}")

    choice_indices = map(int, input("Select blocks by number (separated by commas): ").split(','))
    selected_blocks = [blocks[i - 1] for i in choice_indices]

    text = input("Enter text: ")
    print("Processed Text:", block_processor(text, *selected_blocks))


if __name__ == "__main__":
    run_text_processor()
