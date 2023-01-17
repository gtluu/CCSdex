from flask import render_template, url_for, redirect, request, session
from CCSdex import app, CCSdexSearch


@app.route('/')
def ccsdex():
    form = CCSdexSearch(request.form)
    return render_template('ccsdex.html', title='CCSdex', form=form)
