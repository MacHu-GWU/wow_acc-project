# -*- coding: utf-8 -*-

from pathlib import Path
from wow_acc.model import (
    Account,
    Realm,
    Character,
    Dataset,
)


dir_here = Path(__file__).absolute().parent


class Test:
    @classmethod
    def setup_class(cls):
        ds = Dataset.from_yaml(dir_here.joinpath("dataset.yml"))
        cls.ds = ds

        # fmt: off
        cls.acc1 = ds.accounts["acc1"]
        cls.acc2 = ds.accounts["acc2"]
        cls.acc1_realm1 = ds.accounts["acc1"].realms_mapper["realm1"]
        cls.acc1_realm2 = ds.accounts["acc1"].realms_mapper["realm2"]
        cls.acc2_realm1 = ds.accounts["acc2"].realms_mapper["realm1"]
        cls.acc2_realm2 = ds.accounts["acc2"].realms_mapper["realm2"]
        cls.acc1_realm1_char111 = ds.accounts["acc1"].realms_mapper["realm1"].characters_mapper["char111"]
        cls.acc1_realm1_char112 = ds.accounts["acc1"].realms_mapper["realm1"].characters_mapper["char112"]
        cls.acc1_realm2_char121 = ds.accounts["acc1"].realms_mapper["realm2"].characters_mapper["char121"]
        cls.acc1_realm2_char122 = ds.accounts["acc1"].realms_mapper["realm2"].characters_mapper["char122"]
        cls.acc2_realm1_char111 = ds.accounts["acc2"].realms_mapper["realm1"].characters_mapper["char211"]
        cls.acc2_realm1_char112 = ds.accounts["acc2"].realms_mapper["realm1"].characters_mapper["char212"]
        cls.acc2_realm2_char121 = ds.accounts["acc2"].realms_mapper["realm2"].characters_mapper["char221"]
        cls.acc2_realm2_char122 = ds.accounts["acc2"].realms_mapper["realm2"].characters_mapper["char222"]
        # fmt: on

    def test_hash_and_comparison(self):
        st = {self.acc1, self.acc2, self.acc1, self.acc2}
        assert len(st) == 2  # hashable, can fit into set
        assert self.acc1 < self.acc2
        assert self.acc1 == self.acc1
        assert self.acc1 != self.acc2

        st = {
            self.acc1_realm1,
            self.acc1_realm2,
            self.acc2_realm1,
            self.acc2_realm2,
        }
        assert len(st) == 4
        st1 = st & st
        assert len(st1) == 4
        assert self.acc1_realm1 < self.acc1_realm2
        assert self.acc1_realm1 == self.acc1_realm1
        assert self.acc1_realm1 != self.acc1_realm2

        st = {
            self.acc1_realm1_char111,
            self.acc1_realm1_char112,
            self.acc1_realm2_char121,
            self.acc1_realm2_char122,
            self.acc2_realm1_char111,
            self.acc2_realm1_char112,
            self.acc2_realm2_char121,
            self.acc2_realm2_char122,
        }
        assert len(st) == 8
        st1 = st & st
        assert len(st1) == 8
        assert self.acc1_realm1_char111 < self.acc1_realm1_char112
        assert self.acc1_realm1_char111 == self.acc1_realm1_char111
        assert self.acc1_realm1_char111 != self.acc1_realm1_char112

    def test_attributes(self):
        assert len(self.acc1.sort_key) == 16
        assert len(self.acc1.realms_mapper) == 2
        assert self.acc1.realms == [self.acc1_realm1, self.acc1_realm2]
        assert len(self.acc1.characters) == 4
        assert self.acc1.wtf_account_name == "ACC1"

        assert len(self.acc1_realm1.sort_key) == 33  # 16*2+1
        assert len(self.acc1_realm1.characters_mapper) == 2
        assert self.acc1_realm1.account_name == self.acc1.account
        assert self.acc1_realm1.characters == [
            self.acc1_realm1_char111,
            self.acc1_realm1_char112,
        ]

        assert len(self.acc1_realm1_char111.sort_key) == 50  # 16*3+2
        assert self.acc1_realm1_char111.account_name == self.acc1.account
        assert self.acc1_realm1_char111.realm_name == self.acc1_realm1.realm
        assert self.acc1_realm1_char111.titled_character_name == "Char111"

    def test_to_module(self):
        path = dir_here.joinpath("constants.py")
        path.unlink(missing_ok=True)
        content = self.ds.to_module(
            import_line="from dataset import ds",
        )
        path.write_text(content)

        from constants import AccountEnum, RealmEnum, CharacterEnum

        for k, v in AccountEnum.__dict__.items():
            if not k.startswith("_"):
                assert isinstance(v, Account)

        for k, v in RealmEnum.__dict__.items():
            if not k.startswith("_"):
                assert isinstance(v, Realm)

        for k, v in CharacterEnum.__dict__.items():
            if not k.startswith("_"):
                assert isinstance(v, Character)


if __name__ == "__main__":
    from wow_acc.tests import run_cov_test

    run_cov_test(__file__, "wow_acc.model", preview=False)
