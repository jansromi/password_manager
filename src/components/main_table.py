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
        self.pwm = self.app.PWM
        self.column_labels = self.pwm.get_entry_columns()
        self.original_rows = self.pwm.get_entries()
        self.filtered_rows = self.original_rows
        self.column_keys = self.add_columns(*self.column_labels)
        self.row_keys = self.add_rows(self.filtered_rows)
    
    def filter_table(self, filter):
        """
        Returns a list of rows that contain the filter string.
        """
        filtered_array = [
            item
            for item in self.original_rows
            if filter.lower() in item[0].lower() or filter.lower() in item[1].lower()
        ]
        return filtered_array

    def on_data_table_row_selected(self, event):
        print("row selected")
        print(event.row)

    def update_values(self, values):
        """
        Sets the values to be displayed and refreshes the grid.
        """
        self.clear()
        self.filtered_rows = values
        self.add_rows(self.filtered_rows)
