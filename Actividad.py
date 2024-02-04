from cryptography.fernet import Fernet

# Fredy
key = Fernet.generate_key()

print('key: ', key)
f = Fernet(key)
token = f.encrypt(b'MILANESA DE POLLO')
print('token: ', token)


# Alonso
f1 = Fernet(b'YXEwJ3I6W06odgHBf2sX_HM6ein2CiKKlxcU_kGwaPE=')

message = f1.decrypt(b'gAAAAABluxCsg376WPvVbPTT-xFOS0GSLhZBBq0EmiJVIpRThcbzoeZJYVx-Hcacfy-SUF1xASzRxmMjPwM5Z-8zMeTd4elOLrWhpdzFjwdYWR928hHuEwY=')
print('\nmessage:', message)

