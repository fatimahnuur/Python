

class Inson: 
  def __init__(self, ismi, familiya,age,job,city): #xususiyatlarini e'lon qilish, method classga tegishli funksiya.
    self.ismi=ismi
    self.familiya=familiya
    self.age=age
    self.job=job
    self.city=city

    

odam1=Inson('Fatima','Isaqova',20,'programmer','Fergana')
print(odam1.ismi)
print(odam1.job)
print(odam1.city)