from bs4 import BeautifulSoup
import csv

# load compTrain webpage
compTrain = BeautifulSoup (open("compTrain.html"))

# get current post
todayArticle = compTrain.find_all('article', 'category-wods')[:2]


# get the fist div tag which contains recent information
# then skip to just get workouts 'p' tags
for divTag in todayArticle:
    wholeWorkoutDiv = divTag.find_all('div', 'entry-content')
    for justWorkoutDiv in wholeWorkoutDiv:
	for workout in justWorkoutDiv.find_all('p', style=False):
	      print(workout.text);
