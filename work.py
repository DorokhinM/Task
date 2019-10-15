from random import randint
attempt = 1
point = 1
points =[]

while attempt <=5: 
  attempt += 1 
  text1 = randint(1,6) 
  line = int(input('вводите число,вот одного до 5:')) 
  perem = abs (line - text1)
 
  if perem == 0: 
    point = 6 
    points.append(point) 
  elif perem == 1: 
    point = 5 
    points.append(point) 
  elif perem == 2: 
    point = 4 
    points.append(point) 
  elif perem == 3: 
    point = 3 
    points.append(point) 
  elif perem == 4: 
    point = 2 
    points.append(point) 
  elif perem == 2: 
    point = 4 
    points.append(point)
  elif perem == 5: 
    point = 1 
    points.append(point) 
  print("кол-ов очков: ",point ) 
  every = sum(points) 

print ("общее кол - во очков",every)
if every< 25: 
  print("вы проиграли")
else: 
  print ("вы выйграли")