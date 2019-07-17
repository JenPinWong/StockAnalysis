from Source_code.Counter import Counter
from Source_code.HTTPResponse import HTTPRequest
from Source_code.Filter import Filter
from Source_code.Database import Database

import time

URL = "https://www.malaysiastock.biz/Listed-Companies.aspx?type=S&s1=17"


TECHNOLOGY = "../Counter_info/technology.txt"
HEALTHCARE = "../Counter_info/healthcare.txt"
FINANCIAL = "../Counter_info/financial.txt"
PLANTATION = "../Counter_info/plantation.txt"
PROPERTY = "../Counter_info/property.txt"
TELECOM = "../Counter_info/telecom.txt"
LOGISTICS = "../Counter_info/logistics.txt"
ENERGY = "../Counter_info/energy.txt"
REALESTATE = "../Counter_info/realestate.txt"
GAS = "../Counter_info/gas.txt"


class Main:
    def __init__(self):
        self.counter_array = []

    # Gets the page of a URL
    @staticmethod
    def get_page():
        http_request = HTTPRequest(URL)
        response = http_request.get_response()
        return response

    # Filters a file to get only the code (number) of each counter
    @staticmethod
    def get_counters(filename):
        counters_code = Filter(filename)
        counters = counters_code.filter_counters()
        return counters

    # Prints all information (Company and financial info) of a counter
    def print_all_data(self, filename):
        counter_codes = self.get_counters(filename)
        for code in counter_codes:
            counter = Counter(code)
            counter.print_company_info()
            counter.print_financial_info()

        print("{} counters found".format(len(counter_codes)))

    # Gets all data of a company in a dictionary format
    def get_all_data(self, filename):
        counter_data = []
        counter_codes = self.get_counters(filename)
        for code in counter_codes:
            time.sleep(1.5)
            counter = Counter(code)
            counter.process_company_info()
            counter.process_financial_info()
            merged_data = {**counter.get_company_info(), **counter.get_company_financial()}
            counter_data.append(merged_data)

        return counter_data

    def get_price_data(self, filename):
        counter_data = []
        counter_codes = self.get_counters(filename)
        for code in counter_codes:
            time.sleep(1.5)
            counter = Counter(code)
            counter.process_price_info()
            price_data = counter.get_price_info()
            counter_data.append(price_data)

        return counter_data


if __name__ == "__main__":
    new = Main()
    sectors = [FINANCIAL]

    start = time.time()
    counter_count = 0
    for sector in sectors:
        data = new.get_price_data(sector)
        counter_count += len(data)
        Database.write_to_database("../Data/price_database.csv", data)

    end = time.time()
    print("Total time taken: {}".format(end - start))
    print("Total counters found = {}".format(counter_count))