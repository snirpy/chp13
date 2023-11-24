import re

passwords = "P@ssw0rd, strongP@ss, 12345678, WeakPassword, !/_y@$K0rr1"

# Votre expression régulière ici
pattern = re.compile(r'')  # À compléter

# Utilisez la méthode findall pour obtenir tous les mots de passe valides
valid_passwords = pattern.findall(passwords)

# Affichez les mots de passe valides
print("Mots de passe valides :", valid_passwords)



