from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired


class SelectForms(FlaskForm):
    # Формы, выбор стороны, выбор направления, выбор комнаты
    select_side = SelectField('', choices=['Левая сторона', 'Правая сторона'])

    select_dir = SelectField('', choices=['От Вас', 'На Вас'])

    select_room = RadioField('',
                             choices=[('Первая комната', 1),
                                      ('Вторая комната', 2),
                                      ('Третья комната', 3),
                                      ('Четвёртая комната', 4)],
                             validators=[DataRequired()])

    # Кнопка Принять
    submit = SubmitField('Принять')
