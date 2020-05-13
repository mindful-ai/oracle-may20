Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILE IO
>>> 
>>> # open(<path>, <mode>)
>>> # <mode>  ---> r -> read,  w -> write, a -> appends
>>> 
>>> # close()
>>> 
>>> # --------------- Reading from a file
>>> # read() -> reads the entire content as a single string
>>> # readline() -> reads the file line by line
>>> # readlines() -> read the entire content and return a list of lines
>>> 
>>> # tell()
>>> # seek()  --> resetting the cursor
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\lyrics.txt", "r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = "C:\next\text\read\form.txt"
>>> print(path)
C:
ext	exteadorm.txt
>>> path = r"C:\next\text\read\form.txt"
>>> print(path)
C:\next\text\read\form.txt
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\lyrics.txt", "r")
>>> type(f)
<class '_io.TextIOWrapper'>
>>> 
>>> text = f.read()
>>> print(text)
On a dark desert highway
Cool wind in my hair
Warm smell of colitas
Rising up through the air
Up ahead in the distance
I saw a shimmering light
My head grew heavy and my sight grew dim
I had to stop for the night
There she stood in the doorway
I heard the mission bell
And I was thinkin' to myself
'This could be heaven or this could be hell
Then she lit up a candle
And she showed me the way
There were voices down the corridor
I thought I heard them say
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face
Plenty of room at the Hotel California
Any time of year (any time of year)
You can find it here
Her mind is Tiffany-twisted
She got the Mercedes Benz, uh
She got a lot of pretty, pretty boys
That she calls friends
How they dance in the courtyard
Sweet summer sweat
Some dance to remember
Some dance to forget
So I called up the Captain
"Please bring me my wine"
He said, "We haven't had that spirit here since 1969"
And still those voices are calling from far away
Wake you up in the middle of the night
Just to hear them say
Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face
They livin' it up at the Hotel California
What a nice surprise (what a nice surprise)
Bring your alibis
Mirrors on the ceiling
The pink champagne on ice
And she said, "We are all just prisoners here of our own device"
And in the master's chambers
They gathered for the feast
They stab it with their steely knives
But they just can't kill the beast
Last thing I remember
I was running for the door
I had to find the passage back
To the place I was before
"Relax", said the night man
"We are programmed to receive
You can check out any time you like
But you can never leave"
>>> type(text)
<class 'str'>
>>> 
>>> 
>>> line = f.readline()
>>> line
''
>>> f.tell()
1796
>>> len(text)
1740
>>> text
'On a dark desert highway\nCool wind in my hair\nWarm smell of colitas\nRising up through the air\nUp ahead in the distance\nI saw a shimmering light\nMy head grew heavy and my sight grew dim\nI had to stop for the night\nThere she stood in the doorway\nI heard the mission bell\nAnd I was thinkin\' to myself\n\'This could be heaven or this could be hell\nThen she lit up a candle\nAnd she showed me the way\nThere were voices down the corridor\nI thought I heard them say\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face\nPlenty of room at the Hotel California\nAny time of year (any time of year)\nYou can find it here\nHer mind is Tiffany-twisted\nShe got the Mercedes Benz, uh\nShe got a lot of pretty, pretty boys\nThat she calls friends\nHow they dance in the courtyard\nSweet summer sweat\nSome dance to remember\nSome dance to forget\nSo I called up the Captain\n"Please bring me my wine"\nHe said, "We haven\'t had that spirit here since 1969"\nAnd still those voices are calling from far away\nWake you up in the middle of the night\nJust to hear them say\nWelcome to the Hotel California\nSuch a lovely place (such a lovely place)\nSuch a lovely face\nThey livin\' it up at the Hotel California\nWhat a nice surprise (what a nice surprise)\nBring your alibis\nMirrors on the ceiling\nThe pink champagne on ice\nAnd she said, "We are all just prisoners here of our own device"\nAnd in the master\'s chambers\nThey gathered for the feast\nThey stab it with their steely knives\nBut they just can\'t kill the beast\nLast thing I remember\nI was running for the door\nI had to find the passage back\nTo the place I was before\n"Relax", said the night man\n"We are programmed to receive\nYou can check out any time you like\nBut you can never leave"'
>>> f.seek(0)
0
>>> f.readline()
'On a dark desert highway\n'
>>> f.readline()
'Cool wind in my hair\n'
>>> f.readline()
'Warm smell of colitas\n'
>>> 
>>> 
>>> f.seek(0)
0
>>> content = f.readlines()
>>> type(content)
<class 'list'>
>>> content
['On a dark desert highway\n', 'Cool wind in my hair\n', 'Warm smell of colitas\n', 'Rising up through the air\n', 'Up ahead in the distance\n', 'I saw a shimmering light\n', 'My head grew heavy and my sight grew dim\n', 'I had to stop for the night\n', 'There she stood in the doorway\n', 'I heard the mission bell\n', "And I was thinkin' to myself\n", "'This could be heaven or this could be hell\n", 'Then she lit up a candle\n', 'And she showed me the way\n', 'There were voices down the corridor\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face\n', 'Plenty of room at the Hotel California\n', 'Any time of year (any time of year)\n', 'You can find it here\n', 'Her mind is Tiffany-twisted\n', 'She got the Mercedes Benz, uh\n', 'She got a lot of pretty, pretty boys\n', 'That she calls friends\n', 'How they dance in the courtyard\n', 'Sweet summer sweat\n', 'Some dance to remember\n', 'Some dance to forget\n', 'So I called up the Captain\n', '"Please bring me my wine"\n', 'He said, "We haven\'t had that spirit here since 1969"\n', 'And still those voices are calling from far away\n', 'Wake you up in the middle of the night\n', 'Just to hear them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face\n', "They livin' it up at the Hotel California\n", 'What a nice surprise (what a nice surprise)\n', 'Bring your alibis\n', 'Mirrors on the ceiling\n', 'The pink champagne on ice\n', 'And she said, "We are all just prisoners here of our own device"\n', "And in the master's chambers\n", 'They gathered for the feast\n', 'They stab it with their steely knives\n', "But they just can't kill the beast\n", 'Last thing I remember\n', 'I was running for the door\n', 'I had to find the passage back\n', 'To the place I was before\n', '"Relax", said the night man\n', '"We are programmed to receive\n', 'You can check out any time you like\n', 'But you can never leave"']
>>> content[0]
'On a dark desert highway\n'
>>> content[1]
'Cool wind in my hair\n'
>>> content[10:20]
["And I was thinkin' to myself\n", "'This could be heaven or this could be hell\n", 'Then she lit up a candle\n', 'And she showed me the way\n', 'There were voices down the corridor\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face\n', 'Plenty of room at the Hotel California\n']
>>> print(content[10:20])
["And I was thinkin' to myself\n", "'This could be heaven or this could be hell\n", 'Then she lit up a candle\n', 'And she showed me the way\n', 'There were voices down the corridor\n', 'I thought I heard them say\n', 'Welcome to the Hotel California\n', 'Such a lovely place (such a lovely place)\n', 'Such a lovely face\n', 'Plenty of room at the Hotel California\n']
>>> for line in content[10:20]:
	print(line)

	
And I was thinkin' to myself

'This could be heaven or this could be hell

Then she lit up a candle

And she showed me the way

There were voices down the corridor

I thought I heard them say

Welcome to the Hotel California

Such a lovely place (such a lovely place)

Such a lovely face

Plenty of room at the Hotel California

>>> f.close()
>>> 
>>> 
>>> # --------------------------- Writing to a file
>>> 
>>> # write() -> writes one line into a file
>>> # writelines() -> write a list of lines into a file
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\lyrics2.txt", "w")
>>> f.write('This is a copy of lyrics.txt\n')
29
>>> f.write('-'*60)
60
>>> f.write('\n')
1
>>> 
>>> f.close()
>>> 
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\transcripts\lyrics2.txt", "a")
>>> info = []
>>> for line in content:
	info.append(line.upper())

	
>>> f.writelines(info)
>>> f.close()
>>> 
>>> 
>>> 
