from flask import Flask, render_template, redirect, url_for
from config import Config
from project.forms import SelectForms
from room_choose_class import DoorChoose

app = Flask(__name__)
app.config.from_object(Config)


# Главная страница (кэп)
@app.route('/')
def menu():
    return render_template('menu.html')


# При любом адресе перенаправляем пользователя на главную страницу
@app.route('/<string:any>/')
def menu_any(any):
    return render_template('menu.html')


# Выбор стороны, направления, комнаты
@app.route('/side_choices/', methods=['get', 'post'])
def side_choices():
    form = SelectForms()
    if form.validate_on_submit():
        global select1, select2, select3
        select1 = form.select_side.data
        select2 = form.select_dir.data
        select3 = form.select_room.data

        # Выбор осуществляется с помощью класса
        if DoorChoose(select1, select2, select3).door_choose():
            url = f'{DoorChoose(select1, select2, select3).door_choose()}'
            return redirect(url_for(url))

    return render_template('side_choices.html', form=form)


# Далее идут роуты дверей и комнат

# Tip map
@app.route('/tip_map/')
def tip_map():
    return render_template('doors_html/tip_map.html')


# Common closed door
@app.route('/closed_door/')
def closed_door():
    # Changing the string name of the room to digital
    global select3
    room_dict = {'Вторая комната': 2,
                 'Третья комната': 3,
                 'Четвёртая комната': 4}
    
    return render_template('doors_html/closed_door.html',
                           side=select1,
                           direction=select2,
                           room_number=room_dict[select3])


# Common closed room
@app.route('/closed_room/')
def closed_room():
    return render_template('rooms_html/closed_room.html')


# Left side, from you
# first door
@app.route('/left_side/from_you/first_door/')
def left_side_from_you_first_door():
    return render_template('doors_html/left-side-from-u/first_door.html')


# first room
@app.route('/left_side/from_you/first_room/')
def left_side_from_you_first_room():
    return render_template('rooms_html/left-side-from-u/first_room.html')


# second door
@app.route('/left_side/from_you/second_door/')
def left_side_from_you_second_door():
    return render_template('doors_html/left-side-from-u/second_door.html')


# second room
@app.route('/left_side/from_you/second_room/')
def left_side_from_you_second_room():
    return render_template('rooms_html/left-side-from-u/second_room.html')


# Left side, on you
# final door
@app.route('/left_side/on_you/final_door/')
def left_side_on_you_final_door():
    return render_template('doors_html/left-side-on-u/final_door.html')


# final room
@app.route('/left_side/on_you/final_room/')
def left_side_on_you_final_room():
    return render_template('rooms_html/left-side-on-u/final_room.html')


# first door
@app.route('/left_side/on_you/first_door/')
def left_side_on_you_first_door():
    return render_template('doors_html/left-side-on-u/first_door.html')


# first room
@app.route('/left_side/on_you/first_room/')
def left_side_on_you_first_room():
    return render_template('rooms_html/left-side-on-u/first_room.html')


# third door
@app.route('/left_side/on_you/third_door/')
def left_side_on_you_third_door():
    return render_template('doors_html/left-side-on-u/third_door.html')


# third room
@app.route('/left_side/on_you/third_room/')
def left_side_on_you_third_room():
    return render_template('rooms_html/left-side-on-u/third_room.html')


# Right side, from you
# first door
@app.route('/right_side/from_you/first_door/')
def right_side_from_you_first_door():
    return render_template('doors_html/right-side-from-u/first_door.html')


# first room
@app.route('/right_side/from_you/first_room/')
def right_side_from_you_first_room():
    return render_template('rooms_html/right-side-from-u/first_room.html')


# tip door
@app.route('/right_side/from_you/tip_door/')
def right_side_from_you_tip_door():
    return render_template('doors_html/right-side-from-u/tip_door.html')


# tip room
@app.route('/right_side/from_you/tip_room/')
def right_side_from_you_tip_room():
    return render_template('rooms_html/right-side-from-u/tip_room.html')


# Right side, on you
# first door
@app.route('/right_side/on_you/first_door/')
def right_side_on_you_first_door():
    return render_template('doors_html/right-side-on-u/first_door.html')


# first room
@app.route('/right_side/on_you/first_room/')
def right_side_on_you_first_room():
    return render_template('rooms_html/right-side-on-u/first_room.html')


# second door
@app.route('/right_side/on_you/second_door/')
def right_side_on_you_second_door():
    return render_template('doors_html/right-side-on-u/second_door.html')


# second room
@app.route('/right_side/on_you/second_room/')
def right_side_on_you_second_room():
    return render_template('rooms_html/right-side-on-u/second_room.html')


# third door
@app.route('/right_side/on_you/third_door/')
def right_side_on_you_third_door():
    return render_template('doors_html/right-side-on-u/third_door.html')


# third room
@app.route('/right_side/on_you/third_room/')
def right_side_on_you_third_room():
    return render_template('rooms_html/right-side-on-u/third_room.html')
