'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1
'''
import csv
import json
import xml.etree.ElementTree as ET

tree = ET.ElementTree(ET.fromstring(input()))
root = tree.getroot()

dictColor = {}

dictColor[root.attrib['color']] = 1

def colors (root, level):
    for child in root:
        if child.attrib['color'] not in dictColor.keys():
            dictColor[child.attrib['color']] = level
        else:
            dictColor[child.attrib['color']] += level
    for child in root:
        colors(child, level + 1)
   
colors(root, 2)
print(str(dictColor['red']), str(dictColor['green']), str(dictColor['blue']))
