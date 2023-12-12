#!/usr/bin/env python
# encoding: utf-8

import npyscreen, curses

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm(cycle_widgets=True))

class MainForm(npyscreen.FormBaseNewWithMenus):
    def create(self):
        self.search_field = self.add(SearchBar, name="Search:", value="")
        # The menus
        self.m1 = self.add_menu(name="Main Menu", shortcut="^X")
        self.m1.addItem(text="Debug", onSelect=self.debug)
        self.m1.addItem(text="Close Menu", onSelect=self.close_menu, shortcut="c")
        self.m1.addItem(text="Exit Application", onSelect=self.exit_application, shortcut="e")

        self.grid = self.add(MainGrid, max_height=10, rely=5, select_whole_line=True, always_show_cursor=False)
        self.grid.create()

        self.button = self.add(npyscreen.ButtonPress, name="Nappi", when_pressed_function=self.button_pressed)

    def filter_values(self, input):
        """Filters grid values based on the input in the search field"""
        search_text = input.lower()
        old_values = self.grid.values
        """compare to first column values"""
        new_values = [value for value in old_values if value[0].lower().startswith(search_text)]
        self.grid.update_values(new_values)

    def button_pressed(self):
        npyscreen.notify_confirm(self.search_field.value, "Information")

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

    def close_menu(self):
        self.adjust_widgets()

    def debug(self, input):
        curses.beep()

class SettingForm(npyscreen.FormBaseNewWithMenus):
    def create(self):
        pass

class MainGrid(npyscreen.GridColTitles):
    def create(self):
        self.col_titles = ["APP", "USERNAME", "PASSWORD"]
        self.values = [["Facebook", "robajansson@gmail.com", "*****************"],
                       ["Steam", "robaxxx", "***************"],
                       ["Instagram", "rouubert", "***************"]]
        
    def update_values(self, values):
        self.values = values
        self.update()

class PopUp(npyscreen.Popup):
    def create(self):
        self.add(npyscreen.TitleText, name="Text:", value="This is a popup")

class SearchBar(npyscreen.TitleText):
    def when_value_edited(self):
        self.parent.parentApp.getForm("MAIN").filter_values(self.value)
    
def main():
    TA = MyTestApp()
    TA.run()

if __name__ == '__main__':
    main()