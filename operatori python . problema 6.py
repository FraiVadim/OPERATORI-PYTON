n=5604
print ("ultima cifra a acestui numar:",(n%1000%100%10))
print ("penultima cifra a acestui numar:",(n%1000%100//10))
print ("restul impartirii la 9:",(n%9))
print ("catul impartirii la 9:",(n//9))
print ("suma cifrelor acestui numar:",((n//1000)+(n%1000//100)+(n%1000%100//10)+(n%1000%100%10)))
cifra1= (n//1000)
cifra2= (n%1000//100)
cifra3= (n%1000%100//10)
cifra4= (n%1000%100%10)
print ("rasturnatul acestui numar este:",cifra4,cifra3,cifra2,cifra1)