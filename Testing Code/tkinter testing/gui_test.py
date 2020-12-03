from tkinter import *
import tkinter.scrolledtext as st 
import http.client
import urllib.parse
import requests
import json
import folium
import webbrowser


class Table: 

	def __init__(self,root): 
		# code for creating table 
		
		list = root.grid_slaves()
		for l in list:
			l.destroy()


		for i in range(total_rows): 
			for j in range(total_columns):   
				self.e = Entry(root, width=20, fg='black', font=('Arial',16,'bold')) 
				self.e.grid(row=i, column=j) 
				#print(TabladeDatos[i][j])
				if TabladeDatos[i][j] is not None:
					#print("No es Vacio")
					self.e.insert(END, TabladeDatos[i][j])
				else:
					#print("Es vacio")
					self.e.insert(END, "Sin coordenadas")
				
				
TabladeDatos = [ ]
a = [' ',' ',' ',' ']
TabladeDatos.append(a)
a = ['G Force','LAT','LONG','Direction']
#a = [' ',' ',' ',' ',' ',' ']
TabladeDatos.append(a)



def read_channel(api_key,channel_id):

	key=api_key
	channel=channel_id
	url = 'https://api.thingspeak.com/channels/'+channel+'/feeds.json?api_key='+key+'&results=8000'
	pull_data=requests.get(url).json()
	return pull_data

def analyze_field(api_key,channel_id,field_id):
	key=api_key
	channel=channel_id
	num=field_id
	url = 'https://api.thingspeak.com/channels/'+channel+'/field/'+num+ '.json?api_key='+key+'&results=8000'
	pull_data=requests.get(url).json()
	field=pull_data
	#print(field_1)
	total=0
	n=0
	
	print("Accelerometer readings:")
	
	for i in field['feeds']:
		temp=i['field1']
		print(temp)
		total=total+float(temp)
		n=n+1
	
	if n !=0:
		avg=total/n
		print("The average value is: " + str(avg))
	else:
		print("No data to be analyzed, channel empty.")


	
def getAddress(lt,ln): 
#returns the street address of a set of coordinates
	
	latitude=lt
	longitude=ln
	
	URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
	api_key = 'QIb2IpsnEhXcnrbXrkTmErXA3PwNMTzUkX0HKdnuc4A'
	PARAMS = {
				'at': '{},{}'.format(latitude,longitude),
				'apikey': api_key
				}

	r = requests.get(url = URL, params = PARAMS)
	data = r.json() 

	for i in data['items']:
		temp=i['address']['label']
		return temp
	


def main():
	#ret_json=read_channel('9SO0XFLPB59ODN5L','1160858')
	#disp_text=json.dumps(ret_json, indent=4)
	filename='markers.json'

	with open(filename) as map_marker_data:
		data=json.load(map_marker_data)


	for i in data:
		temporal = getAddress(i['LAT'],i['LONG'])
		a=[i["G's"],i['LAT'],i['LONG'],i['ADDRESS'], temporal]
		TabladeDatos.append(a)
	print(TabladeDatos)
	
	#print(ret_json)
	#print("Inicio de todos mis feeds de datos")
	
	#for feed in ret_json['events']: 
	#	temporal = getAddress(feed['LAT'],feed['LONG'])
		#a= [feed['entry_id'],feed['field1'],feed['field2'],feed['field3'],feed['created_at']]
		#lst.append(a)
		
		#print (temporal)
	#	a=[feed["G's"],feed['LAT'],feed['LONG'],feed['ADDRESS'], temporal]
	#	TabladeDatos.append(a)
	#print(TabladeDatos)

	
	#analyze_field('9SO0XFLPB59ODN5L','1160858','1') 
def FilterTable(Datos, searchValue):
	i=0
	for elemento in Datos: 
		if elemento[4] == searchValue:
			Datos.pop(i)
		i+=1
	return Datos


def openweb():
	webbrowser.open('index.html')

def printv():
	TablaFiltrada = []
	TablaFiltrada=FilterTable(TabladeDatos,entry_var.get())
	print(TablaFiltrada)

	total_rows= len(TablaFiltrada)
	total_columns= len(TablaFiltrada[0])

	t = Table(root) 



	
if __name__ == "__main__":
	main()

	# find total number of rows and 
	# columns in list 
	total_rows = len(TabladeDatos) 
	total_columns = len(TabladeDatos[0]) 

	
	
	# create root window 
	root = Tk() 
	
	t = Table(root) 
	
	entry_var= StringVar()
	
	
	entry=Entry(root, textvariable=entry_var).grid(column=1, row=0)
	Button(root, text="Submit", command=printv).grid(column=2, row=0)
	Button(root, text="Map", command=openweb).grid(column=3, row=0)
	root.mainloop()

