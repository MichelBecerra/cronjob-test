from subprocess import Popen, PIPE

def iAmRunning():
    p = Popen(['ps aux --columns 200 | grep "[r]unner.py"'], shell=True, stdout=PIPE)
    texto = p.communicate()[0].decode("utf-8").strip()
    procesos=texto.split('\n')
    if len(procesos) > 1:
        return True
    else:
        return False

def processRunning(prog):
    initial = prog[0]
    rest = prog[1:]
    p = Popen(['ps aux --columns 200 | grep "[{}]{}"'.format(initial, rest)], shell=True, stdout=PIPE)
    texto = p.communicate()[0].decode("utf-8").strip()
    procesos=texto.split('\n')
    if len(procesos) > 1:
        return True
    else:
        return False