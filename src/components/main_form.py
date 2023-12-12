import npyscreen, curses
from components.main_grid import MainGrid

class MainForm(npyscreen.FormBaseNewWithMenus):
    """
    This class represents the main view form.

    Attributes:
        search_field (SearchBar): The search bar widget.
        m1 (Menu): The main menu.
        grid (MainGrid): The main grid widget.
        button (ButtonPress): The button widget. Currently just a debug tool.

    Methods:
        create(): Creates the main view form.
        filter_values(input): Filters grid values based on the input in the search field.
        button_pressed(): Handles the button press event.
        exit_application(): Exits the application.
        close_menu(): Closes the menu.
        switch_to_settings(): Switches to the settings form.
    """

    def create(self):
        """
        Creates the main view form.
        """
        self.search_field = self.add(SearchBar, name="Search:", value="")
        # The menu bar
        self.m1 = self.add_menu(name="Main Menu", shortcut="^X")
        self.m1.addItem(text="Settings", onSelect=self.switch_to_settings)
        self.m1.addItem(text="Close Menu", onSelect=self.close_menu, shortcut="c")
        self.m1.addItem(text="Exit Application", onSelect=self.exit_application, shortcut="e")

        self.grid = self.add(MainGrid, max_height=10, rely=5, select_whole_line=True, always_show_cursor=False)
        self.grid.create()

        self.button = self.add(npyscreen.ButtonPress, name="Nappi", when_pressed_function=self.button_pressed)

    def filter_values(self, input):
        """
        Filters grid values based on the input in the search field.

        Args:
            input (str): The input in the search field.
        """
        search_text = input.lower()
        all_values = self.grid.get_values()
        #compare to first column values
        new_values = [value for value in all_values if value[0].lower().startswith(search_text)]
        self.grid.update_values(new_values)

    def button_pressed(self):
        """
        Handles the button press event.
        """
        # Add your code here to handle the button press event
        pass
        npyscreen.notify_confirm(self.search_field.value, "Information")

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

    def close_menu(self):
        self.adjust_widgets()

    def switch_to_settings(self):
        curses.beep()
        self.parentApp.switchForm("SETTINGS")

class SearchBar(npyscreen.TitleText):
    def when_value_edited(self):
        self.parent.parentApp.getForm("MAIN").filter_values(self.value)