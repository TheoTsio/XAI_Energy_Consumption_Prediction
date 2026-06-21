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

# Test run. You can change frequency to '5min', '10min', '1H', etc.
merged_data = merge_data_from_different_sensors_in_same_building('Data/NORD', frequency='10min')
print(merged_data.to_csv('Data/merged_nord.csv', index=False))
