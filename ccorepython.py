#instance classes


class employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj1=employee("gowthami",23)
# obj2=employee("s",23)
# print(obj1)
# print(obj2)
# print(obj1.name,obj1.age)
# print(obj2.name, obj2.age)



# class Car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color

# obj1=Car("benzz","olive") 
# print(obj1.brand,obj1.color)       



#PLOYMORPHYSM::
# FOR EXAMPLE
class person():
    def __init__(self,name,action):
        self.name=name
        self.action=action

    def dance(self):
        print("sing and dance")


class  cat():
    def __init__(self,name,action):
        self.name=name
        self.action=action

    def dance(self):
        print("move and jump")    


obj1=person("gowthami","sing")     
obj2=cat("jimmy","drink")   

for x  in (obj1,obj2):
    x.dance()



print(obj1.name,obj1.action)
print(obj2.name,obj2.action)


print("hello world")
