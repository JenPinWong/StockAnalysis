import re


class Filter:
    """
    Author: Jen Pin Wong
    A class that will filter a .txt file to have only counter codes remaining
    """
    def __init__(self, filename):
        self.filename = filename

    # Filters a file to only keep counter codes
    def filter_counters(self):
        file = None
        try:
            file = open(self.filename)
        except IOError:
            print("Error opening file: {}".format(self.filename))

        counter_list = []

        for line in file:
            line = re.sub("[^0-9]", "", line)
            if len(line) == 4:
                counter_list.append(line)

        file.close()
        return counter_list
