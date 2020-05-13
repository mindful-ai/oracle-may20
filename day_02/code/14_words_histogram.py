# Program to create or print the word histogram
# Input:
# 'Twinkle Twinkle Little Star'
# Output:
# Twinkle -> 2
# Little  -> 1
# Star    -> 1

# open the file
# read the contents -> read() -> string
# split() -> List of words
# Construct a dictionary key -> word, value -> number of time word occurs
# Transfer the contents of the dictionary in to a text file

srcpath = r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\lyrics.txt"
destpath = r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\whreport.txt"


# open the file

f = open(srcpath)

# read the contents -> read() -> string

content = f.read()
f.close()

# split() -> List of words

words = content.split()
# print(words)

# Construct a dictionary key -> word, value -> number of time word occurs

D = {}
for word in words:
    if word in D.keys():
        D[word] = D[word] + 1
    else:
        D[word] = 1

# print(D)

# Transfer the contents of the dictionary in to a text file

print('-'*60)

print('Number of unique words: ', len(D.keys()))

f = open(destpath, 'w')
f.write('WORD HISTOGRAM : lyrics.txt \n\n')
f.write('-----------------------------------------\n')
f.write('WORD                | WORD COUNT         \n')
f.write('-----------------------------------------\n')
for word, wcount in D.items():
    col1 = word.ljust(20)
    col2 = str(wcount).rjust(10)
    row  = col1 + '|' + col2 + '\n'
    f.write(row)

f.write('-----------------------------------------\n')
f.write('Total number of words: ' + str(len(words)) + '\n')
f.write('Number of unique words: ' + str(len(D.keys())) + '\n')
f.close()
    





    
    
