class TV():
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")

TV_set = TV()
TV_set.show_status()
TV_set.turn_on()
TV_set.show_status()
TV_set.turn_off()
TV_set.show_status()