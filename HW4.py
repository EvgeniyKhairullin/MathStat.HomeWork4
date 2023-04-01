'''def mean_and_variance(a,b):
    return f'На промежутке ({a};{b}]\nСреднее значение: М(А) = {(a+b)/2: .2f}\nДисперсия: D(A) = {((b-a)**2)/12: .2f}'
print(mean_and_variance(200,800))'''

'''b=0.5+2.4**(1/2)
print(f'Левая граница распределения величины В - b = {b: .3f}\n'
      f'Среднее значение В на промежутке (0.5; {b: .3f}) M(B) = {(b+0.5)/2: .3f}'     
     )'''

#def z_value(height):
#    return (height-174)/8
#from statistics import NormalDist
#print(z_value(182))
#NormalDist().cdf(z_value(182))
#P=1-NormalDist().cdf(z_value(182))
#P
#z=z_value(190)
#z
#P=1-NormalDist().cdf(z)
#P
#z1=z_value(166)
#z1
#z2=z_value(190)
#z2
#P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
#P
#z1=z_value(166)
#z1
#z2=z_value(182)
#z2
#P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
#P
#z1=z_value(158)
#z1
#z2=z_value(190)
#z2
#P=NormalDist().cdf(z2)-NormalDist().cdf(z1)
#P
#z1=z_value(150)
#z1
#z2=z_value(190)
#z2
#P=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))
#P
#z1=z_value(150)
#z1
#z2=z_value(198)
#z2
#P=NormalDist().cdf(z1)+(1-NormalDist().cdf(z2))
#P
#z=z_value(166)
#z
#P=NormalDist().cdf(z)
#P

Z=(190-178)/25**(1/2)
Z
print(f'Рост человека, равный 190 см, отклоняется от математического ожидания роста в популяции, \n'
      f'в которой M(X) = 178 см и D(X) = 25 кв.см на Z = {Z} сигм.')
