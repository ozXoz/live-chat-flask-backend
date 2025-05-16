from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import mongo, jwt

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
CORS(app)
mongo.init_app(app)
jwt.init_app(app)

# Optional Debug Check
with app.app_context():
    print("✅ Connected to DB:", mongo.db.name)  # You should see your DB name printed

# Import and register blueprints
from auth.routes import auth_bp
from protected.routes import protected_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(protected_bp, url_prefix="/api")

@app.route("/")
def index():
    return {"msg": "Flask API running"}

if __name__ == "__main__":
    app.run(debug=True)
