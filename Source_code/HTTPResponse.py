import requests


class HTTPRequest:
    """
    Author: Jen Pin Wong
    A Class that request a HTML based on a URL
    """
    def __init__(self, url):
        self.url = url

    # Get HTML file from the URL
    def get_response(self):
        print("Getting response from {}".format(self.url))

        try:
            response = requests.get(self.url)
            if response.status_code != 200:
                print("Error Status Code {}".format(response.status_code))
            else:
                print("Successfully Retrieve URL\n")
            return response

        except requests.exceptions.MissingSchema:
            print("\nInvalid URL (Missing Schema)")
            print("Try Adding \"https\"/\"http\"...")





