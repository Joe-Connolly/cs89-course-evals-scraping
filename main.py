import requests
import json
import csv
# script for scraping course eval csv files
# and outputting a json file for each review
# of the 250 longest reviews for a course
# for consumption by Watson Discovery

def csvToJSON(courseNum):
    # set up reader
    csvFile = open(f'data/csv/cs_{courseNum}.csv')
    reader = csv.DictReader(csvFile)

    questionNum = 0
    rowNum = 0
    reviewJSONData = []
    skipRow = False
    for row in reader:
        # print(row)
        rowList = list(row.items())
        if rowList[0][1].startswith('Comment') or rowList[0][1].startswith('How'):
            questionNum += 1
            skipRow = True
            continue
        if skipRow:
            skipRow = False
            continue
        reviewJSON = {}
        term = rowList[0][1].strip()
        professor = rowList[1][1].strip()
        text = rowList[2][1].strip()
        if len(text) < 4:
            continue
        reviewJSON['courseNum'] = courseNum
        reviewJSON['term'] = term
        reviewJSON['professor'] = professor
        reviewJSON['text'] = text
        reviewJSON['questionNum'] = questionNum
        # print(reviewJSON)
        rowNum = rowNum + 1
        if len(reviewJSON['term'].strip()) >= 3:
            reviewJSONData.append(reviewJSON)

    reviewJSONData.sort(key=lambda x: len(x['text']), reverse=True)
    i = 0
    while i < 250 and i < len(reviewJSONData):
        reviewJSON = reviewJSONData[i]
        jsonFile = open(f'reviews/review_cs{courseNum}_{i}.json', 'w')
        with jsonFile as outfile:  
            json.dump(reviewJSON, outfile)
        jsonFile.close()
        i += 1

    # close files
    csvFile.close()
    

csvToJSON(31)