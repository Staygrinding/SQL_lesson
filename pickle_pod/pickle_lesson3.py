'''
Program: pickle_lesson2.py
Author: Josiah Johnson
Date: 1/27/2021
The Hidden Genius Project
Cohort: Oak8
'''

instructor = {}



jacore_members = {}
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'
jacore_leader = {}
jacore_leader['Jacore Baptise'] = jacore_members
instructor['Baba'] =  jacore_leader
print(instructor)


andrew_members = {}
andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755'
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'
andrew_leader = {}
andrew_leader['Andrew lubega'] = andrew_members
instructor['Baba'] = andrew_leader
print(instructor)


richard_members = {}
richard_members['Richard Kamau'] = '(510)228-5623'
richard_members['Matthew Dudley'] = '(510)816-2411'
richard_members['Kymari Rhodes'] = '(510)575-1982'
richard_members['Josiah Johnson'] = '(510)860-5112'
richard_leader = {}
richard_leader['richard kamu'] = richard_members
instructor['Baba'] = richard_leader
print(instructor)

gabe_members = {}
gabriel_members['Gabriel Reader'] = '(510)326-5834'
gabriel_members['Emanual Torbor'] = '(510)934-4133'
gabriel_members['David Brickely'] = '(510)631-6288'
gabriel_members['Myles Wilkerson'] = '(510)500-7266'
gabe_leader = {}
gabe_leader['gabriel reader'] = gabe_members
instructor['Baba'] = gabe_leader
print(instructor)

aris_members = {}
aris_members['Aris Carter'] = '(510)229-6359'
aris_members['Milan Kral'] = '(510)816-3232 '
aris_members['Maurice Richardson'] = '(510)424-7789'
aris_members['Zyion Williams'] = '(510)480-5785'
aris_members['Hyab Isayas'] = '(510)612-3737'
aris_leader = {}
aris_leader['aris carter'] = aris_members
instructor['baba'] = aris_leader
print(instructor)


for key,value in all_pod_members.items():

  print('This POD Leader is',key)
  for key2, value2 in value.items():
    print(key2,value2)
  print('\n')


"""
