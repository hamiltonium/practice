import numpy
import csv


def writecsv():
    with open('eggs.csv','wb') as csvfile:
        eggwriter = csv.writer(csvfile)
        eggwriter.writerow(['spam','2spams'])

def readcsv():
    with open('eggs.csv','r') as csvfile:
        eggreader = csv.reader(csvfile)
        for row in eggreader:
            print row

if __name__ == "__main__":
    writecsv()
    readcsv()
