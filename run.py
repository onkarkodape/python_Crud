from src import app

# app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='127.0.0.1:3000', port=5000,debug= True)
