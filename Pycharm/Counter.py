from bs4 import BeautifulSoup

from Pycharm.HTTPResponse import HTTPRequest


class Company:
    """
    Stores information about a company
    Contains: Name, Sector, Company Code, Company Number
    """
    def __init__(self):
        self.name = ""
        self.sector = ""
        self.code = ""
        self.number = ""
        self.market = ""
        self.company_dict = dict()

    def set_attribute(self, attr):
        self.name = attr.get("Name")
        self.sector = attr.get("Sector")
        self.code = attr.get("Code")
        self.number = attr.get("Number")
        self.market = attr.get("Market")
        self.company_dict = attr


    def __repr__(self):
        return "Name   : {}\n" \
               "Sector : {}\n" \
               "Code   : {}\n" \
               "Number : {}\n" \
               "Market : {}\n" \
            .format(self.name, self.sector, self.code, self.number, self.market)

    def get_company_info(self):
        return self.company_dict


class Financial:
    def __init__(self):
        self.market_cap = ""
        self.share_count = ""
        self.EPS = ""
        self.PERatio = ""
        self.ROE = ""
        self.financial_dict = dict()

    def set_attribute(self, attr):
        self.market_cap = attr.get("Mktcap")
        self.share_count = attr.get("Share_count")
        self.EPS = attr.get("EPS")
        self.PERatio = attr.get("PERatio")
        self.ROE = attr.get("ROE")
        self.financial_dict = attr

    def __repr__ (self):
        return "Market Cap  : {}\n" \
               "Share Count : {}\n" \
               "EPS         : {}\n" \
               "PE Ratio    : {}\n" \
               "ROE         : {}\n" \
            .format(self.market_cap, self.share_count, self.EPS, self.PERatio, self.ROE)

    def get_financial_info(self):
        return self.financial_dict


class Counter:
    COUNTER_URL = "https://www.malaysiastock.biz/Corporate-Infomation.aspx?securityCode="

    def __init__(self, counter_number):
        self.company = Company()
        self.financial = Financial()
        self.counter_number = counter_number
        self.response = self.get_page()
        self.page_content = BeautifulSoup(self.response.content, "html.parser")  # Creates BeautifulSoup Object
        self.process_counter()
        self.process_financial()

    # Get the page of the URL
    def get_page(self):
        http_request = HTTPRequest(self.COUNTER_URL + self.counter_number)
        response = http_request.get_response()
        return response




    # Extracts information of a company from page
    def process_counter(self):
        company_info = dict()

        company_name = self.page_content.find(id="ctl13_lbCorporateName").text   # Finds company name
        company_info.update({"Name": company_name[2:].upper()})              # Removes ": " from the string

        company_sector = self.page_content.find(id="ctl13_lbSector").text
        company_info.update({"Sector": company_sector[2:].upper()})

        counter_code = self.page_content.find(id="ctl13_lbSymbolCode").text
        company_info.update({"Code": counter_code[2:].upper()})

        market = self.page_content.find(id="ctl13_lbMarket").text
        company_info.update({"Market": market[2:].upper()})

        company_info.update({"Number": self.counter_number})

        self.company.set_attribute(company_info)

    def process_financial(self):
        financial_info = dict()

        market_cap = self.page_content.find(id="MainContent_lbFinancialInfo_Capital").text
        financial_info.update({"Mktcap": market_cap[2:]})

        share_count = self.page_content.find(id="MainContent_lbNumberOfShare").text
        financial_info.update({"Share_count": share_count[2:]})

        eps = self.page_content.find(id="MainContent_lbFinancialInfo_EPS").text
        financial_info.update({"EPS": eps[2:]})

        pe_ratio = self.page_content.find(id="MainContent_lbFinancialInfo_PE").text
        financial_info.update({"PERatio": pe_ratio[2:]})

        roe = self.page_content.find(id="MainContent_lbFinancialInfo_ROE").text
        financial_info.update({"ROE": roe[2:]})

        self.financial.set_attribute(financial_info)


    # Prints Company information
    def print_company_info(self):
        print("Company Info")
        print(self.company)


    # Prints Counter Financial information
    def print_financial_info(self):
        print("Financial Info")
        print(self.financial)

    def get_company_info(self):
        return self.company.get_company_info()


    def get_company_financial(self):
        return self.financial.get_financial_info()

if __name__ == "__main__":
    print("\n")
    new_counter = Counter("0156")
    new_counter.print_company_info()
    new_counter.print_financial_info()
    print(new_counter.get_company_info())
    print(new_counter.get_company_financial())