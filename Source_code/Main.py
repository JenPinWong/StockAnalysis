from Counter import Counter
from Filter import Filter
from Database import Database

import time

# Location for files storing data of counters for each sectors (Files are stored in CounterInfo/)
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

# Constants
SHARE_PRICE = "share_price"
COUNTER_INFO = "counter_info"
REQUEST_INTERVAL = 0


class Main:
    """
    Author: Jen Pin Wong
    A Main Class that will harvest data from a stock website (malaysiastock.biz)
    Counters harvested are those stored in a file
    Returns data harvested in a form of dictionary or prints the data
    """
    # Filters a file to get only the code (number) of each counter
    @staticmethod
    def filter_counters(filename):
        counters_code = Filter(filename)
        counters = counters_code.filter_counters()
        return counters

    # Prints all information (Company and financial info) of a counter
    def print_all_data(self, filename, data_type):
        counter_codes = self.filter_counters(filename)
        for code in counter_codes:
            # Load each counter with 1.5 second to not overload web server
            time.sleep(REQUEST_INTERVAL)

            counter = Counter(code)

            # Harvest Counter share price if data requested == share price
            if data_type == SHARE_PRICE:
                # Process Data
                counter.process_price_info()

                # Print Data
                counter.print_price_info()

            # Harvest Counter Info if data requested == counter info
            elif data_type == COUNTER_INFO:
                # Process Data
                counter.process_company_info()
                counter.process_financial_info()

                # Print Data
                counter.print_company_info()
                counter.print_financial_info()

        print("{} counters found".format(len(counter_codes)))

    # Gets all data of a company in a dictionary format
    def get_all_data(self, filename, data_type):
        # Get all codes of counters from given file
        counter_codes = self.filter_counters(filename)
        counter_data = []

        for code in counter_codes:
            # Load each counter with x seconds to not overload web server
            time.sleep(REQUEST_INTERVAL)

            # Initialize counter
            counter = Counter(code)

            # Checks if the counter still exists
            if not counter.counter_exist():
                continue

            # Harvest Counter share price if data requested == share price
            if data_type == SHARE_PRICE:
                # Prepare Data
                counter.process_price_info()

                # Hash Table of share price data
                price_data = counter.get_price_info()

                counter_data.append(price_data)

            # Harvest Counter Info if data requested == counter info
            elif data_type == COUNTER_INFO:
                # Prepare Data
                counter.process_company_info()
                counter.process_financial_info()

                # Hash Table of company info and financial info
                merged_data = {**counter.get_company_info(), **counter.get_company_financial()}

                counter_data.append(merged_data)

        return counter_data

    # Harvest data from a website based on data type
    def harvest(self, sector_list, data_type):
        counter_count = 0

        for sector in sector_list:
            if data_type == SHARE_PRICE:
                data = self.get_all_data(sector, SHARE_PRICE)
                counter_count += len(data)
                Database.write_to_database("../Data/{}_price_database.csv".format(sector.split('/')[-1][:-4]), data)

            elif data_type == COUNTER_INFO:
                data = self.get_all_data(sector, COUNTER_INFO)
                counter_count += len(data)
                Database.write_to_database("../Data/counter_database.csv", data)

        print("Total counters found = {}".format(counter_count))


if __name__ == "__main__":
    market = Main()
    sectors = [TECHNOLOGY, FINANCIAL, TELECOM, HEALTHCARE, PLANTATION, PROPERTY, LOGISTICS, ENERGY, REALESTATE, GAS]

    start = time.time()
    market.harvest(sectors, SHARE_PRICE)
    end = time.time()

    print("Total time taken: {}".format(end - start))
