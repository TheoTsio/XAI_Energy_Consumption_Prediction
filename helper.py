import os 
import pandas as pd

def merge_data_from_different_sensors_in_same_building(path, columns_to_keep_from_each_sensor = ['Date and Time', 'TMP indoor', 'HUM indoor', 'CO2 indoor', 'VOCT indoor', 'DBAA indoor', 'DBAP indoor', 'LIGHT_LUX indoor', 'OCCUPANCY_RATE indoor'], frequency='15min'):
    '''
    This function merges data from different sensors in the same building.

    Give as input the path to the folder containing the data from a building.    
    '''
    list_of_sensor_dataframes = []

    for file in os.listdir(path):
        if file.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(path, file))
            
            # Catch different naming conventions for the time column and normalize them!
            if 'DateTime' in df.columns:
                df = df.rename(columns={'DateTime': 'Date and Time'})
            
            # Safely extract the room name (Salle)
            if 'Salle' in df.columns:
                salle_name = df['Salle'].iloc[0]
            else:
                # Based on your changes, grab it from the filename
                salle_name = str(file).split('_')[0]
                
            # Filter down to the exact columns to keep
            cols_to_keep = [col for col in columns_to_keep_from_each_sensor if col in df.columns]
            
            # Just in case the time column dropped from cols_to_keep but existed:
            if 'Date and Time' not in cols_to_keep and 'Date and Time' in df.columns:
                cols_to_keep.append('Date and Time')
                
            df = df[cols_to_keep]

            # Standardize the Datetime to align misaligned timestamps!
            if 'Date and Time' in df.columns:
                df['Date and Time'] = pd.to_datetime(df['Date and Time'])
                # Set 'Date and Time' to be the index of the dataframe momentarily
                df = df.set_index('Date and Time')
            else:
                print(f"Skipping {file} because it lacks a Date and Time column")
                continue
            
            # Resample the data taking the mean
            df = df.resample(frequency).mean()

            # Append the suffix to these numeric columns 
            rename_dict = {col: f"{col} {salle_name}" for col in df.columns}
            df = df.rename(columns=rename_dict)
            
            list_of_sensor_dataframes.append(df)
            print(f"Processed nicely: {file}")

    # Concatenate them all together on their standardized 'Date and Time' Index
    if list_of_sensor_dataframes:
        merged_df = pd.concat(list_of_sensor_dataframes, axis=1)
        merged_df = merged_df.reset_index()
        return merged_df
        
    return pd.DataFrame()

def merge_sensor_and_power_data(sensor_df, power_df, frequency='10min'):
    """
    Merges the sensor dataframe and the power dataframe.
    It aligns them by matching 'Date and Time' from the sensors so that it falls 
    within the [Horodatage_Début, Horodatage_Fin) interval of the power data.
    Keeps only the consumption values (Valeur) aggregated to completely match sensor frequency!
    """
    sensor_df = sensor_df.copy()
    power_df = power_df.copy()

    # 1. Normalize sensor datetime
    sensor_df['Date and Time'] = pd.to_datetime(sensor_df['Date and Time'])
    if sensor_df['Date and Time'].dt.tz is not None:
        sensor_df['Date and Time'] = sensor_df['Date and Time'].dt.tz_localize(None)
    
    # 2. Normalize power datetimes completely ignoring their explicit string offsets (e.g., '+01:00')
    # This prevents any timezone shifting and ensures it strictly matches the raw "clock time" of the sensors.
    power_df['Horodatage_Début'] = pd.to_datetime(power_df['Horodatage_Début'].astype(str).str[:19])
    power_df['Horodatage_Fin'] = pd.to_datetime(power_df['Horodatage_Fin'].astype(str).str[:19])

    # 3. Filter power_df to keep only the consumption value!
    if 'Nature_Mesure' in power_df.columns:
        power_df = power_df[power_df['Nature_Mesure'] == 'CONSOMMATION']
    
    cols_to_keep = ['Horodatage_Début', 'Horodatage_Fin', 'Valeur', 'Consommation']
    power_df = power_df[[c for c in cols_to_keep if c in power_df.columns]]
    
    # 3b. Aggregate energy consumption across exactly matching intervals sizes (e.g. '10min')
    if frequency:
        # Round the sensor datetimes to the chosen frequency to align as best as possible!
        sensor_df['Date and Time'] = sensor_df['Date and Time'].dt.round(frequency)
        # Sum the energy consumption over the new intervals to capture any 2x5min splits!
        power_df = power_df.set_index('Horodatage_Début').resample(frequency).sum(numeric_only=True).reset_index()
        # Mathematically create the exact Horodatage_Fin
        power_df['Horodatage_Fin'] = power_df['Horodatage_Début'] + pd.Timedelta(frequency)
    
    # 4. Sort both dataframes for exactly matching them using merge_asof
    sensor_df = sensor_df.sort_values('Date and Time')
    power_df = power_df.sort_values('Horodatage_Début')
    
    # 5. Use nearest merge_asof to match exactly or closest interval
    merged = pd.merge_asof(
        sensor_df, 
        power_df,
        left_on='Date and Time',
        right_on='Horodatage_Début',
        direction='nearest',
        tolerance=pd.Timedelta(frequency) / 2 if frequency else None
    )
    
    # 6. Filter out rows where 'Date and Time' safely exceeded 'Horodatage_Fin'
    if 'Horodatage_Fin' in merged.columns:
        merged = merged[merged['Date and Time'] < merged['Horodatage_Fin']]

    return merged
