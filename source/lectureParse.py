# -*- coding=utf8 -*-
import sys
import urllib2

from bs4 import BeautifulSoup

from config import rootUrl
from lecture import Lecture

class LectureParser:
	def __init__(self):
		self.lectures = []

	def getLectureList(self):
		request = urllib2.Request(rootUrl)
		content = urllib2.urlopen(request).read()
		originContent = content.decode('gb2312').encode('utf-8')
		
		soup = BeautifulSoup(originContent)
		body = soup.body
		lectureBody = body.findAll("table")[1]
		lectureTrs = lectureBody.findAll("tr")[1:]

		for lectureTr in lectureTrs:
			self.processLecture(lectureTr)

	def processLecture(self,lectureTr):
		columns = lectureTr.findAll("td")
		serierNumber = columns[0]
		date = columns[3]
		title = columns[4]
		try:
			serierInt = int(serierNumber.text)
		except ValueError:
			return 
		if "Re:" in title.text:
			return 
		else :
			lecture = Lecture()
			url = title.find('a')
			lecture.link = url.attrs['href']
			try:
				dateAndTitle = (title.text.split('[')[1]).split("]")
				if len(dateAndTitle[0]) != 5:
					return 
				lecture.date = dateAndTitle[0]
				lecture.title = dateAndTitle[1]
				self.lectures.append(lecture)
			except IndexError:
				return

if __name__ == '__main__':
	lectureParser = LectureParser()
	lectureParser.getLectureList()
	for lecture in lectureParser.lectures:
		print lecture.date,lecture.title,lecture.link

