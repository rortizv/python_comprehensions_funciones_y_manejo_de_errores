import csv

# Read CSV file and convert to a dictionary
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # This is a list with the names of the keys(columns)
        header = next(reader)
        data = []
        for row in reader:
            # Let's join the header and the iterated row
            iterable = zip(header, row)
            country_dict = { key: value for key, value in iterable }
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])