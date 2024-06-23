What is This
==============================================================================
这个库是一个用 Python 对象来描述 World of Warcraft 账户的库. 它允许你将账户信息保存在一个 `YAML <https://yaml.org/>`_ 格式的文件中, 然后用 Python 来将数据读到内存中, 最后自动创建一个 enum 的脚本, 里面有着对所有的 Account, Realm, Character 的引用, 使得你在其他模块中可以方便的利用 IDE 的自动补全对其进行引用.

下面这是一个 YAML 文件的例子. 里面定义了 2 个 Account, 2 个 Realm, 一共 8 个 Character.

.. dropdown:: tests/dataset.yml

    .. literalinclude:: ../../../tests/dataset.yml
       :language: yaml
       :linenos:

下面这个模块可以将上面的 YAML 文件读取到内存中. 作为模块使用, ``if __name__ == "__main__":`` 以外的代码可以被 import. 作为脚本使用, 它能生成一个 enum 的模块.

.. dropdown:: tests/dataset.py

    .. literalinclude:: ../../../tests/dataset.py
       :language: python
       :linenos:

下面就是生成的 enum 模块. 你可以在其他模块中引用这个模块, 然后使用 IDE 的自动补全来引用其中的 Account, Realm, Character. 并且每当你修改了 YAML 文件后, 你可以轻松地重新生成这个 enum 模块.

.. dropdown:: tests/constants.py

    .. literalinclude:: ../../../tests/constants.py
       :language: python
       :linenos:
