import csv

scores = {}

with open('pr.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # 跳过标题行
    for row in reader:
        name = row[1]
        if len(row) < 5:
            score = 0
        else:
            score = row[4]
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score

with open('scores_summary.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Total Score'])
    for name in scores:
        writer.writerow([name, scores[name]])
