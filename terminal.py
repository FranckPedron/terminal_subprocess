import os
import subprocess

while True:
    commande = input(os.getcwd() + " > ")
    if commande == "exit":
        break

    commande_split = commande.split(" ")
    if len(commande_split) == 2 and commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1])
        except FileNotFoundError:
            print("Répertoire invalide")
    else:
        result = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)

        print(result.stdout)
        print(result.stderr)
