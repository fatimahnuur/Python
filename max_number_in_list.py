ball=int(input('Balingizni kiriting: '))

if ball<=60:
  print(ball,' F===> You failed, hahaha')
elif ball>60 and ball<=70:
  print(ball,' D===> Qoniqarli')
elif ball>70 and ball<=80:
  print(ball,' C===> Yaxshi')
elif ball>80 and ball<=90:
  print(ball,' B===> A\'lo ')
elif ball>90 and ball<=100:
  print(ball, 'A===> Zo\'r')
else:
  print('Error')