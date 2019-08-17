import json
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

def unpack_data(filename):
    """ Function to extract data from a json file 
        and convert it to a python dictionary.
    
        Parameters:
            str filename
        
        Returns:
            dict data
    """
    
    if type(filename) != str:
        raise Exception('File name not input as str')
        
    with open(filename) as infile:
        raw_data = infile.read()
        data = json.loads(raw_data)
        
    return data


def broken_docks(dict_data):
    """ Function to calculate total number of broken
        docks for a given data set
        
        Parameters:
            dict dict_data
            
        Returns:
            int broken_docks
        
    """
    broken_docks = 0
    station_list = dict_data['objects']
    
    for station in station_list:
        allProperties = station['additionalProperties']
        
        for singleProperty in allProperties:
            if 'NbBikes' == singleProperty['key']:
                nbBikes = int(singleProperty['value'])
                
            if 'NbEmptyDocks' == singleProperty['key']:
                nbEmptyDocks = int(singleProperty['value'])
                
            if 'NbDocks' == singleProperty['key']:
                nbDocks = int(singleProperty['value'])
                
        broken_docks += (nbDocks - (nbBikes + nbEmptyDocks))

    return broken_docks


def available_space(n, dict_data):
    """ Function that returns all station names
        with more than n number of free spaces.
        
        Parameters:
            int n 
            dict dict_data
            
        Returns:
            list free_space_list
    """
    
    free_space_list = []
    station_list = dict_data['objects']
    
    for station in station_list:
        allProperties = station['additionalProperties']
        
        for singleProperty in allProperties:
            if 'NbEmptyDocks' == singleProperty['key']:
                nbEmptyDocks = int(singleProperty['value'])
            
        if nbEmptyDocks > n:
            stationName = station['commonName']
            free_space_list.append(stationName)
            
    return free_space_list

def closest_stations(dict_data, latitude, longitude):
    """ Function to find closest three stations to
        a given location. It returns a list sorted
        by distance.
        
        Parameters:
            dic dict_data
            float latitude
            float longitude
            
        Returns:
            list distance_list
    """
    station_list = []
    distance_list = []
    station_names = available_space(2, dict_data)
    all_stations = dict_data['objects']
    
    for station in all_stations:
        if station['commonName'] in station_names:
            station_list.append(station)
            
    for station in station_list:
        name = station['commonName']
        station_lat = station['lat']
        station_lon = station['lon']
        distance = np.sqrt((latitude-station_lat)**2 + 
                           (longitude-station_lon)**2)
        distance_list.append([name,distance])
        
    distance_list = sorted(distance_list)
    distance_list = distance_list[0:3]
    
    return distance_list

def plot_stations(dict_data):
    """ Function that plots all the stations
        and shows the number of bikes at each station.
        
        Parameters:
            dict dict_data
        
        Output:
            PNG 2d Scatter
    """
    lats = []
    lons = []
    colors = []
    station_list = dict_data['objects']
    
    for station in station_list:
        lats.append(station['lat'])
        lons.append(station['lon'])
        
        for prop in station['additionalProperties']:
            if 'NbBikes' == prop['key']:
                colors.append(int(prop['value']))
                
    lats = np.array(lats)
    lons = np.array(lons)
    colors = np.array(colors)
    
    plt.scatter(lats, lons, s=20, c=colors, marker='o', cmap=cm.jet)
    plt.xlabel('Latitiude')
    plt.ylabel('Longitude')
    plt.title('Number of Bikes free at each station')
    plt.colorbar()
    
    plt.savefig('scatter.png')
    plt.clf()

    
def plot_stations_2(dict_data, color_mode='NbBikes'):
    """ Function that plots all the stations
        and shows the number of bikes at each station 
        by default. It can alternatively show free space.
        
        Parameters:
            dict dict_data
            str color_mode
        
        Output:
            PNG 2d Scatter
    """
    lats = []
    lons = []
    colors = []
    station_list = dict_data['objects']
    
    for station in station_list:
        lats.append(station['lat'])
        lons.append(station['lon'])
        
        for prop in station['additionalProperties']:
            if color_mode == prop['key']:
                colors.append(int(prop['value']))
                
    lats = np.array(lats)
    lons = np.array(lons)
    colors = np.array(colors)
    
    plt.scatter(lats, lons, s=20, c=colors, marker='o', cmap=cm.jet)
    plt.xlabel('Latitiude')
    plt.ylabel('Longitude')
    plt.title('{} at each station'.format(color_mode))
    plt.colorbar()
    
    plt.savefig('scatter_{}.png'.format(color_mode))
    plt.clf()
    
if __name__ == '__main__':
    data = unpack_data('python_language_data.json')
    print(broken_docks(data))
    print(len(available_space(2, data)))
    print(closest_stations(data, 51.527255, -0.113995))
    plot_stations(data)
    plot_stations_2(data, color_mode='NbEmptyDocks')