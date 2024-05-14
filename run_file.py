#to run this file, uncomment the top part of your code and then run this file
#if you enter 1, this file will run your code with the input from test1.txt
# and output to output1.txt

import subprocess
n = input("Enter a single-digit test number: ")
myoutput = open("output"+n+".txt","w")
myinput = open("test"+n+".txt",encoding="ascii",errors="surrogateescape")
p1 = subprocess.check_call(['python',"proj05.py"],stdin=myinput,stdout=myoutput)
#myoutput.flush()
myinput.close()
myoutput.close()
