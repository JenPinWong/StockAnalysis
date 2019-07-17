import csv
import os

from Source_code.Counter import Counter


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
                line_count = 0

                for row in counter_database_reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    else:
                        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                        line_count += 1
                    print(f'Processed {line_count} lines.')

        except IOError:
            print("Fail to read database")



if __name__ == "__main__":
    list = []
    new_counter = Counter("6483")
    new_counter2 = Counter("3441")
    list.append(new_counter.get_company_info())
    list.append(new_counter2.get_company_info())

    Database.write_to_database("Data/counter_database.csv", list)

