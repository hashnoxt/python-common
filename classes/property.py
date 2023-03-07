
class Human:

    Name = 'Dave Willson'

    def __init__(self, name):
        self.name = name
        self._age = 0

    def say(self, msg):
        return f'Fire {msg} Flying'

    @classmethod
    def get_name(cls):
        return cls.Name

    @staticmethod
    def get_age():
        return 12

    @property
    def test_prop(self):
        return self._age 


    @test_prop.setter
    def test_prop(self,age):
        self._age = age 
    
    @test_prop.deleter
    def test_prop(self,age):
        del self._age

i = Human('New Human')

x = i.say('is')

cls_Name = i.get_name()
cls_age = i.get_age()

i.test_prop = 5

print(i.test_prop)

del i.test_prop

print(i.test_prop)