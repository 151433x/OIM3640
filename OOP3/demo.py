import random

class covid:
    """this is a class of Covid, each covid should have a base seq and a extension"""
    base_sequence="1234567890"
    def __init__(self,new_seq='new sequence'):
        if random.random() <.9:
            self.extension=new_seq
            self.sequence=self.base_sequence+self.extension
        else:
            self.sequence=self.base_sequence
    def replicate(self):
        """return a new covid instace by replicating itself"""
        new_covid=covid(self.extension,name='new'+self.name) # means call __init__(self,new_seq=self.extension)
        return new_covid
    def add(self,another_covid):
        new_seq=''.join(random.choices(self.extension+another_covid.extension,k=3))
        return covid(name='new covid from mixing',new_seq=new_seq)
    def __str__(self):
        """represents the instance in a human readable format"""
        return f'{self.name}:{self.sequence}'
        


covid_0=covid(name='ground zero',) # creating an instance of covid by invoking the initilizaing method, __init__
covid_1=covid(name='second case', new_seq='123')
covid_2=covid_1.replicate()

print(covid_0.sequence)
print(covid_1.sequence)
print(covid_2.sequence)
print(covid_2.mix(covid_0).sequence)