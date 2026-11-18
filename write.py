#write to file John doe.txt it should contain data about John doe.txx

import string


f= open("john doe.txt","w")
string = '''
John doe is a nice guy and he lives in Nyc and his has card
'''

f.write(string)
f.close()
