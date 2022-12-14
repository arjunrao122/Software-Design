from pathlib import Path
from importlib import import_module


def get_all_blocks():
    blocks = set(files.stem for files in Path.glob(Path.cwd() / 'src', "*.py"))
    
    to_delete = ['get_processed_text', 'block_processor', 'load_modules', 'get_all_blocks']
    blocks.difference_update(to_delete)

    return set(map(lambda block: import_module("." + block, __package__).__getattribute__(block.lower()), blocks))
