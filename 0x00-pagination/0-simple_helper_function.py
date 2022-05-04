#!/usr/bin/env python3
""" return tuple"""

def index_range(page: int, page_size: int) -> tuple: 
    """ define index_range"""
    mytuple = ((page - 1) * page_size, page * page_size)
    """ assigning mytuple"""
    return mytuple 
    """return mytuple"""
