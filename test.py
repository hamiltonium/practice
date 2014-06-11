import numpy
import csv


def main():
    with open('eggs.csv','wb') as csvfile:
        eggwriter = csv.writer(csvfile)
        eggwriter.writerow(['spam','2spams'])

if __name__ == "__main__":
    main()
