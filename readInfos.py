#!/usr/bin/python3
## @file readInfos.py
#  @package readInfos
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

import urllib
import string
import parser
from http import cookies
from urllib.parse import *
from collections import OrderedDict
from utils import *
from cste import *
import json
import requests
import sys
import time

startTime = time.time()

# Start TCP session
sess = requests.Session()
r = sess.get('http://edt.univ-tours.fr/direct/myplanning.jsp?login=ade-etudiant&password=test', headers=headerSess)

responeHeader = r.headers
headerSess['Cookie'] = parserBegin(r.headers['Set-Cookie'], ';') + "; " + '"{"state":{"sortField":"s:NAME", "sortDir":"s:ASC"}}"'

# Get GWT
r = sess.get('http://edt.univ-tours.fr/direct/gwtdirectplanning/gwtdirectplanning.nocache.js', headers=headerSess)
GWT = parser(r.text, "',ac='", "',bc='")

# Get js keys with GWT
r = sess.get('http://edt.univ-tours.fr/direct/gwtdirectplanning/' + GWT + '.cache.html', headers=headerSess)
headerSess['X-GWT-Permutation'] = GWT
headerSess['X-GWT-Module-Base'] = 'http://edt.univ-tours.fr/direct/gwtdirectplanning/'
keyCorePlanningServiceProxy = parser(r.text, "function SB(){vB();xx.call(this,$moduleBase,'CorePlanningServiceProxy','", "',uB)}")
keyConfigurationServiceProxy = parser(r.text, "function by(){Cx();xx.call(this,$moduleBase,'ConfigurationServiceProxy','", "',Bx)}")
keyWebClientServiceProxy = parser(r.text, "function vF(){fF();xx.call(this,$moduleBase,'WebClientServiceProxy','", "',eF)}")
keyMyPlanningClientServiceProxy = parser(r.text, "function b3b(){_2b();xx.call(this,$moduleBase,'MyPlanningClientServiceProxy','", "',$2b)}")
keyDirectPlanningServiceProxy = parser(r.text, "function x0b(){s0b();xx.call(this,$moduleBase,'DirectPlanningPlanningServiceProxy','", "',r0b)}")


##
# @fn initAde()
# @brief Method to register the application (init the session with the cookie)
#
def initAde() :
	payloadConfigurationProxy = "7|0|7|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyConfigurationServiceProxy + "|com.adesoft.gwt.core.client.rpc.ConfigurationServiceProxy|method1getInitialConfiguration|J|java.lang.String/2004016611|fr|1|2|3|4|2|5|6|" + uniqKey + "|7|"

	payloadCheck = "7|0|5|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyWebClientServiceProxy + "|com.adesoft.gwt.core.client.rpc.WebClientServiceProxy|method38isSsoConnected|J|1|2|3|4|1|5|" + uniqKey + "|"

	payloadCal = "7|0|5|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyWebClientServiceProxy + "|com.adesoft.gwt.core.client.rpc.WebClientServiceProxy|method4getProjectList|J|1|2|3|4|1|5|" + uniqKey + "|"

	payloadEtu = "7|0|5|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyWebClientServiceProxy + "|com.adesoft.gwt.core.client.rpc.WebClientServiceProxy|method2getUserLogin|J|1|2|3|4|1|5|" + uniqKey + "|"

	payloadProject = "7|0|7|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyWebClientServiceProxy + "|com.adesoft.gwt.core.client.rpc.WebClientServiceProxy|method6loadProject|J|I|Z|1|2|3|4|3|5|6|7|" + uniqKey + "|10|0|"

	payloadStruct = "7|0|6|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyWebClientServiceProxy + "|com.adesoft.gwt.core.client.rpc.WebClientServiceProxy|method26getSavedProperties|J|I|1|2|3|4|2|5|6|" + uniqKey + "|8|"

	payloadMyPlanningClientServiceProxy = "7|0|9|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyMyPlanningClientServiceProxy + "|com.adesoft.gwt.directplan.client.rpc.MyPlanningClientServiceProxy|method1login|J|com.adesoft.gwt.core.client.rpc.data.LoginRequest/3705388826|com.adesoft.gwt.directplan.client.rpc.data.DirectLoginRequest/635437471|ade-etudiant|test|1|2|3|4|2|5|6|" + uniqKey + "|7|0|0|0|0|0|8|9|-1|0|0|"

	headerSess['Content-Type'] = "text/x-gwt-rpc; charset=utf-8"
	headerSess["Content-Length"] = len(payloadConfigurationProxy)
	rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/ConfigurationServiceProxy", headers=headerSess, data=payloadConfigurationProxy)

	headerSess["Content-Length"] = len(payloadCheck)
	rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/WebClientServiceProxy", headers=headerSess, data=payloadCheck)

	#print("\nCHECK   : " + rPost.text)

	headerSess["Content-Length"] = len(payloadMyPlanningClientServiceProxy)
	rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/MyPlanningClientServiceProxy", headers=headerSess, data=payloadMyPlanningClientServiceProxy)

	#print("\nLOG     : " + rPost.text)

	headerSess["Content-Length"] = len(payloadCal)
	rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/WebClientServiceProxy", headers=headerSess, data=payloadCal)

	#print("\nCAL     : " + rPost.text)

	headerSess["Content-Length"] = len(payloadEtu)
	rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/WebClientServiceProxy", headers=headerSess, data=payloadEtu)

	#print("\nETU     : " + rPost.text)

	headerSess["Content-Length"] = len(payloadProject)
	rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/WebClientServiceProxy", headers=headerSess, data=payloadProject)

	#print("\nPROJECT : " + rPost.text)

	headerSess["Content-Length"] = len(payloadStruct)
	rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/WebClientServiceProxy", headers=headerSess, data=payloadStruct)

	#print("\nSTRUCT  : " + rPost.text)
