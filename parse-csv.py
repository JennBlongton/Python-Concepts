import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)
    # print(csv_reader)
    # <_csv.reader object at 0x0000025E2E96F580>
    # next(csv_reader)
    # skips the header

    # for line in csv_reader:
    #     print(line)
        # list of values in csv file
