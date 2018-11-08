import re


item = "0714RgilDS1054e.ON"
print(item)
name  = re.sub('(\d+)([a-zA-Z][\w\ ]+)([\.\w]+)', r'\2',  item)
print(name)
name = re.sub('([\w]+)/([a-zA-Z[\w\ ]+)', r'\2',  name)
print(name)
exit()