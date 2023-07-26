import random
import itertools



RANKS='023456789QWERTYUIOPASDFGHJKZXCVBNMqwertyuiopasdfghjkzxcvbnm!@#$%^&,;()_'
password=''
for i in range(12):
    password += ' '.join([random.choice(RANKS)])
    
print(password)

