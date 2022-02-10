import csv
from sys import argv, exit
from collections import OrderedDict


def main():
    # check for data file and sequence file
    # Usage: python dna.py data.csv sequence.txt
    # python dna.py databases/small.csv sequences/1.txt -> Bob
    # python dna.py databases/large.csv sequences/5.txt -> Lavender

    if len(argv) != 3:
        exit("Usage: python dna.py data.csv sequence.txt")

    # get protein headers and data with persons DNA sequences
    header, people = get_data(argv[1])

    # get test dna sequence
    sequence = get_dna(argv[2])

    # scan dna sequence for STR repeats from header
    unknown_person = scan_sequence(header, sequence)

    # compare unknown person to known persons
    # output name if found match or No Match
    compare(header, people, unknown_person)

    exit(0)


def get_data(filename):
    # Open DNA database CSV file
    # returns a list (header) with the CSV file headers and
    # an orderedDict (people) with persons names and dna profiles

    with open(filename, mode='r') as csvfile:
        csvdata = csv.DictReader(csvfile)
        people = []

        headers = csvdata.fieldnames

        for row in csvdata:
            people.append(row)

    return headers, people


def get_dna(filename):
    # Opens text file and return string (seq) with dna sequence

    with open(filename, "r") as file:
        seq = file.read()

    return seq


def scan_sequence(head, seq):
    # scan through unknown DNA sequence and store the longest consecutive protein strings in result dictionary
    result = OrderedDict()

    for i in range(1, len(head)):
        protein = head[i]

        loc = 0
        count = 1
        maxCount = 1
        foundLoc = seq.find(protein, loc)

        while (foundLoc != -1):
            loc = foundLoc + 1
            foundLoc = seq.find(protein, loc)
            # check if sequential
            if foundLoc == loc - 1 + len(protein):
                count += 1
                if count > maxCount:
                    maxCount = count
            else:  # not sequential
                count = 1

        result[protein] = maxCount

    return result


def compare(header, people, unknown_person):
    # compare the unkown DNA profile with the known persons

    for person in people:
        person['match_count'] = 0

    for s in range(1, len(header)):
        protein = header[s]
        for person in people:
            if int(unknown_person[protein]) == int(person[protein]):
                person['match_count'] += 1

    found_match = False
    for person in people:
        if person['match_count'] == (len(header) - 1):
            print(person['name'])
            found_match = True

    if not found_match:
        print("No match")

    return


if __name__ == "__main__":
    main()

