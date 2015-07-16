/* @file main.js
 * @brief Javascript to print the carnet formated
 * @author Jeremy HERGAULT (reneca)
 * @version 1.0
 * @date 2015-07-15
 *
 * This file is part of Polycarnet, which is a carnet de suivi genrator
 * Copyright (C) 2015  HERGAULT Jeremy, Alexandre, Thierry ( reneca )
 *
 * Polycarnet is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Polycarnet is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Polycarnet. If not, see <http://www.gnu.org/licenses/>.
 */

////
// Read JSON file
////
var reqJsonDII5 = new XMLHttpRequest();
reqJsonDII5.open("GET", "data/DII5.json", true); 
reqJsonDII5.onreadystatechange = readJsonDII5;
reqJsonDII5.send(null);

// Temp vars
var title;
var textTitle;
var tab;


/*
 * @fn printWeek(dataJson, week, groupe, tabBalise)
 * @brief Method to print week on the HTML page
 *
 * @param dataJson data input from the json file
 *
 * @param week number of the year week
 *
 * @param groupe name of the student classgroup
 *
 * @param tabBalise pointer on the HTML balise
 */
function printWeek(dataJson, week, groupe, tabBalise) {
	// Ajout titre semaine
	title = document.createElement('h3');
	textTitle = document.createTextNode("Semaine " + week + " (" + groupe + ")");
	title.appendChild(textTitle);
	tabBalise.appendChild(title);

	tab = document.createElement('p');

	// Ajout tableau
	var textElement = document.createTextNode("INTITULE COURS" + ";" + "NOTIONS ETUDIEES" + ";" + "NIVEAU" + ";" + "COMMENTAIRE");
	tab.appendChild(textElement);
	tab.innerHTML += "<br />";

	for(mats in dataJson[week][groupe]) {
		textElement = document.createTextNode(dataJson[week][groupe][mats]["name"]
					+ ";" + dataJson[week][groupe][mats]["notions"]
					+ ";" + dataJson[week][groupe][mats]["niveau"]
					+ ";" + dataJson[week][groupe][mats]["comm"]);

		tab.appendChild(textElement);
		tab.innerHTML += "<br />";						
	}

	tabBalise.appendChild(tab);
}


/*
 * @fn readJsonDII5()
 * @brief Method call when the json file is load
 */
function readJsonDII5() {
	if (reqJsonDII5.readyState == 4) {
		if(reqJsonDII5.status == 200) {
			var data = JSON.parse(reqJsonDII5.responseText);
			var balise = document.getElementById('divDII5');

			for(week in data) {
				if (data[week]["DII5_G1"].length > 0) {
					printWeek(data, week, "DII5_G1", balise)
				}
				if (data[week]["DII5_G2"].length > 0) {
					printWeek(data, week, "DII5_G2", balise)
				}
			}
		} else
			dump("Erreur pendant le chargement de la page.\n");
	}
};

// End of file
