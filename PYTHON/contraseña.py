CONTRASEÑA='tomi.cardo'
contador=0
intentos=5
print('enter your password')
contraseña1=input(str())
while CONTRASEÑA!=contraseña1 and contador<4:
   intentos=intentos-1
   print(f'password incorrect, you have {intentos}  attemps restants')
   print("enter your password again")
   contraseña1=input(str())
   contador=contador+1
if CONTRASEÑA==contraseña1 and contador==4:
   print('password correct, you can get in to the calculator')
   print('welcome to calculator')
   print('input the first numer to make a operation')
   num1=float(input()) 
   print('input the second number to make a operation')
   num2=float(input())
   print('input the operations name for to make a operation like: suma, resta, multiplicacion o division')
   operacion=input(str()).strip().lower()
   if 'suma' in operacion:
      resultadoSuma=num1+num2
      print('el resultado de la suma es: ',resultadoSuma)
   elif 'resta' in operacion:
      resultadoResta=num1-num2
      print('el resultado de la resta es: ',resultadoResta)
   elif 'multiplicacion' in operacion:
      resultadoMultiplicacion=num1*num2
      print('el resultado de la multiplicacion es: ',resultadoMultiplicacion)
   elif 'division' in operacion:
      if num1 or num2==0:
         print('no se puede dividir por el numero "0"')
      else:
               resultadoDivsion=num1/num2  
               print('el resultado de la divison es: ',resultadoDivsion)
   elif contraseña1!=CONTRASEÑA and contador<4:
         print('intentos agotados, no puede ingresar al simulador')
