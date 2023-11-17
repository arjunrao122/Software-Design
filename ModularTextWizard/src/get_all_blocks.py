from pathlib import Path
from importlib import import_module


def get_all_blocks():
    block_files = Path(__file__).parent.glob("*.py")

    blocks = {file.stem for file in block_files}

    to_delete = {'get_processed_text', 'block_processor', 'load_modules', 'get_all_blocks', '__init__', 'character_blocker'}
    blocks.difference_update(to_delete)

    block_functions = set()
    for block in blocks:
        module_name = f"src.{block}"
        try:
            block_module = import_module(module_name)
            func_name = block
            block_function = getattr(block_module, func_name)
            block_functions.add(block_function)
        except AttributeError as e:
            print(f"Error: The function {func_name} is not found in the module {block}.py: {e}")
        except ImportError as e:
            print(f"Error: Could not import module {module_name}: {e}")

    return block_functions
