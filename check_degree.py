ball=input('Balingizni kiriting: ')

if ball.isdigit():
    ball=int(ball)
    if ball<60 and ball>=0:
     print(ball,' You failed, hahaha')

    elif ball>=60 and ball<70:
     print(ball,'===> D ')

    elif ball>=70 and ball<80:
     print(ball,'===> C')

    elif ball>=80 and ball<90:
     print(ball,'===> B')

    elif ball>=90 and ball<=100:
     print(ball, '===> A')
    
    
else:
  print('Error') 
  
   
