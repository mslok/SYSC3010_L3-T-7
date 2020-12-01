#will need to install pip3 and then folium with pip3 in order to run 

import folium 
import json

def update_log(database='local.json', log='markers.json'):
#loops through local.json linked to thingspeak and adds unique missing events to the markers.json log. 
#only unique values are added woot woot. 
#next time a map is generated any new recorded bumps will be included. 
    
    with open(database) as data_file:
        
        data = json.load(data_file)
    
    #with open(log) as log_file: 

        #markers = json.load(log_file)  

    seen = set()
    temp = []
    for d in data['events']:
        t=tuple(d.items())
        if t not in seen:
            seen.add(t)
            temp.append(d)

    with open(log,'w') as marker_file: 
        json.dump(temp, marker_file, indent=4)


def update_map(filename='markers.json'):
#generates a map with bump markers from the markers.json file.

    bump_map = folium.Map(location=[45.4215, -75.6972])
    tooltip="Bump Detected"

    with open(filename) as map_marker_data:

        data=json.load(map_marker_data)

    for i in data:

        lon=i['LONG']
        print(lon)
        lat=i['LAT']
        print(lat)
        gs=i["G's"]

        folium.Marker(['{}'.format(lat),'{}'.format(lon)], popup='{}'.format(gs), tooltip=tooltip).add_to(bump_map)
        print('Marker added')
        bump_map.save('index.html')


def main():
	update_log()
	update_map()

if __name__ == "__main__":
	main()
