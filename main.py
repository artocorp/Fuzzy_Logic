import fuzzy as logic

lup = True

while lup == True:
 text = input("me : ")
 tanya=(logic.fjenis(text))
 if tanya == True:
  print('bot : [nanya] [{}]'.format(logic.fobjek(text)))
 else:
  print('bot : [peryataan]')

 luup=input('bot : lanjut?\nme : ')
 if luup.lower() == 'ya':
  pass
 else:
  lup = False