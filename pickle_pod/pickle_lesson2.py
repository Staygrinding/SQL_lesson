'''
Program: pickle_lesson2.py
Author: Josiah Johnson
Date: 1/27/2021
The Hidden Genius Project
Cohort: Oak8
'''




import pickle

#1 Initialize an empty dictionary variable, name it all_pod_members
all_pod_members = {}

#2 Initialize a file variable to write data to, name it pod_file, that will
# open a file named hgp_pods that you will write data to the file. 
pod_file = open('all_pods.pkl', 'wb')

#3  Initialize empty dictionary variables, name it as such;
jacore_members = {}
gabe_members = {}
richard_members = {}
aris_members = {}
andrew_members = {}

#4 Create an empty dictionary for the other 3 PODs; Aris, Gabriel and Richard


jacore_members[‘Morris Jones’] = ‘(925) 286-5922’
jacore_members[‘Prince Fields’] = ‘(510) 472-0804’
jacore_members[‘Akari Johnson’] = ‘(510) 500-2206’

andrew_members[‘Andrew Lubega’] = ‘(925) 727-4611’
andrew_members[‘Mallick Abdullah’] = ‘(510) 409-8755’
andrew_members[‘Ronin Youngjones’] = ‘(415) 910-3415’
andrew_members[‘Glenn Ivory’] = ‘(510) 328-8290’

richard_members[‘Richard Kamau’] = ‘(510)228-5623’
richard_members[‘Matthew Dudley’] = ‘(510)816-2411’
richard_members[‘Kymari Rhodes’] = ‘(510)575-1982’
richard_members[‘Josiah Johnson’] = ‘(510)860-5112’

gabriel_members[‘Gabriel Reader’] = ‘(510)326-5834’
gabriel_members[‘Emanual Torbor’] = ‘(510)934-4133’
gabriel_members[‘David Brickely’] = ‘(510)631-6288’
gabriel_members[‘Myles Wilkerson’] = ‘(510)500-7266’

aris_members[‘Aris Carter’] = ‘(510)229-6359’
aris_members[‘Milan Kral’] = ‘(510)816-3232 ’
aris_members[‘Maurice Richardson’] = ‘(510)424-7789’
aris_members[‘Zyion Williams’] = ‘(510)480-5785’
aris_members[‘Hyab Isayas’] = ‘(510)612-3737’


#6 Add all the PODS to the all_pod_members dictionary
all_pod_members['Jacore'] = jacore_members
all_pod_members['Andrew'] = andrew_members

#7 Dump all the 
pickle.dump(jacore_members,pod_file)
pickle.dump(andrew_members,pod_file)

#8 Open the pod_file to read data
pod_file = open('all_pods.pkl', 'rb')

#9 Print all the Pod leaders and POD membership
for key,value in all_pod_members.items():
  print('This POD Leader is',key)
  for key2, value2 in value.items():
    print(key2,value2)
  print('\n')

pod_file.close()
