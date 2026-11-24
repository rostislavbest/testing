from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Мій Flask сайт</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 100px;
            background: #f0f0f0;
        }

        h1 {
            color: #333;
        }

        button {
            padding: 10px 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Привіт, Flask!</h1>
    <p>Це мій перший Flask-застосунок.</p>
    <button onclick="alert('Працює!')">Натисни мене</button>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)