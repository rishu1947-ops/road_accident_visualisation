import pandas as pd
import folium
from folium.plugins import MarkerCluster, HeatMap

# Load the dataset
file_path = "Road Accident Data.csv"
data = pd.read_csv(file_path)

# Clean the Local_Authority_(District) column for consistent matching.
data['Local_Authority_(District)'] = data['Local_Authority_(District)'].astype(str).str.strip().str.lower()
print(data['Local_Authority_(District)'].dropna().unique())

# Get user input and clean it.
area = input("Enter the area name: ").strip().lower()

# Filter data for the specified area.
area_data = data[data['Local_Authority_(District)'] == area]

if area_data.empty:
    print("No accident found in the area or the area is not present.")
else:
    print("Accident data found for the area!")
    
    # Convert Latitude and Longitude to numeric.
    area_data['Latitude'] = pd.to_numeric(area_data['Latitude'], errors='coerce')
    area_data['Longitude'] = pd.to_numeric(area_data['Longitude'], errors='coerce')
    
   
        # Define your mapping 
    severity_mapping = {
            'slight': 2,
            'serious': 5,
            'fatal': 8
        }
    area_data['Accident_Severity'] = area_data['Accident_Severity'].astype(str).str.strip().str.lower().map(severity_mapping)
   
    
    # Drop rows with NaNs in any key column.
    accident_locations = area_data[['Latitude', 'Longitude', 'Accident_Severity']].dropna(subset=['Latitude', 'Longitude', 'Accident_Severity'])
    
    if accident_locations.empty:
        print("No valid accident data with proper location information found after cleaning.")
    else:
        
        # Create a map centered on the average location.
        map_center = [accident_locations['Latitude'].mean(), accident_locations['Longitude'].mean()]
        
        if any(pd.isna(coord) for coord in map_center):
            print("Computed map center contains NaN values. Please check your data.")
        else:
            accident_map = folium.Map(location=map_center, zoom_start=10)
    
          
            # 1. Create marker clusters with markers colored based on severity.
            
            severity_clusters = {}
            for _, row in accident_locations.iterrows():
                severity = row['Accident_Severity']
    
                # Create a MarkerCluster for this severity if it doesn't exist yet.
                if severity not in severity_clusters:
                    cluster = MarkerCluster(name=f"Severity {severity}").add_to(accident_map)
                    severity_clusters[severity] = cluster
    
                # Choose a color based on severity thresholds.
                if severity < 3:
                    color = 'green'    # Lower severity (e.g., slight)
                elif severity < 7:
                    color = 'orange'   # Moderate severity (e.g., serious)
                else:
                    color = 'red'      # High severity (e.g., fatal)
    
                folium.Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=f"Accident Severity: {severity}",
                    icon=folium.Icon(color=color, icon='info-sign')
                ).add_to(severity_clusters[severity])
    
           
            # 2. Create a weighted heat map layer to colorize areas based on the
            #    frequency of accidents and their severity.
           
            # Prepare the data: list of [latitude, longitude, weight]
            heat_data = accident_locations[['Latitude', 'Longitude', 'Accident_Severity']].values.tolist()
    
            # Define a gradient for the heat map.
            gradient = {"0.2": 'green', "0.5": 'orange', "1.0": 'red'}

            HeatMap(
            heat_data,
            gradient=gradient,
            min_opacity=0.2,
            radius=25,
            blur=10,
            max_zoom=1
            ).add_to(accident_map)

    
            # Add layer control
            folium.LayerControl().add_to(accident_map)
    
            # Save the map to an HTML file.
            output_file = "accident_clusters_heatmap.html"
            accident_map.save(output_file)
            print("Map saved")
