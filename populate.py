import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','vrreal.settings')


import django
django.setup()

import random
from build.models import Prop

from faker import Faker

fakegen = Faker()

city = ['hyderabad','bangalore','chennai','noida','pune','mumbai','warangal','kanpur','hubli']

def state(s):
    if s == 'hyderabad' or s=='warangal':
        return 'Telangana'
    if s == 'mumbai' or s == 'pune':
        return 'Maharasthra'
    if s == 'noida' or s=='kanpur':
        return 'uttarpradesh'
    if s == 'bangalore' or s=='hubli':
        return 'Karnataka'
    return 'notassigned'
    

vastu = ['east','north','west','south']

def populate(N=10):

    for entry in range(N):

        fake_city =random.choice(city)
        fake_state = state(fake_city)
        fake_vastu = random.choice(vastu)+'facing'
        fake_cost = random.randint(1000,2000)
        fake_f = fakegen.name()+fakegen.name()

        p = Prop.objects.create(city=fake_city,state=fake_state,vastu=fake_vastu,facilities=fake_f);
        p.save()

if __name__=='__main__':
    print("Populating data....;))))")
    populate(50)
    print('Completed')


        









