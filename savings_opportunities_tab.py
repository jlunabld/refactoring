import dash_bootstrap_components as dbc
from dash import html

def savings_opportunities_tab():
    """
    Creates and returns a dbc.Tab object for Savings Opportunities.
    
    This function sets up the layout and style for the Savings Opportunities tab. 

    Returns:
        dbc.Tab: A Tab component object with label, style and child components defined.
    """
    
    # Creating a dbc.Tab object
    return dbc.Tab(
        # Setting the label of the tab
        label="Savings Opportunities",
        
        # Setting the CSS class names for the tab
        className="border-primary text-dark",
        
        # Setting the style for the tab using a dictionary
        style={
            "backgroundColor": "transparent",
            "opacity": 1,
            "padding": "1px",
        },
        
        # Setting the active label class name for the tab
        active_label_class_name="selected-tab",
        
        # Setting the children for the tab. In this case, a Div is being created.
        children=html.Div(
            # Setting the id of the Div
            id="Savings",
            
            # Setting the style of the Div
            style={"overflow": "scroll", "resize": "both"},
        )
    )