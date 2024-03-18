from flask import Flask

# Nome do arquivo
app = Flask(__name__)

# Rota /
@app.route("/")
def hello_world():
  return "Hello world!"

# Rota /about
@app.route("/about")
def about():
  return "Página sobre"

# Rodar a aplicação em tempo de desenvolvimento
if __name__ == "__main__":
  app.run(debug=True)