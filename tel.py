
class Phone:
  def __init__(self,name, model, weight, color):
    self.name=name
    self.model=model
    self.weight=weight
    self.color=color

  def info(self):
    print(f'Hi, information about your phone==>\nName:{self.name}\nModel:{self.model}\nWeight:{self.weight}\nColor:{self.color} ')


my_phone=Phone('Samsung galaxy A05s','Samsung',400,'gray')

print(my_phone.name)
print(my_phone.color)

my_phone.info()


























