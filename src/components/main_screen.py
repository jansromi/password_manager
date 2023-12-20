from textual import on
from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Header, Input, DataTable, Footer, ListView
from textual.screen import Screen
from textual.reactive import reactive

from components.sidebar import Sidebar
from components.main_table import MainTable

class Searchbar(Input):

    filter = ""

    def watch_input(self, value):
        print("value changed")
        #self.parent.query_one(MainTable).filter(value)

    @on(Input.Changed)
    def on_input_changed(self, event):
        table = self.app.query_one(MainTable)
        updated_rows = table.filter_table(event.value)
        table.update_values(updated_rows)

    def compose(self) -> ComposeResult:
        self.border_title = "Search"
        return super().compose()

class MainScreen(Screen):

    AUTO_FOCUS = "#search"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Sidebar(classes="-hidden"),
            Vertical(
                Vertical(Searchbar(id="search"), id="top_container"),
                Vertical(MainTable(id="table", cursor_type="row"), id="bottom_container")
            ),
        )
        yield Footer()

    def action_show_menu(self) -> None:
        sidebar = self.query_one(Sidebar)
        self.set_focus(None)
        if not sidebar.isOpen():
            sidebar.set_context()
            sidebar.open_sidebar()
            self.set_focus(sidebar.query_one(ListView))
            return
        if sidebar.isOpen():
            sidebar.close_sidebar()
            # voisi katsoa, onko joku menun valinta valittuna,
            # jos on, niin suljettaessa palataan hakuun.
            # nyt palataan hakuun joka tapauksessa
            # joten jos valittuna sidebarin ulkopuolinen asia,
            # niin menee tyhmästi
            self.set_focus(self.query_one("#search"))
        
