# -*- coding: utf-8 -*-
from db import db

class Transaction(object):

    def __init__(self, tx):
        self.tx = tx

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_type is not None:
            self.rollback()
        self.commit()

    def rollback(self):
        self.tx.rollback()
        self.tx.close()

    def commit(self):
        self.tx.commit()
        self.tx.close()

class TxManager(object):

    def __init__(self, engine):
        self.engine = engine

    def begin(self):
        return Transaction(self.engine)

tx_manager = TxManager(db.session)

def transaction_wrapper(func):
    def wrapper(*args, **kwargs):
        with tx_manager.begin() as tx:
            return func(*args, **kwargs)
    return wrapper
