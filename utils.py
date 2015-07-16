#!/usr/bin/python3
## @file utils.py
#  @package utils
#  @brief Generals constants for python application
#  @author Jeremy HERGAULT (reneca)
#  @version 1.0
#  @date 2015-07-15
#
#  This file is part of Polycarnet, which is a carnet de suivi genrator
#  Copyright (C) 2015  HERGAULT Jeremy, Alexandre, Thierry ( reneca )
#
#  Polycarnet is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Polycarnet is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Polycarnet. If not, see <http://www.gnu.org/licenses/>.

import string
import json
from datetime import datetime
from datetime import timedelta

##
# @fn parser(text, patternBegin, patternEnd)
# @brief Method to parse a text between two patterns
#
# @param text text to parse
#
# @param patternBegin pattern for the match at the beginning
#
# @param patternEnd pattern for the match at the ending
#
# @return return the text between patternBegin and patternEnd
#
def parser(text, patternBegin, patternEnd) :
	try :
		text = text[(text.index(patternBegin) + len(patternBegin)):]
	except ValueError :
		print("Can't parse[1] patern '" + patternBegin + "' :\n" + text)
		return text
	try :
		text = text[:text.index(patternEnd)]
	except ValueError :
		print("Can't parse[2] patern '" + patternEnd + "' :\n" + text)
		pass
	return text

##
# @fn parserFirst(text, pattern)
# @brief Method to parse a text after the pattern
#
# @param text text to parse
#
# @param pattern pattern for the match at the beginning
#
# @return return the text after the pattern
#
def parserFirst(text, pattern) :
	try :
		text = text[(text.index(pattern) + len(pattern)):]
	except ValueError :
		print("Can't parseFirst patern '" + pattern + "' :\n" + text)
		pass
	return text

##
# @fn parserBegin(text, pattern)
# @brief Method to parse a text before the pattern
#
# @param text text to parse
#
# @param pattern pattern for the match at the ending
#
# @return return the text before the pattern
#
def parserBegin(text, pattern) :
	try :
		text = text[:text.index(pattern)]
	except ValueError :
		print("Can't parseBegin patern '" + pattern + "' :\n" + text)
		pass
	return text

##
# @fn parserFrom(text, paternBegin, iteration, paternEnd)
# @brief Method to parse a text between two patterns after a number of iterations
#
# @param text text to parse
#
# @param patternBegin pattern for the match at the beginning
#
# @param iteration iteration of the patternBegin
#
# @param patternEnd pattern for the match at the ending
#
# @return return the text between patternBegin after the number of iteration and patternEnd
#
def parserFrom(text, paternBegin, iteration, paternEnd) :
	extract = text.split(paternBegin)
	if len(extract) >= (iteration + 1) :
		return(extract[iteration].split(paternEnd)[0])

##
# @fn parseLink(text)
# @brief Method to parse a url from a html tag
#
# @param text text to parse
#
# @return return the url of the html tag
#
def parseLink(text) :
	return parser(text, '<a href="', '">')

##
# @fn showTime(time)
# @brief Method to format the print of a time
#
# @param time time to format
#
# @return return a string of the formated time
#
def showTime(time) :
	return(str(time.hour) + ':' + str(time.minute) + ':' + str(time.second) + '.' + str(time.microsecond))

##
# @fn getTimeDifference(previousTime)
# @brief Method to get the delta time between now and the previous time
#
# @param previousTime time from a previous moment
#
# @return return the delta time between now and the previous time
#
def getTimeDifference(previousTime) :
	return(datetime.now() - previousTime)

##
# @fn getDateNow(addDays)
# @brief Method to get the current date formated, with an offset of addDays
#
# @param addDays offset from the current date
#
# @return return the date formated with an offset of addDays
#
def getDateNow(addDays) :
	now = datetime.now() + timedelta(days=addDays)
	return(str(now.day) + '/' + str(now.month) + '/' + str(now.year))

##
# @fn getDayWeekNow(addDays)
# @brief Method to get the current day formated, with an offset of addDays
#        The day is formated like 0 is Monday, and 6 sunday
#
# @param addDays offset from the current date
#
# @return return the current day formated, with an offset of addDays
#
def getDayWeekNow(addDays) :
	return (datetime.now() + timedelta(days=addDays)).isoweekday()

##
# @fn compressJsonFile(nameFile)
# @brief Method to compress a JSON file to remove useless caracters (spaces and new lines)
#
# @param nameFile name of the file need to be compress
#
# @return return 1 if an error occur
#
def compressJsonFile(nameFile) :
	try:
		jsonBuf = json.load(open(nameFile), object_pairs_hook=collections.OrderedDict)
	except IOError :
		print("Can't open the file : " + nameFile)
		return 1
	fFile = open(nameFile, 'w', encoding='utf-8')
	json.dump(jsonBuf, fFile)

##
# @fn uncompressJsonFile(nameFile)
# @brief Method to uncompress a JSON file to add indentation
#
# @param nameFile name of the file need to be uncompress
#
# @return return 1 if an error occur
#
def uncompressJsonFile(nameFile) :
	try:
		jsonBuf = json.load(open(nameFile), object_pairs_hook=collections.OrderedDict)
	except IOError :
		print("Can't open the file : " + nameFile)
		return 1
	fFile = open(nameFile, 'w', encoding='utf-8')
	json.dump(jsonBuf, fFile, indent=4)


# End of file

