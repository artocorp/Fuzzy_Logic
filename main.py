import fuzzy as logic
import sys

while True:
 text = input("me : ")
 tanya=(logic.fjenis(text))
 print('bot : [nanya] [{}]'.format(logic.fobjek(text))) if tanya == True else print('bot : [peryataan]')

 luup=input('bot : lanjut?\nme : ')
 if luup.lower() == 'ya':pass
 else:sys.exit('Bye onii-chan')
