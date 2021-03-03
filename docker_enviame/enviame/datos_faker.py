import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enviame.settings')

import django
django.setup()

from faker import Faker  
from empresa.models import Empresa

for i in range(50):
    fake = Faker() 
    name = fake.company()
    address = fake.country()
    phone = fake.phone_number()
    email = fake.email()
    business_sector = fake.job()
    legal_representative  = fake.name()

    empresa = Empresa.objects.get_or_create(name = name, address=address, phone=phone, email=email, business_sector=business_sector,legal_representative=legal_representative)
    #print(empresa)