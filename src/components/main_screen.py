from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Header, Input, DataTable, Footer, ListView
from textual.screen import Screen

from components.sidebar import Sidebar
from components.main_table import MainTable

class MainScreen(Screen):
    AUTO_FOCUS = "#search"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Sidebar(classes="-hidden"),
            Vertical(
                Vertical(Input("Search", id="search"), id="top_container"),
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
        

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        #table.add_columns(*ROWS[0])
        #table.add_rows(ROWS[1:])