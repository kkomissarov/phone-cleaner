from unittest import TestCase
from main import normalize_phone


class NormalizePhoneTest(TestCase):
    def test_startswith_zero(self):
        phone = '0282768'
        self.assertEqual(normalize_phone(phone), None)

    def test_long_phone(self):
        phone = '792116782928282768'
        self.assertEqual(normalize_phone(phone), None)

    def test_error_code(self):
        phone = '88126531239'
        self.assertEqual(normalize_phone(phone), None)

    def test_seven_chars(self):
        phone = '6531239'
        self.assertEqual(normalize_phone(phone), '78126531239')

    def test_ten_chars(self):
        phone = '8126531239'
        self.assertEqual(normalize_phone(phone), '78126531239')

    def test_full_phone(self):
        phone = '78126531239'
        self.assertEqual(normalize_phone(phone), '78126531239')
