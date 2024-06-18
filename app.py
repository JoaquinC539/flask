from flask import Flask
from waitress import serve
import os
import sys
import psycopg2
from src.controllers.user_controller import user_bp
from src.controllers.index_controller import index_bp
from src.controllers.vendedor_controller import vendedor_bp
from dotenv import load_dotenv
ruta_relativa = os.path.join(os.path.dirname(__file__), '.')
ruta_absoluta = os.path.abspath(ruta_relativa)
sys.path.append(ruta_absoluta)
load_dotenv()

app=Flask(__name__)

app.config["DATABASE_URL"]=f"postgresql://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}@{"DATABASE_HOST"}/{"DATABASE_NAME"}"


app.register_blueprint(index_bp)
app.register_blueprint(user_bp)
app.register_blueprint(vendedor_bp)
if __name__ == '__main__':
    serve(app,host="0.0.0.0",port=7500)