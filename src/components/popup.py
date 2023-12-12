import npyscreen

class PopUp(npyscreen.Popup):
    def create(self):
        self.add(npyscreen.TitleText, name="Text:", value="This is a popup")