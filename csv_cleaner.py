import csv
# script for scraping course eval csv files
# and outputting a csv file showing only reviews
# longer than 3 characters
# for consumption by Watson Knowledge Studio

filename = 'cs56_reviews.csv'
csvFile = open(filename)
reader = csv.DictReader(csvFile)

outputFile = open('cs56_reviews_out.csv', "a")
fieldnames = ['text']
writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
writer.writeheader()

reviewList = []
for row in reader:
    rowList = list(row.items())
    text = rowList[0][1].strip()
    print(text)
    if len(text) >= 4:
        reviewList.append(text)

reviewList.sort()

count = 0
while count < 50:
     writer.writerow({'text': reviewList[count]})
     count += 1


csvFile.close()
outputFile.close()