from flask import Blueprint

from api.controllers.matchController import *

match_bp = Blueprint('match_bp',__name__)

match_bp.route('/', methods=['GET', 'POST'])(liste)
match_bp.route('/creerMatch', methods=['GET', 'POST'])(create)
match_bp.route('/jouer/<id>', methods=['GET', 'POST'])(jouer)
match_bp.route('/resMatch/<match>/<team>', methods=['GET', 'POST'])(resMatch)
