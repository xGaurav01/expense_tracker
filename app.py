from flask import Flask
from routes.user_routes import user_bp
from routes.expense_routes import expense_bp
from config.init_db import init_db

app = Flask(__name__)

# Register routes
app.register_blueprint(user_bp)
app.register_blueprint(expense_bp)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
