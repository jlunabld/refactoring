import dash_bootstrap_components as dbc
from dash import html

def usage_comparison_chart_tab():
    """
    Creates and returns a dbc.Tab object for YTD Bldng Usage Comparison Chart.
    
    This function sets up the layout and style for the Usage Comparison Chart tab. 

    Returns:
        dbc.Tab: A Tab component object with label, style and child components defined.
    """
    
    # Creating a dbc.Tab object
    return dbc.Tab(
        # Setting the label of the tab
        label="YTD Bldng Usage Comparison Chart",
        
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
            id="YTD",
            
            # Setting the style of the Div
            style={"overflow": "scroll", "resize": "both"},
        )
    )