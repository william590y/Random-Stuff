import pandas as pd
import numpy as np
import re
def f(dataset,x,y,radius):
 data = dataset
 results = pd.read_csv(data,delimiter='\t',encoding = 'latin1')
 if data == 'https://raw.githubusercontent.com/william590y/Miscellaneous-/master/Plate_Analysis/Quakes':
     results.drop(305, inplace = True)
 n = 0
 for row in results.iterrows():
     index, contents = row
     if abs(float(contents.Longitude)-x)%180 < radius and abs(float(contents.Latitude)-y)%180 < radius:
         n = n+1
 return n       
x = float(input('x-coordinate '))
y = float(input('y-coordinate '))
radius = float(input('radius '))
quake = f('https://raw.githubusercontent.com/william590y/Miscellaneous-/master/Plate_Analysis/Quakes',x,y,radius)
tsunami = f('https://raw.githubusercontent.com/william590y/Miscellaneous-/master/Plate_Analysis/tsunamis.txt',x,y,radius)
volcanoes = f('https://raw.githubusercontent.com/william590y/Miscellaneous-/master/Plate_Analysis/Volcanoes',x,y,radius)
print('Quakes: ',quake)
print('Tsunamis: ', tsunami)
print('Volcanoes: ',volcanoes)

