# -*- coding: utf-8 -*-

"""
本模块定义了 :class:`Account`, :class:`Realm`, :class:`Character` 三个配置应用场景类.

.. note::

    注意, 这里的类都带有一个 ``def new()`` 的工厂函数, 请不要直接用构造器, 而用这个工厂函数.
    里面会自动把新建的对象加入到父对象的映射中去.
"""

import typing as T
import dataclasses
from pathlib import Path
from functools import cached_property
from .vendor.better_dataclasses import DataClass, T_DATA

import yaml


def right_zfill(s: str, length: int) -> str:
    """
    fill character "0" to the right end to ensure a string has a fixed length.
    """
    return s + "0" * (length - len(s))


def to_var_name(s: str) -> str:
    """
    Convert a string to a valid variable name.
    """
    return s.replace("-", "_").replace(" ", "_")


@dataclasses.dataclass(frozen=True, eq=True, order=True)
class Account(DataClass):
    """
    代表着一个具体账号. 是可哈希, 可排序, 可用集合去重的.

    :param account: 账号名.
    :param realms: 该账号下的所有 :class:`Realm` 对象的列表.
    """

    account: str = dataclasses.field()
    realms: T.List["Realm"] = dataclasses.field(default_factory=list)

    @property
    def sort_key(self) -> str:
        """
        创建账号的排序键. 本质是左对齐并在尾部添加 "0" 的字符串.
        """
        return right_zfill(self.account, 16)

    def __hash__(self):
        """
        判断账号是否相同的哈希函数.
        """
        return hash(self.sort_key)

    @property
    def var_name(self) -> str:
        """
        Variable name for generated Python module.
        """
        return to_var_name(self.account)

    @cached_property
    def realms_mapper(self) -> T.Dict[str, "Realm"]:
        """
        返回该账号下的所有服务器从名字到对象的映射.
        """
        return {realm.realm: realm for realm in self.realms}

    @cached_property
    def characters(self) -> T.List["Character"]:
        """
        返回该账号下所有服务器上的所有角色.
        """
        chars = list()
        for realm in self.realms:
            for character in realm.characters:
                chars.append(character)
        return chars

    @property
    def wtf_account_name(self) -> str:
        r"""
        返回账号名的全部大写形式. 用于 WTF 文件夹中的路径名. 例如:

        ``C:\...\WTF\Account\MYACCOUNT\...``
        """
        return self.account.upper()


@dataclasses.dataclass(frozen=True, eq=True, order=True)
class Realm(DataClass):
    """
    代表着一个具体账号下的具体的服务器. 是可哈希, 可排序, 可用集合去重的.

    :param account: 该服务器所属的 :class:`Account` 对象.
    :param realm: 服务器名.
    :param characters: 该服务器下的所有 :class:`Character` 的列表.
    """

    account: Account = dataclasses.field()
    realm: str = dataclasses.field()
    characters: T.List["Character"] = dataclasses.field(default_factory=list)

    @property
    def sort_key(self) -> str:
        """
        服务器名排序键. 本质是先对账号排序, 再对服务器名排序. 和账号的排序键一样, 也是左对齐
        并在尾部添加 "0" 的字符串.
        """
        return ".".join(
            [
                self.account.sort_key,
                right_zfill(self.realm, 16),
            ]
        )

    def __hash__(self):
        """
        判断服务器是否相同的哈希函数.
        """
        return hash(self.sort_key)

    @property
    def var_name(self) -> str:
        """
        Variable name for generated Python module.
        """
        return f"{self.account.var_name}_{to_var_name(self.realm)}"

    @property
    def account_name(self) -> str:
        """
        该服务器所属的账号名.
        """
        return self.account.account

    @property
    def characters_mapper(self) -> T.Dict[str, "Character"]:
        """
        返回该账号下的所有游戏角色从名字到对象的映射.
        """
        return {char.character: char for char in self.characters}


