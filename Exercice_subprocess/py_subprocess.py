
from subprocess import Popen, PIPE


#cmd = ["cmd", "ssh", "10.0.0.12", "-l", "pi"]
cmd = ["cmd", "dir"]
p = Popen(cmd, stdin=PIPE, stdout=PIPE)
sout, serr = p.communicate(input=b"dir\n\r")
print(sout)

