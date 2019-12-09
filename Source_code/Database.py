import csv
import os


class Database:
    # Writes a dictionary into the database
    @staticmethod
    def write_to_database(filename, data):
        keys = data[0].keys()
        try:
            with open(filename, "a") as csv_file:
                counter_database_writer = csv.DictWriter(csv_file, keys)
                if os.stat(filename).st_size == 0:
                    counter_database_writer.writeheader()
                    counter_database_writer.writerows(data)
                else:
                    # Writes an empty dict to ensure new data follows below old data
                    blank_dict = dict()
                    counter_database_writer.writerow(blank_dict)
                    counter_database_writer.writerows(data)

                csv_file.close()

        except IOError:
            print("Fail to write to database")

        print("Successfully write to {}".format(filename))

    @staticmethod
    def read_database(filename):
        try:
            with open(filename, "r") as counter_database:
                counter_database_reader = csv.reader(counter_database, delimiter=",")

                for row in counter_database_reader:
                    print(", ".join(row))

        except IOError:
            print("Fail to read database")

