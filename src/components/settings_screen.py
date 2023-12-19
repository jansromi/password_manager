from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Header, Footer, ListView, ListItem, Label
from src.components.sidebar import Sidebar

class SettingsScreen(Screen):
    
    AUTO_FOCUS = "#settings_listview"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Sidebar(classes="-hidden"),
            ListView(
                ListItem(Label("Change password"), id="change_password"),
                ListItem(Label("Change username"), id="change_username")
            , id="settings_listview")
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
            # jos on, niin suljettaessa palataan listviewiin
            self.set_focus(self.query_one("#settings_listview"))