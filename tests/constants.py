# -*- coding: utf-8 -*-

from dataset import ds


# fmt: off
class AccountEnum:
    acc1 = ds.accounts["acc1"]
    acc2 = ds.accounts["acc2"]


class RealmEnum:
    acc1_realm1 = ds.accounts["acc1"].realms_mapper["realm1"]
    acc1_realm2 = ds.accounts["acc1"].realms_mapper["realm2"]
    acc2_realm1 = ds.accounts["acc2"].realms_mapper["realm1"]
    acc2_realm2 = ds.accounts["acc2"].realms_mapper["realm2"]


class CharacterEnum:
    acc1_realm1_char111 = ds.accounts["acc1"].realms_mapper["realm1"].characters_mapper["char111"]
    acc1_realm1_char112 = ds.accounts["acc1"].realms_mapper["realm1"].characters_mapper["char112"]
    acc1_realm2_char121 = ds.accounts["acc1"].realms_mapper["realm2"].characters_mapper["char121"]
    acc1_realm2_char122 = ds.accounts["acc1"].realms_mapper["realm2"].characters_mapper["char122"]
    acc2_realm1_char211 = ds.accounts["acc2"].realms_mapper["realm1"].characters_mapper["char211"]
    acc2_realm1_char212 = ds.accounts["acc2"].realms_mapper["realm1"].characters_mapper["char212"]
    acc2_realm2_char221 = ds.accounts["acc2"].realms_mapper["realm2"].characters_mapper["char221"]
    acc2_realm2_char222 = ds.accounts["acc2"].realms_mapper["realm2"].characters_mapper["char222"]
# fmt: on