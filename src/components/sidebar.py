from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import ListView, ListItem, Label, Static

class Sidebar(Container):
    
    def compose(self) -> ComposeResult:
        yield Title("")
        yield MenuListView(id="sidebar_listview")

    def _on_mount(self) -> None:
        self.add_class("-hidden")

    def open_sidebar(self):
        self.remove_class("-hidden")
        self.add_class("-active")
    
    def close_sidebar(self):
        self.remove_class("-active")
        self.add_class("-hidden")

    def isOpen(self):
        """Returns True if sidebar is open, False if not."""
        return self.has_class("-active")
    
    def set_context(self):
        self.query_one(Title).renderable = "dashboard" if self.app.current_mode == "main" else "settings" if self.app.current_mode == "settings" else None
        self.query_one(MenuListView).set_label_title(
            label_title = "settings" if self.app.current_mode == "main" else "dashboard" if self.app.current_mode == "settings" else None
        )

class MenuListView(ListView):
    def compose(self) -> ComposeResult:
        yield ListItem(Label("", id="label_settings_dashboard"), id="settings_dashboard")
        yield ListItem(Label("Help"), id="help")
        yield ListItem(Label("Exit"), id="exit")

    def on_list_view_selected(self, selected) -> None:
        current_mode = self.app.current_mode
        if current_mode == "main" and selected.item.id == "settings_dashboard":
            self.parent.close_sidebar()
            self.app.switch_mode("settings")
            return
        
        if current_mode == "settings" and selected.item.id == "settings_dashboard":
            self.parent.close_sidebar()
            self.app.switch_mode("main")
            return
        
        if selected.item.id == "help":
            self.app.notify(message="Help is not implemented yet", title="Help")
            

    def set_label_title(self, label_title):
        label = self.query_one("#label_settings_dashboard")
        label.renderable = label_title

class Title(Static):
    pass