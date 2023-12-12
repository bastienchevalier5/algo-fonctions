def motdepasse (lettre):
    lettre = "*"
    print(lettre,end="")

mot = input("Saisir un mot")
for i in mot:
    motdepasse(i)
    
