import subprocess

run_shell = subprocess.run(['ls', './'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(run_shell)
test = str(run_shell.stdout.decode()).split('\n') # decode method make the output clearer

for element in test:
    if not element: 
        continue
    print(bool(element))
    print(f"Plik: {element}")
print("Info: {}".format(run_shell.stderr.decode())) # stderr method start working when directory of file ['ls', """"'./any'""""] doesn't exists