from bs4 import BeautifulSoup
from constants import *
from functions import *

# open files for program
document = BeautifulSoup(open('Oly_Program.html'))
wod_doc_temp = open('temp_wods.html', 'w')
wod_doc_final = open('extracted_wods.html', 'w')

# generate opening tags to final html doc
wod_doc_final.write(START_HTML_TAG)
wod_doc_final.write(CHAR_META_TAG)
generate_jquery(wod_doc_final)

# get all div tags that contain the workout lists
tags_to_delete = document.find_all(['span', 'a', 'br'])
divs = document.find_all('div', { 'class' : 'workouts_list_text'} )

day_num = 0

# remove all span, a, and br tags and their content
for delete in tags_to_delete:
	delete.replaceWith('')

# write workout divs into temp file
for div in divs:
	day_num += 1

	#wod_doc_temp.write(START_WOD_TITLE_TAG + 'Day %i' % day_num + END_WOD_TITLE_TAG)
	wod_doc_temp.write(div.prettify('utf-8'))

wod_doc_temp.close()
wod_doc_temp = open('temp_wods.html', 'r')

generate_dropdown(day_num, wod_doc_final)
day_num = 0

# write workouts into final html file
for line in wod_doc_temp:
	if '&amp;' in line:
		wod_doc_final.write(line.replace('&amp;', 'and'))
	elif 'workouts_list_text' in line:
		day_num += 1
		wod_doc_final.write(line.replace('workouts_list_text', 'workout day%i' % day_num))
	else:
		wod_doc_final.write(line)

wod_doc_final.write(END_HTML_TAG)
wod_doc_final.close()
