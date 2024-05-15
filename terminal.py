import subprocess

while True:
    commande = input("Entrez une commande: ")
    if commande == "exit":
        break

    result = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)

    print(result.stdout)
    print(result.stderr)
