import csv
with open('data.csv','r')as f:
  data = csv.reader(f)
  for row in data:
        print(row)


reader = csv.DictReader(open("data.csv"))
for raw in reader:
    print(dict(raw))
