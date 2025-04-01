register= {'name': 'José', 
           'catchPhrase': 'Implemented secondary concept',
           'bs': 'e-enable extensible e-tailers'}

# {'id': 9, 'name': 'Glenna Reichert', 'username': 'Delphine', 'email': 'Chaim_McDermott@dana.io', 


# 'address': {'street': 'Dayna Park', 'suite': 'Suite 449', 'city': 'Bartholomebury', 
# 'zipcode': '76495-3109', 'geo': {'lat': '24.6463', 'lng': '-168.8889'}},

#  'phone': '(775)976-6794 x41206', 'website': 'conrad.com', 'company': {'name': 'Yost and Sons', 
# 'catchPhrase': 'Switchable contextually-based project', 'bs': 'aggregate real-time technologies'}}

register['name'] = 'samuel'
print(register['name'])


print("Existe o nome samuel no registro? ",'samuel' in register.values())


register['teste']= 123


print("Items do dicionário:",len(register))

print(register.keys())
print(register.values())
print(register.items())
