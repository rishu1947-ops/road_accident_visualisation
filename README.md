# road_accident_visualisation

# Road Accident Data Visualization by Area

This project provides a Python script to visualize road accident data for a specific Local Authority District using interactive maps generated with the Folium library. The script reads accident data from a CSV file, filters it based on user input, and creates an HTML map displaying accident locations as colored markers within clusters and a weighted heatmap indicating accident density and severity.

## Features

-   Loads road accident data from a CSV file.
-   Allows the user to specify a Local Authority District to analyze.
-   Filters the dataset for the selected area.
-   Generates an interactive HTML map centered on the selected area.
-   Displays individual accident locations as colored markers grouped in clusters based on severity (Slight, Serious, Fatal).
-   Includes a weighted heatmap layer that visualizes accident density and severity across the area.
-   Provides a layer control to toggle between marker clusters and the heatmap.

## Prerequisites

-   Python 3.x
-   The following Python libraries: `pandas`, `folium`.
-   The Road Accident (United Kingdom (UK)) Dataset from Kaggle.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rishu1947-ops/road_accident_visualisation
    cd rishu1947-ops
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Obtain the dataset:**
    The dataset file is too large to be stored directly in this repository. You need to download it from its original source:
    *   Go to the Kaggle dataset page: [Road Accident (United Kingdom (UK)) Dataset](https://www.kaggle.com/datasets/silverbottle/road-accident-united-kingdom-uk-dataset)
    *   Download the dataset (you may need a Kaggle account and agree to the dataset's terms). Look for a download button or link for the entire dataset.
    *   The downloaded file might be a zip archive containing `Road Accident Data.csv`. Extract the `Road Accident Data.csv` file.
    *   **Place the `Road Accident Data.csv` file in the same directory as the `map_accidents_by_area.py` script.**

## How to Run

1.  Make sure you have completed the setup steps and have placed the `Road Accident Data.csv` file in the correct directory.
2.  Run the Python script from your terminal:
    ```bash
    python map_accidents_by_area.py
    ```
3.  The script will prompt you to "Enter the area name". Type the name of the Local Authority District you want to visualize (e.g., "Leeds", "Birmingham") and press Enter. The script will also print a list of unique districts found in your data, which can help you enter a valid name.
4.  If data is found for the area, an HTML file named `accident_map_area.html` will be generated in the same directory.
5.  Open the `accident_map_area.html` file in your web browser to view the interactive map.

## Output

-   An HTML file (`accident_map_area.html`) containing the interactive map.

## Code Explanation

-   The script starts by loading the data using pandas.
-   It cleans the 'Local\_Authority\_(District)' column for easier matching.
-   It takes user input for the area name and filters the data.
-   Latitude and Longitude columns are converted to numeric, coercing errors to `NaN`.
-   'Accident\_Severity' is mapped to numeric values (2, 5, 8 for Slight, Serious, Fatal).
-   Rows with missing location or severity data are removed.
-   A Folium map is created, centered on the average location of the remaining data points.
-   Accident locations are added as markers, grouped into `MarkerCluster` layers colored based on severity.
-   A `HeatMap` layer is added, weighted by accident severity, to show accident hotspots.
-   A `LayerControl` is added to the map, allowing users to toggle the visibility of the Marker Clusters and Heatmap layers.
-   The final map is saved as an HTML file.

## Potential Improvements (TODO)

-   Add more robust error handling for invalid user input.
-   Allow specifying the input CSV file path as a command-line argument.
-   Provide options for different base map tiles.
-   Implement filters based on other data columns (e.g., date, time, type of accident).
-   Add popups with more detailed accident information on marker click.
-   Create separate heatmaps or clusters for different types of accidents.
-   Improve the severity mapping and heatmap gradient for better visualization clarity.
-   Add basic data summary statistics for the selected area.
