import npyscreen

class SettingsForm(npyscreen.FormBaseNewWithMenus):
    def create(self):
        self.m1 = self.add_menu(name="Main Menu", shortcut="^X")
        self.m1.addItem(text="Main View", onSelect=self.switch_to_main_view)
        self.m1.addItem(text="Close Menu", onSelect=self.close_menu, shortcut="c")
        self.m1.addItem(text="Exit Application", onSelect=self.exit_application, shortcut="e")
        self.add(npyscreen.TitleText, name="Text:", value="This is the settings view")

    def switch_to_main_view(self):
        self.parentApp.switchForm("MAIN")

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

    def close_menu(self):
        self.adjust_widgets()