from flask import Flask, render_template_string

app = Flask(__name__)

# Define an HTML template with CSS styles
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #000; /* Black background */
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1); /* Semi-transparent overlay */
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        }
        h1 {
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        p {
            margin: 0;
            font-size: 1.2em;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Hello, Aaron Lim!</h1>
        <p>Welcome to your enhanced Flask web application.</p>
    </div>
</body>
</html>
"""

@app.route("/")
def hello_world():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)

