# -*- coding: utf-8 -*-

from wow_acc import api


def test():
    _ = api


if __name__ == "__main__":
    from wow_acc.tests import run_cov_test

    run_cov_test(__file__, "wow_acc.api", preview=False)
