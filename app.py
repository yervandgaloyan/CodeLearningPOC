from flask import Flask, request
import io, sys
import subprocess

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hi"

@app.route('/run/<code>', methods=['GET'])
def run(code):
    # #keep a named handle on the prior stdout 
    # old_stdout = sys.stdout 
    # #keep a named handle on io.StringIO() buffer 
    # new_stdout = io.StringIO() 
    # #Redirect python stdout into the builtin io.StringIO() buffer 
    # sys.stdout = new_stdout

    # exec(code)
    # #stdout from mycode is read into a variable
    # result = sys.stdout.getvalue().strip()

    # #put stdout back to normal 
    # sys.stdout = old_stdout 
    
    # print(str(result)) 
    # return str(result)
   

    proc = subprocess.Popen(['python3', 'run.py',  code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.communicate()[0]