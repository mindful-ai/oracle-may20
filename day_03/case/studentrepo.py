# Read the csv file as a text file

path = r"C:\Users\Purushotham\Desktop\oracle\day_03\case\students.csv"
f = open(path)
content = f.readlines()
f.close()

# ------------------------ csv file is read and its content is available for further processing

# Read the coloums --> name,age,regid,phy,chem,math,bio,avg,rank
# Read a row --> Vijay,14,HPE001,99,98,97,96,0,0
# Construct a dictionary out of the column and the row
# Add that dictionary to the main dictionry that represents the class
# Repeat this process for all the entries in the csv file

classdict = {}

coldata  = content[0]
columns  = [item.strip() for item in coldata.split(',')]
for rowdata in content[1:]:
    #rowdata  = content[1]
    rows     = [item.strip() for item in rowdata.split(',')]
    studdict = dict(zip(columns, rows))
    classdict.setdefault(studdict['regid'], studdict)

# ------------------------- csv data is in the form of a dictionary

# Access the dictionary iteratively and calculate the average marks and
# update in the dictionary

for regid in classdict.keys():
    # sum_of_subjmarks = classdict[regid]['phy'] + classdict[regid]['chem'] + ...
    sum_of_subjmarks = 0
    for key in ['phy', 'chem', 'math', 'bio']:
        sum_of_subjmarks += int(classdict[regid][key])
    classdict[regid]['avg'] = sum_of_subjmarks / 4



# ------------------------- dictionary updated with average data

# Calculate the rank
# collect all the averages -> into a list
# arrange the averages in descending order
# iterate the entire dictionary and update the rank based on the descending
# order of averages

avgs = [classdict[regid]['avg'] for regid in classdict.keys()]

avgs.sort(reverse=True)

rank = 1
for avg in avgs:
    for regid in classdict.keys():
        if(classdict[regid]['avg'] == avg):
            classdict[regid]['rank'] = rank
    rank += 1

print(classdict)

# ------------------------- dictionary updated with rank data

# Re-write the csv file

path = r"C:\Users\Purushotham\Desktop\oracle\day_03\case\students_updated.csv"
f = open(path, 'w')
f.write(coldata)
for regid in classdict.keys():
    r = list(zip(*classdict[regid].items()))
    rowdata = ','.join([str(item) for item in r[1]]) + '\n'
    f.write(rowdata)
f.close()

# ------------------------- resultant csv file is now ready
