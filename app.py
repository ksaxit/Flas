from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///it.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sport.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Rab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    rabota = db.Column(db.String(300), nullable=False)
    staj = db.Column(db.String(300), nullable=False)
    about_rabota = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Rab %r>' % self.id


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    sports = db.Column(db.String(300), nullable=False)
    stage_sport = db.Column(db.String(300), nullable=False)
    about_sport = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Sport %r>' % self.id
class It(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    project = db.Column(db.String(300), nullable=False)
    reference = db.Column(db.String(300), nullable=False)
    about_project = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<It %r>' % self.id

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    secondname = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    about_you = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    game_name = db.Column(db.String(100), nullable=False)
    complexity = db.Column(db.String(100), nullable=False)
    passage = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Game %r>' % self.id


@app.route('/rabota')
def rabota():
    rabota = Rab.query.order_by(Rab.date.desc()).all()
    return render_template('rabota.html', rabota=rabota)


@app.route('/sport')
def sport():
    sport = Sport.query.order_by(Sport.date.desc()).all()
    return render_template('sport.html', sport=sport)


@app.route('/it')
def it():
    its = It.query.order_by(It.date.desc()).all()
    return render_template('it.html', its=its)
@app.route('/game')
def game():
    games = Game.query.order_by(Game.date.desc()).all()
    return render_template('game.html', games=games)


@app.route('/game/<int:id>')
def game_detail(id):
    games = Game.query.get(id)
    return render_template('game_detail.html', games=games)

@app.route('/from_here')
@app.route('/here')
def here():
    return render_template('index.html')



@app.route('/')
def about():
    return render_template('about.html')


@app.route('/Piatnica')
def piatnica():
    return render_template('Piatnica.html')


@app.route('/Dmitri')
def dmitri():
    return render_template('Dmitriy.html')


@app.route('/Stef')
def stef():
    return render_template('Stef.html')


@app.route('/create')
def create():
    article = Article.query.order_by(Article.date.desc()).all()
    return render_template('create.html', article=article)


@app.route('/create/<int:id>')
def create_detail(id):
    article = Article.query.get(id)
    return render_template('create_detail.html', article=article)


@app.route('/create/<int:id>/del')
def create_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/create')
    except:
        return 'При удалении произошла ошибка'


@app.route('/create/<int:id>/update', methods=["POST", "GET"])
def create_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.firstname = request.form['firstname']
        article.secondname = request.form['secondname']
        article.username = request.form['username']
        article.about_you = request.form['about_you']
        try:
            db.session.commit()
            return redirect('/create')
        except:
            return "При редактировании профиля возникла ошибка"

    else:
        return render_template('create_update.html', article=article)


@app.route('/create-article', methods=["POST", "GET"])
def create_article():
    if request.method == "POST":
        firstname = request.form['firstname']
        secondname = request.form['secondname']
        username = request.form['username']
        about_you = request.form['about_you']
        article = Article(firstname=firstname, secondname=secondname, username=username, about_you=about_you)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/create')
        except:
            return "При добавлении профиля возникла ошибка"

    else:
        return render_template('create_article.html')


@app.route('/create-game', methods=["POST", "GET"])
def create_game():
    if request.method == "POST":
        username = request.form['username']
        game_name = request.form['game_name']
        complexity = request.form['complexity']
        passage = request.form['passage']
        games = Game(username=username, game_name=game_name, complexity=complexity, passage=passage)
        try:
            db.session.add(games)
            db.session.commit()
            return redirect('/game')
        except:
            return "При добавлении профиля возникла ошибка"

    else:
        return render_template('create_game.html')


@app.route('/game/<int:id>/update', methods=["POST", "GET"])
def game_update(id):
    games = Game.query.get(id)
    if request.method == "POST":
        games.username = request.form['username']
        games.game_name = request.form['game_name']
        games.complexity = request.form['complexity']
        games.passage = request.form['passage']
        try:
            db.session.commit()
            return redirect('/game')
        except:
            return "При редактировании профиля возникла ошибка"

    else:
        return render_template('game_update.html', games=games)


@app.route('/create-it', methods=["POST", "GET"])
def create_it():
    if request.method == "POST":
        username = request.form['username']
        project = request.form['project']
        reference = request.form['reference']
        about_project = request.form['about_project']
        its = It(username=username, project=project, reference=reference, about_project=about_project)
        try:
            db.session.add(its)
            db.session.commit()
            return redirect('/it')
        except:
            return "При добавлении профиля возникла ошибка"

    else:
        return render_template('create_it.html')

if __name__ == '__main__':

    app.run(debug=True)