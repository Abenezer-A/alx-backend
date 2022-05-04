#!/usr/bin/env python3
""" return tuple"""


def index_range(page: int, page_size: int) -> tuple:
    mytuple = ((page - 1) * page_size, page * page_size)
    return mytuple
