from dateutil import parser ; str2date = parser.parse
b = str2date('20 April') <= str2date('22 April') <= str2date('21 May')
print(b)