# End of initAde()


##
# @fn getCalendar(numCalendar, GrpCalendar, outputJson)
# @brief Method to get the calendar from ADE
#
# @param numCalendar number of the student classgroup
#
# @param GrpCalendar name of the student classgroup
#
# @param outputJson output to write the calendar with data
#
def getCalendar(numCalendar, GrpCalendar, outputJson) :
	for SemAde in range(0, 44):
		# Evolution
		print('.', end="")
		sys.stdout.flush()

		# Avoid cross week at the beginning of the year
		if SemAde > 16:
			if SemAde < 26:
				Sem = "0" + str(SemAde - 16)
			else:
				Sem = str(SemAde - 16)
		else:
			Sem = str(SemAde + 36)

		# Init payloads
		payloadLegend = "7|0|12|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyDirectPlanningServiceProxy + "|com.adesoft.gwt.directplan.client.rpc.DirectPlanningPlanningServiceProxy|method5getLegends|J|com.adesoft.gwt.core.client.rpc.data.planning.PlanningSelection/886937684|com.extjs.gxt.ui.client.data.SortInfo/1143517771|java.util.ArrayList/4159755760|java.lang.Integer/3438268394|Cumul|com.extjs.gxt.ui.client.Style$SortDir/640452531|NAME|1|2|3|4|3|5|6|7|" + str(uniqKey) + "|6|8|7|9|0|9|1|9|2|9|3|9|4|9|5|9|6|259|10|0|8|1|9|" + str(numCalendar) + "|8|1|9|" + str(SemAde) + "|7|11|1|12|"

		payloadPlann = "7|0|11|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyCorePlanningServiceProxy + "|com.adesoft.gwt.core.client.rpc.CorePlanningServiceProxy|method5getAvailabilities|J|com.adesoft.gwt.core.client.rpc.data.planning.PlanningSelection/886937684|I|Z|java.util.ArrayList/4159755760|java.lang.Integer/3438268394|Cumul|1|2|3|4|5|5|6|7|7|8|" + str(uniqKey) + "|6|9|7|10|0|10|1|10|2|10|3|10|4|10|5|10|6|178|11|0|9|1|10|" + str(numCalendar) + "|9|1|10|" + str(SemAde) + "|1242|488|0|"

		payload = "7|0|12|http://edt.univ-tours.fr/direct/gwtdirectplanning/|" + keyDirectPlanningServiceProxy + "|com.adesoft.gwt.directplan.client.rpc.DirectPlanningPlanningServiceProxy|method8getTimetable|J|com.adesoft.gwt.core.client.rpc.data.planning.PlanningSelection/886937684|I|Z|java.util.List|java.util.ArrayList/4159755760|java.lang.Integer/3438268394|Cumul|1|2|3|4|6|5|6|7|7|8|9|" + str(uniqKey) + "|6|10|7|11|0|11|1|11|2|11|3|11|4|11|5|11|6|178|12|0|10|1|11|" + str(numCalendar) + "|10|1|11|" + str(SemAde) + "|1242|488|1|10|0|"

		headerSess["Content-Length"] = len(payloadLegend)
		rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/DirectPlanningPlanningServiceProxy", headers=headerSess, data=payloadLegend)
		headerSess["Content-Length"] = len(payloadPlann)
		rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/CorePlanningServiceProxy", headers=headerSess, data=payloadPlann)
		headerSess["Content-Length"] = len(payload)
		rPost = sess.post("http://edt.univ-tours.fr/direct/gwtdirectplanning/DirectPlanningPlanningServiceProxy", headers=headerSess, data=payload)

		data = rPost.text[4:]
		tempData = json.loads(data)

		jsonData = tempData[len(tempData) - 3]
		for mat in jsonData:
			if Sem not in outputJson:
				outputJson[Sem] = {}

			if GrpCalendar not in outputJson[Sem]:
				outputJson[Sem][GrpCalendar] = []

			if mat not in skipValue and mat not in outputJson[Sem][GrpCalendar] and len(mat) > 3:
				if mat in assocValue:
					if len(assocValue[mat]["name"]) > 1 and assocValue[mat]["name"] not in outputJson[Sem][GrpCalendar]:
						wValue = {}
						wValue["name"] = assocValue[mat]["name"]
						wValue["notions"] = assocValue[mat]["notions"]
						wValue["niveau"] = assocValue[mat]["niveau"]
						wValue["comm"] = assocValue[mat]["comm"]
						outputJson[Sem][GrpCalendar].append(wValue)
				elif mat.find('/') == -1 and len(mat) > 5:
					print(mat)
					outputJson[Sem][GrpCalendar].append(mat)
# End getCalendar()


print('START ', end="")
sys.stdout.flush()

initAde()
ListDII5 = OrderedDict()

# Calendar DII5_G1
getCalendar(7205, "DII5_G1", ListDII5)
getCalendar(7201, "DII5_G2", ListDII5)

sess.close()

# Write json file
json.dump(ListDII5, open('data/DII5.json', 'w', encoding='utf-8'), sort_keys=False, ensure_ascii=False)
print(" DONE")
print("Ca y est ton carnet de suivi a été généré ! Et en seulement " + str(time.time() - startTime) + " secondes ! Alors heureux ?")


# End of file

