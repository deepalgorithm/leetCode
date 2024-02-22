from geopy.distance import distance

def calculate_destination_coordinates(start_lat, start_lon, start_alt, distance_meters, bearing_deg):
    # Calculate destination coordinates using Haversine formula
    destination_point = distance(meters=distance_meters).destination((start_lat, start_lon), bearing_deg)

    # Extract destination latitude, longitude, and altitude
    dest_lat = destination_point.latitude
    dest_lon = destination_point.longitude
    dest_alt = start_alt  # Assuming the altitude doesn't change in this example

    return dest_lat, dest_lon, dest_alt


start_latitude = 37.7749
start_longitude = -122.4194
start_altitude = 0  
distance_to_destination = 100 
bearing_to_destination = 26.698415 

destination_latitude, destination_longitude, destination_altitude = calculate_destination_coordinates(
    start_latitude, start_longitude, start_altitude, distance_to_destination, bearing_to_destination
)

print(f"Destination Latitude: {destination_latitude}")
print(f"Destination Longitude: {destination_longitude}")
print(f"Destination Altitude: {destination_altitude}")
