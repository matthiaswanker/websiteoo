import csv
from cerandi_app.models import Stock

reader = csv.DictReader(open('TICKER_DESCRIPTION.csv'))

def main():
    print 1
    #for row in reader:
    #    print row['TICKER']

if __name__ == "__main__":
    main()