from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Prime Number Checker</title>
</head>
<body>
    <h1>Prime Number Checker</h1>
    <form method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Check</button>
    </form>
    {% if result is not none %}
        <h2>{{ result }}</h2>
    {% endif %}
</body>
</html>
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        number = int(request.form["number"])
        if is_prime(number):
            result = f"{number} is a prime number!"
        else:
            result = f"{number} is not a prime number."
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

