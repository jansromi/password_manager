from textual.widgets import DataTable

import services.database as database

class MainTable(DataTable):
    """
    A custom grid component for displaying data.

    Attributes:
        db (database.Database): An instance of the database class.
        col_titles (list): A list of column titles.
        all_values (list): A list of all values.
        values (list): A list of current values to be displayed.

    Methods:
        create(): Initializes the grid by setting up the database, column titles, and values.
        get_values(): Returns all values.
        update_values(values): Updates the values to be displayed and refreshes the grid.
    """

    def on_mount(self):
        self.db = database.Database()
        columns = self.db.get_fake_columns()
        self.add_columns(*columns)
        self.add_rows(self.db.get_fake_values())
    
    def get_values(self):
        return self.all_values

    def update_values(self, values):
        self.values = values
        self.update()