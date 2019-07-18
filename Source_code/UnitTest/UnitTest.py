from Source_code.HTTPResponse import HTTPRequest
from Source_code.Counter import Counter
from Source_code.Database import Database

import unittest
import os


class UnitTest(unittest.TestCase):
    """
    Unit Test for HTTPResponse.py
    """
    URL = "https://www.google.com"

    def test_get_response(self):
        request1 = HTTPRequest(self.URL)
        self.assertTrue(request1.get_response())


class TestCounter(unittest.TestCase):
    """
    Unit Test for Counter.py
    """
    test_counter = Counter("6947")

    def test_get_page(self):
        self.assertTrue(self.test_counter.get_page())

    def test_process_company_info(self):
        self.assertDictEqual(self.test_counter.company.get_company_info(), {})
        self.test_counter.process_company_info()
        self.assertTrue(self.test_counter.company.get_company_info())

    def test_process_financial_info(self):
        self.assertDictEqual(self.test_counter.financial.get_financial_info(), {})
        self.test_counter.process_financial_info()
        self.assertTrue(self.test_counter.financial.get_financial_info())

    def test_process_price_info(self):
        self.assertDictEqual(self.test_counter.price.get_price_info(), {})
        self.test_counter.process_price_info()
        self.assertTrue(self.test_counter.price.get_price_info())


class TestDatabase(unittest.TestCase):
    """
    Unit Test for Database.py
    """
    def test_write_to_database(self):
        if os.path.exists("output_files/test_database.csv"):
            os.remove("output_files/test_database.csv")

        data = []
        test_counter = Counter("6947")
        test_counter.process_price_info()

        data.append(test_counter.get_price_info())

        Database.write_to_database("output_files/test_database.csv", data)
        self.assertTrue(os.path.exists("output_files/test_database.csv"))
        self.assertTrue(os.stat("output_files/test_database.csv").st_size != 0)



if __name__ == "__main__":
    unittest.main()