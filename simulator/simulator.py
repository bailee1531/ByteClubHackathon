from simData import log_sim_data
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Center
from textual.widgets import Button, Header
from csv import writer

class ButtonsApp(App[str]):
    CSS_PATH = "buttons.tcss"

    with open('simdata.csv', 'w', newline='') as f:
        dataWriter = writer(f)
        dataWriter.writerow(['DateTime', 'Temperature', 'Pressure', 'Wind Speed'])    # Sets column headers
        
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
        if str(event.button.label) == 'Stop Event':
            event.button.label = event.button.name
            log_sim_data(str(event.button.name))
        else:
            event.button.label = 'Stop Event'
            log_sim_data(str(event.button.name))

if __name__ == "__main__":
    app = ButtonsApp()
    app.run()