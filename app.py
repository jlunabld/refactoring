from dash import Dash, html
import dash_bootstrap_components as dbc

# Importing individual tabs from separate modules
from savings_opportunities_tab import savings_opportunities_tab
from usage_comparison_chart_tab import usage_comparison_chart_tab


class RMSDashboard:
    """
    Class to represent a Dash application.
    This class handles the setup and running of the application.
    """

    def __init__(self):
        """
        Initializes the Dash application and sets the layout.
        """
        # Create the Dash application with external Bootstrap stylesheet
        self.app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])  
        # Set the layout of the application
        self.set_layout()

    def set_layout(self):
        """
        Sets the layout of the Dash application to a Container with a Div.
        """
        self.app.layout = dbc.Container(
            [
                self.create_div()  # Call the create_div method to create the div
            ]
        )

    def create_div(self):
        """
        Creates and returns a Div object with a CardHeader containing the application tabs.
        """
        return html.Div(
            [
                dbc.CardHeader(
                    self.create_tab()  # Call the create_tab method to create the tabs
                )
            ],
            className='my-custom-class'  # Add custom CSS class to the Div
        )

    def create_tab(self):
        """
        Creates and returns a Tabs object with two tabs imported from separate modules.
        """
        return dbc.Tabs(
            [
                savings_opportunities_tab(),  # Call the savings_opportunities_tab function to create the first tab
                usage_comparison_chart_tab()  # Call the usage_comparison_chart_tab function to create the second tab
            ]
        )

    def run(self, debug=False):
        """
        Runs the Dash application server.

        :param debug: Boolean to decide if debug mode should be enabled. Default is False.
        """
        self.app.run_server(debug=debug)

# Create the Dash application server
server = RMSDashboard().app.server

if __name__ == '__main__':
    # Instantiate the RMSDashboard class
    my_app = RMSDashboard()
    # Run the application with debug mode enabled
    my_app.run(debug=True)