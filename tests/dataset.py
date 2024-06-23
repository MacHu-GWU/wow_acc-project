# -*- coding: utf-8 -*-

from pathlib import Path
from wow_acc.api import Dataset

dir_here = Path(__file__).absolute().parent
ds = Dataset.from_yaml(dir_here.joinpath("test.yml"))
