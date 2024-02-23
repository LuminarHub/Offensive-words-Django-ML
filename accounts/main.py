from better_profanity import profanity
import re

user_input = input("enter the text: ")
user = user_input.lower()
x = profanity.censor(user_input)
x_list = x.split()

pattern = r"[****]"
def has_special_characters(text):
    return bool(re.search(pattern, text))
c=0
for item in x_list:
    if has_special_characters(item):
        
        c=c+1
if c!=0:
    result = "offensive" 
else :
    result = "not offensive"
import random
pattern1 = '****'
#output = ('low','medium','high')
for word in x_list:
    if word != pattern1:
        print(word, "good")
    else:
        print(word,'offensive')
        #print("bad")



mild=['bitch','bloody','bugger','chav','cow','crap','damn','douchebag','effing','feck','ginger','git','minger','pissed','pissed off','sod off',
      'uppity','arse','balls','bawbag','choad','bang','bonk','frigging','ho','tart']
moderate=['bastard','bellend','bloodclaat','bumberclat','dickhead','shit','shite','son of a bitch','twat','arsehole','beaver','bollocks',
          'lunge','cock','dick','fanny','knob','minge','prick','pussy','snatch','tits','jizz','milf','shag','skank','slag','slapper','spunk','tosser','wanker','whore']
strong=['fuck','motherfucker','cunt','gash','japs eye','punani','pussy hole','cocksucker','cum','nonce','prickteaser','raped','slut'] 




profanity_words = ['bitch','bloody','bugger','chav','cow','crap','damn','douchebag','effing','feck','ginger','git','minger','pissed','pissed off','sod off',
      'uppity','arse','balls','bawbag','choad','bastard','bellend','bloodclaat','bumberclat','dickhead','shit','shite','son of a bitch','twat','arsehole','beaver','bollocks',
          'clunge','cock','dick','fanny','knob','minge','prick','pussy','snatch' ,'tits','fuck','motherfucker','cunt','gash','japs eye','punani','pussy hole',
          'bang','bonk','frigging','ho','tart','milf','shag','skank','slag','slapper','spunk','tosser','wanker','whore','cocksucker','cum','nonce','prickteaser','raped','slut']


pattern = fr'\b({"|".join(map(re.escape, profanity_words))})\b'


censored_words = re.findall(pattern, user, flags=re.IGNORECASE)

print("Censored Words:",censored_words)

for i in censored_words:
    if i in strong:
        print(i,"strong")
    elif i in moderate:
        print(i,"moderate")
    elif i in mild:
        print(i,"mild")
    else:
        print("no offensive")