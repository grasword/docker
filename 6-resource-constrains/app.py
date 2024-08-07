from flask import Flask
app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/')
def index():
    result = fibonacci(30)  # CPU-intensive task
    return f"Fibonacci result: {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')