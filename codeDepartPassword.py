import re

passwords = "1P@ssw0rd5, str0ngP@ss1, 12345678, WeakPassword,!/_y@$K0rr1, m#r0uanE444"

# Séparer les mots de passe par des virgules (sans prendre en compte les espaces après les virgules)
password_list = re.split(r'\s*,\s*', passwords)

# Expression régulière pour un mot de passe valide (sans espace)
pattern = re.compile(r'^(?!.*\s)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*/_]).{8,}$')

# Utilisez la méthode findall pour obtenir tous les mots de passe valides
valid_passwords = [password for password in password_list if pattern.match(password)]

#*****************************************
# valid_passwords = []
# for password in password_list:
#     if pattern.match(password):
#         valid_passwords.append(password)
#*****************************************


# Affichez les mots de passe valides
print("Mots de passe valides :", valid_passwords)
