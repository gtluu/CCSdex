from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField


class CCSdexSearch(FlaskForm):
    compound_id = StringField('ID')
    compound = StringField('Compound')
    mz = FloatField('m/z')
    mz_tol = FloatField('m/z Tolerance')
    mz_tol_mode = SelectField('m/z Tolerance Mode', choices=[('Da', 'Da'),
                                                             ('ppm', 'ppm')])
    ccs = FloatField('CCS')
    ccs_tol = FloatField('CCS Tolerance')
    ccs_tol_mode = SelectField('CCS Tolerance Mode', choices=[('\u00c5', '\u00c5'),
                                                              ('%', '%')])
    charge = IntegerField('Charge')
    adduct = SelectField('Adduct', choices=[('M+H', 'M+H'),
                                            ('M+Na', 'M+Na')])
    smiles = StringField('SMILES')
    inchi = StringField('InChI')
    submit = SubmitField('Search')
