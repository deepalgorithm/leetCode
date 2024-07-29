import re
import numpy as np
import pandas as pd
from datetime import datetime

# Define regex patterns for NMEA sentences
gngsa_pattern = re.compile(r'^\$GNGSA.*')
gnrmc_pattern = re.compile(r'^\$GNRMC.*')
gpgsv_pattern = re.compile(r'^\$GPGSV.*')

# Define the updated function to calculate CN0
def calculate_cn0(snr, bandwidth_hz=2046000):
    if snr is None:
        return None
    bw_db_hz = 10 * np.log10(bandwidth_hz)
    return snr + bw_db_hz

# Function to convert date and time from GNRMC to datetime
def convert_to_datetime(date_str, time_str):
    if date_str and time_str:
        try:
            return datetime.strptime(date_str + time_str.split('.')[0], '%d%m%y%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            return None
    return None

# Parse the NMEA file again and process the data
gngsa_data = []
gnrmc_data = []
gpgsv_data = []
gnrmc_datetimes = []

with open('C:/Users/hamin/Desktop/leetCode/route1_nmea.txt', 'r') as file:
    for line in file:
        if gngsa_pattern.match(line):
            gngsa_data.append(line.strip())
        elif gnrmc_pattern.match(line):
            gnrmc_data.append(line.strip())
            parts = line.split(',')
            datetime_str = convert_to_datetime(parts[9], parts[1])
            gnrmc_datetimes.append(datetime_str)
        elif gpgsv_pattern.match(line):
            gpgsv_data.append(line.strip())

# Fill datetime for GNGSA and GPGSV based on GNRMC datetimes
def fill_datetimes(data, datetime_list):
    extended_datetimes = []
    datetime_index = 0
    for _ in data:
        if datetime_index < len(datetime_list):
            extended_datetimes.append(datetime_list[datetime_index])
            datetime_index += 1
        else:
            extended_datetimes.append(datetime_list[-1])
    return extended_datetimes

# Generate datetime values for each record
gngsa_datetimes = fill_datetimes(gngsa_data, gnrmc_datetimes.copy())
gpgsv_datetimes = fill_datetimes(gpgsv_data, gnrmc_datetimes.copy())

# Process GPGSV data to calculate CN0
gpgsv_processed = []
for sentence, dt in zip(gpgsv_data, gpgsv_datetimes):
    parts = sentence.split(',')
    num_sats = int(parts[3])
    for i in range(4, len(parts) - 4, 4):
        if len(parts) > i+3 and parts[i+3]:
            snr = int(parts[i+3])
            cn0 = calculate_cn0(snr)
            gpgsv_processed.append([dt, parts[1], parts[2], parts[3], parts[i], parts[i+1], parts[i+2], snr, cn0])

# Create DataFrames
gngsa_df = pd.DataFrame([x.split(',') for x in gngsa_data], columns=['Type', 'Mode', 'Fix_Type', 'Sat_Used_01', 'Sat_Used_02', 'Sat_Used_03', 'Sat_Used_04', 'Sat_Used_05', 'Sat_Used_06', 'Sat_Used_07', 'Sat_Used_08', 'Sat_Used_09', 'Sat_Used_10', 'Sat_Used_11', 'Sat_Used_12', 'PDOP', 'HDOP', 'VDOP', 'Checksum'])
gngsa_df.insert(0, 'DateTime', gngsa_datetimes)

gnrmc_df = pd.DataFrame([x.split(',') for x in gnrmc_data], columns=['Type', 'UTC_Time', 'Status', 'Latitude', 'Lat_Hemisphere', 'Longitude', 'Long_Hemisphere', 'Speed_Over_Ground', 'Course_Over_Ground', 'Date', 'Magnetic_Variation', 'Variation_Hemisphere', 'Mode', 'Checksum'])
gnrmc_df.insert(0, 'DateTime', gnrmc_datetimes)

gpgsv_df = pd.DataFrame(gpgsv_processed, columns=['DateTime', 'MessageNumber', 'TotalMessages', 'TotalSatellites', 'SatellitePRN', 'Elevation', 'Azimuth', 'SNR', 'CN0'])

# Save to CSV
gnrmc_df.to_csv('C:/Users/hamin/Desktop/leetCode/GNRMC_data_corrected_with_datetime.csv', index=False)
gngsa_df.to_csv('C:/Users/hamin/Desktop/leetCode/GNGSA_data_corrected_with_datetime.csv', index=False)
gpgsv_df.to_csv('C:/Users/hamin/Desktop/leetCode/GPGSV_data_corrected_with_datetime.csv', index=False)

# Display DataFrames for verification
print("GNGSA Data:")
print(gngsa_df.head())
print("\nGNRMC Data:")
print(gnrmc_df.head())
print("\nGPGSV Data:")
print(gpgsv_df.head())
