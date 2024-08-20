# -*- coding=utf-8 -*-
from rich import print


def test(a, b, c=0):
    """
    this is doc string
    multilint doc string
    """
    print(f"{a=}, {b=}, {c=}")


def main():
    test(a=1, b=2, c=3)
    a, b, c = 1, 1, 1
    test(b, b, b)
    test(c=c, b=b, a=a)
    # print(test(doc))
    print(test.__doc__)


if __name__ == "__main__":
    main()
