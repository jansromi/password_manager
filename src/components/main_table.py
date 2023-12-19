from textual.widgets import DataTable

class MainTable(DataTable):
    """
    A custom grid component for displaying data.

    Attributes:
        pwm: The passwordmanager instance, which is used for calls with database.
        column_labels: The column titles.
        original_rows: The original values.
        filtered_rows: The values that are currently being displayed.
        column_keys: The column keys.
        row_keys: The row keys.

    Methods:
        on_mount: Called when the component is mounted.
        filter_table: Filters the table based on the given string.
        on_data_table_row_selected: Called when a row is selected.
        update_values: Sets the values to be displayed and refreshes the grid.
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

    def update_values(self, values):
        """
        Sets the values to be displayed and refreshes the grid.
        """
        self.clear()
        self.filtered_rows = values
        self.add_rows(self.filtered_rows)
