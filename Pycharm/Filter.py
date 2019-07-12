import re


class Filter:
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


if __name__ == "__main__":
    counter_code = Filter("TechCounter.txt")
    counters = counter_code.get_counters()
    for counter in counters:
        print(counter)