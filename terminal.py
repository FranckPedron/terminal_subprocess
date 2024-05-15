import subprocess

result = subprocess.run("dir", shell=True, capture_output=True, universal_newlines=True)

print(result.stdout)
