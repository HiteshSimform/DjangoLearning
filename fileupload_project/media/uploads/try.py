import dash
from dash import dcc, html
import folium
from dash.dependencies import Input, Output
from geopy.distance import geodesic

# Initialize the Dash app
app = dash.Dash(__name__)

# Coordinates for the start and end points
start_coords = (40.748817, -73.985428)  # Times Square, New York
end_coords = (40.689247, -74.044502)  # Statue of Liberty, New York

# Additional waypoints for possible alternative paths
waypoints = [
    (40.730610, -73.935242),  # Waypoint 1
    (40.741895, -73.989308),  # Waypoint 2
    (40.758896, -73.985130),  # Waypoint 3
]

# Function to create a Folium map and return the HTML representation
def create_map(start_coords, end_coords, path_coords=[]):
    m = folium.Map(location=start_coords, zoom_start=13)

    # Add markers for the start and end locations
    folium.Marker(start_coords, popup="Start (Times Square)").add_to(m)
    folium.Marker(end_coords, popup="End (Statue of Liberty)").add_to(m)

    # Add the paths (for all possible paths and the shortest path)
    for path in path_coords:
        folium.PolyLine(path, color='blue', weight=3, opacity=0.7).add_to(m)

    # Return the HTML representation of the map to embed it in Dash
    return m._repr_html_()

# Function to calculate geodesic distance between two points
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

# Function to find the shortest path based on waypoints and start/end coordinates
def find_shortest_path(start, end, waypoints):
    # Manually define all possible paths (start -> waypoint(s) -> end)
    possible_paths = [
        [start, waypoints[0], end],  # Path 1: start -> waypoint 1 -> end
        [start, waypoints[1], end],  # Path 2: start -> waypoint 2 -> end
        [start, waypoints[2], end],  # Path 3: start -> waypoint 3 -> end
        [start, waypoints[0], waypoints[1], end],  # Path 4: start -> waypoint 1 -> waypoint 2 -> end
        [start, waypoints[1], waypoints[2], end],  # Path 5: start -> waypoint 2 -> waypoint 3 -> end
        [start, waypoints[0], waypoints[2], end],  # Path 6: start -> waypoint 1 -> waypoint 3 -> end
    ]

    # Calculate the total distance for each path
    path_distances = []
    for path in possible_paths:
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += calculate_distance(path[i], path[i+1])
        path_distances.append((path, total_distance))

    # Find the shortest path
    shortest_path = min(path_distances, key=lambda x: x[1])
    return shortest_path, path_distances

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Live Path Map with User Input"),
    
    # Latitude and Longitude input fields
    html.Div([
        html.Label("Enter Latitude for New Point:"),
        dcc.Input(id="lat-input", type="number", value=start_coords[0], step=0.0001),
        html.Label("Enter Longitude for New Point:"),
        dcc.Input(id="lon-input", type="number", value=start_coords[1], step=0.0001),
        html.Button("Update Path", id="update-button", n_clicks=0),
    ]),

    # Div to hold the map
    html.Div(id="map-container"),
])

# Callback to update the map when user inputs new coordinates
@app.callback(
    Output("map-container", "children"),
    [Input("update-button", "n_clicks")],
    [dash.dependencies.State("lat-input", "value"),
     dash.dependencies.State("lon-input", "value")]
)
def update_map(n_clicks, lat, lon):
    if n_clicks > 0:
        # Update the waypoint to the new point
        new_point = (lat, lon)
        # Add the new point to the waypoints list (in case you want to test it)
        updated_waypoints = waypoints + [new_point]

        # Find all possible paths and the shortest path
        shortest_path, path_distances = find_shortest_path(start_coords, end_coords, updated_waypoints)

        # Create the map with all paths and highlight the shortest path
        map_html = create_map(start_coords, end_coords, [path for path, _ in path_distances])

        return html.Div([
            html.H3("Shortest Path (Distance: {:.2f} km)".format(shortest_path[1])),
            html.Iframe(srcDoc=map_html, width="100%", height="600px")
        ])

    return "Enter coordinates and click 'Update Path'"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
