# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models.amount import Amount
from yookassa.domain.models.currency import Currency
from yookassa.domain.models.transfer import Transfer


class TestTransfer(unittest.TestCase):

    def test_receipt_cast(self):
        self.maxDiff = None
        transfer = Transfer()
        transfer.account_id = '79990000000'
        transfer.amount = Amount({
            "value": '100.01',
            "currency": Currency.RUB
        })

        self.assertEqual({
            'account_id': '79990000000',
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            }
        }, dict(transfer))

        self.assertEqual('79990000000', transfer.account_id)

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(transfer.amount))
        self.assertEqual(float(transfer.amount.value), 100.01)

        with self.assertRaises(TypeError):
            transfer.amount = 'invalid type'
