#### Python 2

from urllib import urlopen
import urllib
from re import findall
import csv


# The link to the player list
url = 'http://neafl.com.au/season/players'
web_page_contents = urlopen(url).read()


# Use regular expressions to find the names and clubs of all players
clubs = findall('font-size:0.9em;">(.*)</span>', web_page_contents) 
numbers = findall('<td style="text-align:center;font-weight:700;">(.*)</td>', web_page_contents) 

# Check the number of players and their corresponding club match 
print(len(clubs))
print(len(numbers))


# Find the links to each player profile
pplink = findall('<a href="/season/players/(.*)">', web_page_contents) 

# initialise name and image tuple
names = ()
ims = ()
# Go to each player profile and retrieve relevent data
for l in pplink:
	pp = "http://neafl.com.au/season/players/" + l
	pppage = urlopen(pp).read()

	name = findall('<h4>(.*)</h4>',pppage)
	names = names + (name[0],)
	im = name[0] +".png"
	ims = ims + (im,)
	
	# Find the image link
	image = findall('<img src="(.*)" class="m-0 p-0" style="max-width:100%;" />', pppage)
	# save image if link is found
	if image == []:
		print('no image')
	else:
		urllib.urlretrieve(image[0], im)
		print(im)

files = ['aspley.tex', 'brisbane.tex', 'canberra.tex', 'goldcoast.tex', 'gws.tex', 'nt.tex', 'redlands.tex', 'southport.tex', 'sydney.tex', 'uni.tex']

for team in files:
	file = open(team, 'w')

	for i in range(len(names)):
		if clubs[i] == "Sydney Swans": #need to change for each club. Need to automate this part
			file.write('''\\begin{figure}[H]
				\\centering
				\\includegraphics[width=0.25\\textwidth]{"''' + names[i] +
				'''".png}
				\\caption*{''' + names[i] + ''' ''' + numbers[i] +
				'''}
			\\end{figure}

					''')

