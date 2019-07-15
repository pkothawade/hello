s = input ("Enter a sentence: ")
d = {'digits':0, 'letters':0}
for c in s:
     if c.isdigit():
          d['digits']+=1
     elif c.isalpha():
          d['letters']+=1
     else:
          pass
print("Letters", d['letters'])
print("Digits", d['digits'])
