from urllib import urlopen
import urllib
from re import findall
import csv



url = 'http://neafl.com.au/season/players'

web_page_contents = urlopen(url).read()



clubs = findall('font-size:0.9em;">(.*)</span>', web_page_contents) 
numbers = findall('<td style="text-align:center;font-weight:700;">(.*)</td>', web_page_contents) 
print(len(clubs))
print(len(numbers))





pplink = findall('<a href="/season/players/(.*)">', web_page_contents) 
names = ()
ims = ()
for l in pplink:
	pp = "http://neafl.com.au/season/players/" + l
	pppage = urlopen(pp).read()

	name = findall('<h4>(.*)</h4>',pppage)
	names = names + (name[0],)
	im = name[0] +".png"
	ims = ims + (im,)


	# image = findall('<img src="(.*)" class="m-0 p-0" style="max-width:100%;" />', pppage)
	# if image == []:
	# 	print('t')
	# else:
	# 	urllib.urlretrieve(image[0], im)
	# 	print(im)

	
	



file = open('sydney.tex', 'w')

for i in range(len(names)):
	if clubs[i] == "Sydney Swans":
		file.write('''\\begin{figure}[H]
			\\centering
			\\includegraphics[width=0.25\\textwidth]{"''' + names[i] +
			'''".png}
			\\caption*{''' + names[i] + ''' ''' + numbers[i] +
			'''}
		\\end{figure}

				''')

