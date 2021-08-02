class UserRole:
    ADMIN = 'admin'
    DEFAULT = 'default'


message = 'admin defaultS'
message = message.split()
for mes in message:
    if not (mes in UserRole.__dict__.values()):
        print('ues')
    else:
        print('HHHHH')
