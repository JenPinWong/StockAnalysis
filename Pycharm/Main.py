from Pycharm.Counter import Counter
from Pycharm.HTTPResponse import HTTPRequest
from bs4 import BeautifulSoup
from Pycharm.Filter import Filter
from Pycharm.Database import Database

import time

URL = "https://www.malaysiastock.biz/Listed-Companies.aspx?type=S&s1=17"


TECHNOLOGY = "counter_info/technology.txt"
HEALTHCARE = "counter_info/healthcare.txt"
FINANCIAL = "counter_info/financial.txt"
PLANTATION = "counter_info/plantation.txt"
PROPERTY = "counter_info/property.txt"
TELECOM = "counter_info/telecom.txt"
LOGISTICS = "counter_info/logistics.txt"

class Main:
    def __init__(self):
        self.counter_array = []
        # self.response = self.get_page()
        # self.page_content = BeautifulSoup(self.response.content, "html.parser")
        # print(self.page_content)

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
            merged_data = {**counter.get_company_info(), **counter.get_company_financial()}
            counter_data.append(merged_data)

        return counter_data


if __name__ == "__main__":
    new = Main()
    sectors = [PROPERTY, TELECOM, LOGISTICS]

    start = time.time()
    counter_count = 0
    for sector in sectors:
        data = new.get_all_data(sector)
        counter_count += len(data)
        Database.write_to_database("Counter_database.csv", data)

    end = time.time()
    print("Total time taken: {}".format(end - start))
    print("Total counters found = {}".format(counter_count))