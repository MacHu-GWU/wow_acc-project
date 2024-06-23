.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.1 (2024-06-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release
- Add the following public API:
    - :class:`Account <wow_acc.model.Account>`
    - :meth:`Account.sort_key <wow_acc.model.Account.sort_key>`
    - :meth:`Account.realms_mapper <wow_acc.model.Account.realms_mapper>`
    - :meth:`Account.characters <wow_acc.model.Account.characters>`
    - :meth:`Account.wtf_account_name <wow_acc.model.Account.wtf_account_name>`
    - :class:`Realm <wow_acc.model.Realm>`
    - :meth:`Realm.sort_key <wow_acc.model.Realm.sort_key>`
    - :meth:`Realm.account_name <wow_acc.model.Realm.account_name>`
    - :meth:`Realm.characters_mapper <wow_acc.model.Realm.characters_mapper>`
    - :class:`Character <wow_acc.model.Character>`
    - :meth:`Character.sort_key <wow_acc.model.Character.sort_key>`
    - :meth:`Character.var_name <wow_acc.model.Character.var_name>`
    - :meth:`Character.realm_name <wow_acc.model.Character.realm_name>`
    - :meth:`Character.account <wow_acc.model.Character.account>`
    - :meth:`Character.account_name <wow_acc.model.Character.account_name>`
    - :meth:`Character.titled_character_name <wow_acc.model.Character.titled_character_name>`
    - :class:`Dataset <wow_acc.model.Dataset>`
    - :meth:`Dataset.from_yaml <wow_acc.model.Dataset.from_yaml>`
    - :meth:`Dataset.to_module <wow_acc.model.Dataset.to_module>`
