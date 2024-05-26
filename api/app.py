from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed

from api.models.models import *

from api.routes.match_bp import *
from api.controllers.matchController import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ahcestgang'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://default:VfXQ8iymq9HM@ep-lively-morning-a4ukm3yw-pooler.us-east-1.aws.neon.tech:5432/verceldb"
app.config['SQLACHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)

app.register_blueprint(match_bp, url_prefix=None)


@app.route("/")
def index():
    return redirect(url_for('match_bp.liste'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')