def weight_on_planets():
   # write your code here
   weight = float(input('What do you weigh on earth? ' ))
   mars = '\nOn Mars you would weigh'
   marsWeight = (0.38*weight)
   jupiter = 'On Jupiter you would weigh'
   jupiterWeight = (2.34*weight)
   
   print(mars , marsWeight , 'pounds.\n' + jupiter , jupiterWeight, "pounds")


   
if __name__ == '__main__':
   weight_on_planets()