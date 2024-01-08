from flask import Flask
import ctypes
import time
from flask_cors import CORS

i = 0

def bilhaopython():
    global i
    for _ in range(1000000000):
        i += 1

app = Flask(__name__)

CORS(app)

lib = ctypes.CDLL("./python-flask/functions.so")


@app.route("/")
def inicio():
    return "/python para 1 bilhao em python, /c para 1 bilhao em c e /cpp para 1 bilhao em cpp"
@app.route("/python")
def umbilhaopython():
    global i
    i = 0 
    start_time = time.time()
    bilhaopython()
    exec_time = time.time()
    return "1 bilhão em python: " + str(exec_time - start_time) + " segundos"

@app.route("/c")
def umbilhaoc():
    start_time = time.time()
    lib.bilhaoc()
    exec_time = time.time()
    return "1 bilhão em c: " + str(exec_time - start_time) + " segundos"

@app.route("/cpp")
def umbilhaocpp():
    start_time = time.time()
    lib.bilhaocpp()
    exec_time = time.time()
    return "1 bilhão em cpp: " + str(exec_time - start_time) + " segundos"

if __name__ == "__main__":
    app.run()


