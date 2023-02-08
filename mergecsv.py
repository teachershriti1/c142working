import csv
with open("movies.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]
    headers=data[0]
headers.append("poster_link")
with open("final.csv","a+",encoding="utf-8") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
with open("movie_links.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    alllinks=data[1:]
for movieItem in allmovies:
    posterfound=any(movieItem[8] in linkitem for linkitem in alllinks)
    if(posterfound):
        for linkitem in alllinks:
            if movieItem[8]==linkitem[0]:
                movieItem.append(linkitem[1])
                if len(movieItem)==28 :
                    with open("final.csv","a+",encoding="utf-8") as f:
                        csvwriter=csv.writer(f)
                        csvwriter.writerow(movieItem)



