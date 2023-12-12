import npyscreen
import services.database as database

class MainGrid(npyscreen.GridColTitles):
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