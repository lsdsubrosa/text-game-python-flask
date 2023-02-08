from dataclasses import dataclass


@dataclass
class DoorChoose:
    select1: str
    select2: str
    select3: str
    url_str: str = ''

    def door_choose(self):
        # Left side, from you
        if self.select1 == 'Левая сторона' and self.select2 == 'От Вас' and self.select3 == 'Первая комната':
            self.url_str = 'left_side_from_you_first_door'
        elif self.select1 == 'Левая сторона' and self.select2 == 'От Вас' and self.select3 == 'Вторая комната':
            self.url_str = 'left_side_from_you_second_door'

        # Left side, on you
        elif self.select1 == 'Левая сторона' and self.select2 == 'На Вас' and self.select3 == 'Четвёртая комната':
            self.url_str = 'left_side_on_you_final_door'
        elif self.select1 == 'Левая сторона' and self.select2 == 'На Вас' and self.select3 == 'Первая комната':
            self.url_str = 'left_side_on_you_first_door'
        elif self.select1 == 'Левая сторона' and self.select2 == 'На Вас' and self.select3 == 'Третья комната':
            self.url_str = 'left_side_on_you_third_door'

        # Right side, from you
        elif self.select1 == 'Правая сторона' and self.select2 == 'От Вас' and self.select3 == 'Первая комната':
            self.url_str = 'right_side_from_you_first_door'
        elif self.select1 == 'Правая сторона' and self.select2 == 'От Вас' and self.select3 == 'Третья комната':
            self.url_str = 'right_side_from_you_tip_door'

        # Right side, on you
        elif self.select1 == 'Правая сторона' and self.select2 == 'На Вас' and self.select3 == 'Первая комната':
            self.url_str = 'right_side_on_you_first_door'
        elif self.select1 == 'Правая сторона' and self.select2 == 'На Вас' and self.select3 == 'Вторая комната':
            self.url_str = 'right_side_on_you_second_door'
        elif self.select1 == 'Правая сторона' and self.select2 == 'На Вас' and self.select3 == 'Третья комната':
            self.url_str = 'right_side_on_you_third_door'

        else:
            return 'closed_door'

        return self.url_str
