enter=int(input('Son kiriting: '))
enter=f"{enter}"#int ni str ga o'tkazish
if enter==enter[::-1]:
  print(enter, '==>bu son polidroid')
else:
  print(enter, '==>bu son polidroid emas')