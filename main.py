from bs4 import BeautifulSoup
import requests
import sys
import json
import datetime

variables = {
	'username': '',
	'listType': ''
}
outFile = "UNKNOWN"

def main(argv):
	global outFile

	for index, arg in enumerate(argv):
		if arg == "-u" or arg == "--username":
			variables['username'] = argv[index + 1]
		elif arg == "-t" or arg == "--type":
			variables['listType'] = argv[index + 1]
		elif arg == '-o' or arg == '--out-file' or arg == '--output':
			outFile = argv[index + 1]
		elif arg == '--help' or arg == '-h':
			print('''UNKNOWN Unofficial List Scraper/Exporter
by @nattadasu

Usage: `python main.py [OPTIONS...]`
-u, --username <STRING>
	Set UNKNOWN profile name (username).
-t, --type <anime, manga>
	Select which media type to export.
	Options: anime, manga
	If empty, script will prompt in initialization.
-o, --out-file, --output <file/path>
	Set where file will be saved as JSON.
	Script will automatically append '.json' to filename if not set.
	Default: ./UNKNOWN_animeList.json OR ./UNKNOWN_mangaList.json
-h, --help
	Show this help menu.''')
			return

	if variables['username'] == '':
		readUserName()
	elif variables['listType'] == '':
		readListType()
	else:
		readUNKNOWNLists()

def readUserName():
	variables['username'] = input("UNKNOWN.io username: ")

	if variables['username'] == '':
		print('Please enter a valid username!')
		readUserName()
	elif variables['listType'] == '':
		readListType()
	else:
		readUNKNOWNLists()

def readListType():
	variables['listType'] = input("Lists type you wish to scrape [anime/manga]: ").lower()

	if variables['listType'] != 'anime' and variables['listType'] != 'manga':
		print("please enter either anime or manga")
		readListType()
	else:
		readUNKNOWNLists()

def readUNKNOWNLists():
	rEntry = requests.get("https://UNKNOWN.io/user/" + variables['username'])
	bsEntry = BeautifulSoup(rEntry.text, features="html.parser")

	if outFile != 'UNKNOWN_':
		if '.json' not in outFile:
			fileName = outFile + '.json'
		else:
			fileName = outFile
	else:
		fileName = outFile + variables['listType'] + 'List.json'

	with open(fileName, 'w', encoding='utf-8') as f:
		json.dump(entryList, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
	main(sys.argv)