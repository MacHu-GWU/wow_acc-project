# -*- coding: utf-8 -*-

from pathlib import Path
from wow_acc.api import Dataset

dir_here = Path(__file__).absolute().parent
ds = Dataset.from_yaml(dir_here.joinpath("dataset.yml"))

if __name__ == "__main__":
    path = dir_here.joinpath("constants.py")
    content = ds.to_module(
        import_line="from dataset import ds",
    )
    path.write_text(content)