@dataclasses.dataclass(frozen=True, eq=True, order=True)
class Character(DataClass):
    """
    代表着一个具体账号下的具体的服务器上的具体游戏角色. 是可哈希, 可排序, 可用集合去重的.

    :param realm: 该角色所属的 :class:`Realm` 对象.
    :param character: 角色名.
    """

    realm: Realm = dataclasses.field()
    character: str = dataclasses.field()

    @property
    def sort_key(self) -> str:
        """
        角色名排序键. 本质是先对服务器排序, 再对角色名排序. 和服务器的排序键一样, 也是左对齐
        并在尾部添加 "0" 的字符串.
        """
        return ".".join(
            [
                self.realm.sort_key,
                right_zfill(self.character, 16),
            ]
        )

    def __hash__(self):
        """
        判断角色是否相同的哈希函数.
        """
        return hash(self.sort_key)

    @property
    def var_name(self) -> str:
        """
        Variable name for generated Python module.
        """
        return f"{self.realm.var_name}_{to_var_name(self.character)}"

    @property
    def realm_name(self) -> str:
        """
        该角色所属的服务器名.
        """
        return self.realm.realm

    @property
    def account(self) -> Account:
        """
        该角色所属的账号对象.
        """
        return self.realm.account

    @property
    def account_name(self) -> str:
        """
        该角色所属的账号名.
        """
        return self.account.account

    @property
    def titled_character_name(self) -> str:
        r"""
        角色名的首字母大写形式. 例如 "mycharacter" -> "Mycharacter". 用于
        WTF 文件夹中的路径名. 例如:

        ``C:\...\WTF\Account\MYACCOUNT\MyServer\Mycharacter\...``
        """
        return self.character[0].upper() + self.character[1:].lower()


@dataclasses.dataclass(frozen=True)
class Dataset(DataClass):
    """
    代表着一堆 :class:`Account`, :class:`Realm`, :class:`Character` 的集合.
    """

    accounts: T.Dict[str, Account] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_yaml(cls, stream: T.Union[str, Path]):
        """
        Sample YAML file format:

        .. code-block:: yaml

            acc1:
              realm1:
                - char111
                - char112
              realm2:
                - char121
                - char122
            acc2:
              realm1:
                - char211
                - char212
              realm2:
                - char221
                - char222
        """
        if isinstance(stream, str):  # pragma: no cover
            data = yaml.load(stream, Loader=yaml.SafeLoader)
        elif isinstance(stream, Path):
            with stream.open() as f:
                data = yaml.load(f, Loader=yaml.SafeLoader)
        else:  # pragma: no cover
            raise TypeError

        accounts = dict()
        for account_name, account_data in data.items():
            account = Account(account=account_name)
            for realm_name, character_name_list in account_data.items():
                realm = Realm(account=account, realm=realm_name)
                for character_name in character_name_list:
                    character = Character(realm=realm, character=character_name)
                    realm.characters.append(character)
                account.realms.append(realm)
            accounts[account.account] = account
        return cls(accounts=accounts)

    def to_module(
        self,
        import_line: str,
        dataset_var_name: str = "ds",
    ) -> str:
        """
        Generate python code that can be used to enumerate this dataset.

        :param import_line: this line will be used to import the :class:`Dataset` object,
            usually it is ``from .dataset import ds``
        :param dataset_var_name: the variable name of the :class:`Dataset` object,
            usually it is ``ds``.
        """
        lines = [
            "# -*- coding: utf-8 -*-",
            "",
            import_line,
            "",
            "",
            "# fmt: off",
            "class AccountEnum:",
        ]
        tab = " " * 4
        for account_name, account in self.accounts.items():
            lines.append(
                f'{tab}{account.var_name} = {dataset_var_name}.accounts["{account_name}"]'
            )

        lines.append("")
        lines.append("")
        lines.append("class RealmEnum:")
        for account_name, account in self.accounts.items():
            for realm_name, realm in account.realms_mapper.items():
                lines.append(
                    f'{tab}{realm.var_name} = {dataset_var_name}.accounts["{account_name}"].realms_mapper["{realm_name}"]'
                )

        lines.append("")
        lines.append("")
        lines.append("class CharacterEnum:")
        for account_name, account in self.accounts.items():
            for realm_name, realm in account.realms_mapper.items():
                for character_name, character in realm.characters_mapper.items():
                    lines.append(
                        f'{tab}{character.var_name} = {dataset_var_name}.accounts["{account_name}"].realms_mapper["{realm_name}"].characters_mapper["{character_name}"]'
                    )
        lines.append("# fmt: on")

        return "\n".join(lines)
