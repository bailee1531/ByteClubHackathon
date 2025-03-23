from simData import log_sim_data
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Center
from textual.widgets import Button, Header
from csv import writer

## Creates the app class
class ButtonsApp(App[str]):
    CSS_PATH = "buttons.tcss"   # css file for docking the header and setting margins

    # creates the simulated data csv file
    with open('simdata.csv', 'w', newline='') as f:
        dataWriter = writer(f)
        dataWriter.writerow(['DateTime', 'Temperature', 'Pressure', 'Wind Speed'])    # Sets column headers

    ## Creates the buttons
    def compose(self) -> ComposeResult:
        yield Header()  # calls the docked header
        yield Horizontal(
            Center(Button("No Weather Events", variant='primary', name='No Weather Events')),
            Center(Button.success("Rain", name='Rain')),
            Center(Button.warning("Hurricane Event", name='Hurricane Event')),
            Center(Button.error("Tornado Event", name='Tornado Event'))
        )   # buttons are centered and in a horizontal line
    
    ## Sets the title written in the header
    def on_mount(self) -> None:
        self.title = "Weather Data Simulator"

    ## Event listener for button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        # if the label is 'stop event', then the button has already been pressed
        # if the button has already been pressed, then the script to log simulated data has already run
        if str(event.button.label) == 'Stop Event':
            event.button.label = event.button.name
        # if the label is anything else, then it is the name of the simulated weather event
        # if the label shows a simulated weather event, then it needs to log simulated data
        else:
            event.button.label = 'Stop Event'   # change the label
            log_sim_data(str(event.button.name))    # passes the name because it does not change

if __name__ == "__main__":
    app = ButtonsApp()
    app.run()