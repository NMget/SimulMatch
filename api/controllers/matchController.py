from flask import render_template, request, flash, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SubmitField, StringField, HiddenField, SelectField
from wtforms.validators import InputRequired, ValidationError

from api.models.models import *

class createMatch(FlaskForm):
    id_field = HiddenField()
    poule = SelectField('Poule')
    team1 = SelectField('Equipe 1', [InputRequired()])
    team2 = SelectField('Equipe 2', [InputRequired()])
    submit = SubmitField('Créer')

def liste():
    matchs = Match.query.filter(Match.resultat == 0).order_by(Match.id_poule)
    team = Team
    poule = Poule
    return render_template('bone.html', content='index.html', matchs = matchs, team=team, poule=poule)


def create():
    form = createMatch()
    form.poule.choices = [(g.name) for g in Poule.query.order_by('name')]
    form.team1.choices = [(e.name) for e in Team.query.order_by('name')]
    form.team2.choices = [(i.name) for i in Team.query.order_by('name')]
    if form.validate_on_submit():
        poule = Poule.query.filter(Poule.name == form.poule.data).first()
        team1 = Team.query.filter(Team.name == form.team1.data).first()
        team2 = Team.query.filter(Team.name == form.team2.data).first()
        id_poule = poule.id
        id_team1 = team1.id
        id_team2 = team2.id
        record = Match(id_poule, id_team1, id_team2, 0)
        db.session.add(record)
        db.session.commit()

        return redirect(url_for('match_bp.liste'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form, field).label.text,
                    error
                ), 'error')
    return render_template('bone.html', content='createMatch.html', form=form)


def jouer(id):
    match = Match.query.filter(Match.id == id).first()
    team1 = Team.query.filter(Team.id == match.id_team1).first()
    team2 = Team.query.filter(Team.id == match.id_team2).first()
    p1 = 0
    p2 = 0
    return render_template('bone.html', content='jouerMatch.html',match=match, team1=team1, team2=team2, p1=p1, p2=p2)

def resMatch(match, team):
    match = Match.query.filter(Match.id == match).first()
    liaison = Liaison.query.filter(Liaison.id_poule == match.id_poule, Liaison.id_team == team).first()
    if match.id_team1 == team:
        match.resultat = 1
    else:
        match.resultat = 2

    liaison.points += 1


    db.session.commit()

    return redirect(url_for('match_bp.liste'))
    