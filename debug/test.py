# -*- coding: utf-8 -*-

from pathlib import Path
from wow_acc.model import Database

p = Path(__file__).absolute().parent.parent.joinpath("tests", "test.yml")
db = Database.from_yaml(p)


# fmt: off
class AccountEnum:
    acc1 = db.accounts["acc1"]
    acc2 = db.accounts["acc2"]


class RealmEnum:
    realm1 = db.accounts["acc1"].realms_mapper["realm1"]
    realm2 = db.accounts["acc1"].realms_mapper["realm2"]


class CharacterEnum:
    acc1_realm1_char111 = db.accounts["acc1"].realms_mapper["realm1"].characters_mapper["char111"]
    acc1_realm1_char112 = db.accounts["acc1"].realms_mapper["realm1"].characters_mapper["char112"]
    acc1_realm2_char121 = db.accounts["acc1"].realms_mapper["realm2"].characters_mapper["char121"]
    acc1_realm2_char122 = db.accounts["acc1"].realms_mapper["realm2"].characters_mapper["char122"]
    acc2_realm1_char111 = db.accounts["acc2"].realms_mapper["realm1"].characters_mapper["char211"]
    acc2_realm1_char112 = db.accounts["acc2"].realms_mapper["realm1"].characters_mapper["char212"]
    acc2_realm2_char121 = db.accounts["acc2"].realms_mapper["realm2"].characters_mapper["char221"]
    acc2_realm2_char122 = db.accounts["acc2"].realms_mapper["realm2"].characters_mapper["char222"]
# fmt: on
