import re
import requests

url = "https://www.google.com/search?client=firefox-b-1-e&q=site:instagram.com+%22wrestling%22+%22@gmail.com%22&spell=1&sa=X&ved=2ahUKEwipwejYu9LrAhUFWs0KHdlZAVIQBSgAegQIBxAn&biw=1395&bih=971"

e_regx = r"[\w\.-]+@[\w\.-]+"

r = requests.get(url)

for i in re.findall(e_regx, r.text):
	print(i)
