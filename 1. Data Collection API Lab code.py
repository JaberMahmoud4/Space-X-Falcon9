"""
Professional SpaceX Launches Data Extraction, Enrichment, Cleaning, and Export

This script fetches SpaceX launches data, filters, enriches via API endpoints,
cleans missing values, and exports a ready-to-use CSV file.
"""

import requests
import pandas as pd
import numpy as np
import datetime

# Display settings for pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# API endpoints
SPACEX_LAUNCHES_URL = "https://api.spacexdata.com/v4/launches/past"
STATIC_JSON_URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json"

def get_booster_versions(data):
    booster_versions = []
    for rocket_id in data['rocket']:
        if rocket_id:
            response = requests.get(f"https://api.spacexdata.com/v4/rockets/{rocket_id}").json()
            booster_versions.append(response.get('name'))
        else:
            booster_versions.append(None)
    return booster_versions

def get_launch_sites(data):
    launch_sites, longitudes, latitudes = [], [], []
    for launchpad_id in data['launchpad']:
        if launchpad_id:
            response = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}").json()
            launch_sites.append(response.get('name'))
            longitudes.append(response.get('longitude'))
            latitudes.append(response.get('latitude'))
        else:
            launch_sites.append(None)
            longitudes.append(None)
            latitudes.append(None)
    return launch_sites, longitudes, latitudes

def get_payload_data(data):
    payload_masses, orbits = [], []
    for payload_id in data['payloads']:
        if payload_id:
            response = requests.get(f"https://api.spacexdata.com/v4/payloads/{payload_id}").json()
            payload_masses.append(response.get('mass_kg'))
            orbits.append(response.get('orbit'))
        else:
            payload_masses.append(None)
            orbits.append(None)
    return payload_masses, orbits

def get_core_data(data):
    blocks, reused_counts, serials = [], [], []
    outcomes, flights, gridfins, reused, legs, landingpads = [], [], [], [], [], []
    for core in data['cores']:
        if core.get('core') is not None:
            response = requests.get(f"https://api.spacexdata.com/v4/cores/{core['core']}").json()
            blocks.append(response.get('block'))
            reused_counts.append(response.get('reuse_count'))
            serials.append(response.get('serial'))
        else:
            blocks.append(None)
            reused_counts.append(None)
            serials.append(None)
        outcomes.append(f"{core.get('landing_success')} {core.get('landing_type')}")
        flights.append(core.get('flight'))
        gridfins.append(core.get('gridfins'))
        reused.append(core.get('reused'))
        legs.append(core.get('legs'))
        landingpads.append(core.get('landpad'))
    return blocks, reused_counts, serials, outcomes, flights, gridfins, reused, legs, landingpads

def fetch_and_prepare_data():
    # Try static JSON first, fallback to live API if not available
    response = requests.get(STATIC_JSON_URL)
    if response.status_code == 200:
        data_json = response.json()
    else:
        response = requests.get(SPACEX_LAUNCHES_URL)
        data_json = response.json()

    # Normalize JSON to DataFrame
    data = pd.json_normalize(data_json)

    # Keep relevant columns
    columns = ['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']
    data = data[columns]

    # Remove launches with multiple cores/payloads
    data = data[data['cores'].map(len) == 1]
    data = data[data['payloads'].map(len) == 1]

    # Extract single core/payload from lists
    data['cores'] = data['cores'].map(lambda x: x[0])
    data['payloads'] = data['payloads'].map(lambda x: x[0])

    # Convert date_utc to datetime.date
    data['date'] = pd.to_datetime(data['date_utc']).dt.date

    # Restrict launches to <= 2020-11-13
    cutoff_date = datetime.date(2020, 11, 13)
    data = data[data['date'] <= cutoff_date]

    return data

def main():
    # Prepare and filter launch data
    data = fetch_and_prepare_data()

    # Enrich features using additional API calls
    print("Fetching Booster Versions...")
    booster_versions = get_booster_versions(data)
    print("Fetching Launch Sites...")
    launch_sites, longitudes, latitudes = get_launch_sites(data)
    print("Fetching Payload Data...")
    payload_masses, orbits = get_payload_data(data)
    print("Fetching Core Data...")
    blocks, reused_counts, serials, outcomes, flights, gridfins, reused, legs, landingpads = get_core_data(data)

    # Compose final DataFrame dictionary
    launch_dict = {
        'FlightNumber': list(data['flight_number']),
        'Date': list(data['date']),
        'BoosterVersion': booster_versions,
        'PayloadMass': payload_masses,
        'Orbit': orbits,
        'LaunchSite': launch_sites,
        'Outcome': outcomes,
        'Flights': flights,
        'GridFins': gridfins,
        'Reused': reused,
        'Legs': legs,
        'LandingPad': landingpads,
        'Block': blocks,
        'ReusedCount': reused_counts,
        'Serial': serials,
        'Longitude': longitudes,
        'Latitude': latitudes
    }
    launch_df = pd.DataFrame(launch_dict)

    # Filter for Falcon 9 launches
    data_falcon9 = launch_df[launch_df['BoosterVersion'] != 'Falcon 1'].copy()
    data_falcon9['FlightNumber'] = range(1, data_falcon9.shape[0]+1)

    # Fill missing PayloadMass with its mean (no chained assignment warning)
    payload_mean = data_falcon9['PayloadMass'].mean()
    data_falcon9['PayloadMass'] = data_falcon9['PayloadMass'].fillna(payload_mean)

    # Fill missing LandingPad values with 'N/A'
    data_falcon9['LandingPad'] = data_falcon9['LandingPad'].fillna('N/A')

    # Show missing values (should be zero for PayloadMass and LandingPad)
    print("\nMissing values per column after cleaning:")
    print(data_falcon9.isnull().sum())

    # Export cleaned DataFrame to CSV
    export_path = 'dataset_part_1.csv'
    data_falcon9.to_csv(export_path, index=False)
    print(f"\nCleaned dataset exported to '{export_path}'.")

if __name__ == "__main__":
    main()