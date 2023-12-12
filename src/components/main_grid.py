import npyscreen
import services.database as database

class MainGrid(npyscreen.GridColTitles):
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

    def create(self):
        self.db = database.Database()
        self.col_titles = self.db.get_fake_columns()
        self.all_values = self.db.get_fake_values()
        self.values = self.all_values
    
    def get_values(self):
        return self.all_values

    def update_values(self, values):
        self.values = values
        self.update()