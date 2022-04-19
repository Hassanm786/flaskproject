from application import app, db
from application.models import Fighter, Roster, AddFighter, AddRoster
from flask import redirect, url_for, request, render_template


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/add_fighter', methods=['GET', 'POST'])
def add_fighter():
    form = AddFighter()
    if form.validate_on_submit():
        new_fighter = Fighter(name=form.name.data, country=form.country.data)
        db.session.add(new_fighter)
        db.session.commit()
        return redirect(url_for('add_fighter'))
    else:
        return render_template('add_fighter.html', form=form)

@app.route('/view_fighter')
def view_fighter():
    all_fighters = Fighter.query.all()
    return render_template('view_fighter.html', all_fighters=all_fighters)

@app.route('/update_fighter/<string:name>',methods = ['GET','POST'])
def update_fighter(name):
    form = AddFighter()
    if request.method == 'POST':
        update_fighter = Fighter.query.filter_by(name=name).first()
        if update_fighter: 
            update_fighter.name = request.form['name']
            update_fighter.country = request.form['country']
            db.session.commit()
            return redirect(url_for('view_fighter'))
        return f"no fighter named = {name} exists"
    else:
        return render_template('update_fighter.html', form=form, name=name)

@app.route('/delete_fighter/<string:name>', methods=['GET', 'POST'])
def delete_fighter(name):
    fighter = Fighter.query.filter_by(name=name).first()
    if fighter:
        db.session.delete(fighter)
        db.session.commit()
        return redirect(url_for('view_fighter'))
    else:
        return render_template('view_fighter.html', name=name)

@app.route('/add_fighter_to_roster', methods=['GET', 'POST'])
def add_fighter_to_roster():
    form = AddRoster()
    if form.validate_on_submit():
        new_signing = Roster(weight_class=form.weight_class.data, rank=form.rank.data, fighter_name=form.fighter_name.data)
        db.session.add(new_signing)
        db.session.commit()
        return redirect(url_for('add_fighter_to_roster'))
    else:
        return render_template('add_fighter_to_roster.html', form=form)

@app.route('/view_roster')
def view_roster():
    current_roster = Roster.query.all()
    return render_template('view_roster.html', current_roster=current_roster)

@app.route('/update_roster/<int:id>',methods = ['GET', 'POST'])
def update_roster(id):
    form = AddRoster()
    if request.method == 'POST':
        update_roster = Roster.query.filter_by(id=id).first()
        if update_roster: 
            update_roster.weight_class = request.form['weight_class']
            update_roster.rank = request.form['rank']
            update_roster.fighter_name = request.form['fighter_name']
            db.session.commit()
            return redirect(url_for('view_roster'))
    else:
        return render_template('update_roster.html', form=form, id=id)

@app.route('/release_fighter/<int:id>', methods=['GET', 'POST'])
def release_fighter(id):
    release_fighter = Roster.query.filter_by(id=id).first()
    if release_fighter:
        db.session.delete(release_fighter)
        db.session.commit()
        return redirect(url_for('view_roster'))
    else:
        return render_template('view_roster.html', id=id)

