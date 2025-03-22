from dataLogger import log_sense_data
from dataLogger import log_sim_data
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Center
from textual.widgets import Button, Header


class ButtonsApp(App[str]):
    CSS_PATH = "buttons.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Center(Button("No Weather Events", variant='primary', name='No Weather Events')),
            Center(Button.success("Rain", name='Rain')),
            Center(Button.warning("Hurricane Event", name='Hurricane Event')),
            Center(Button.error("Tornado Event", name='Tornado Event'))
        )
    
    def on_mount(self) -> None:
        self.title = "Weather Data Simulator"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if str(event.button.name) == 'No Weather Events':
            log_sense_data(True)
        elif str(event.button.label) == 'Stop Event':
            log_sim_data(False)
            event.button.label = event.button.name
        else:
            log_sim_data(True)
            event.button.label = 'Stop Event'


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())