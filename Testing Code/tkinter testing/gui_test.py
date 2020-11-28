from tkinter import *
import tkinter.scrolledtext as st 
import http.client
import urllib.parse
import requests
import json

#my read api key 9SO0XFLPB59ODN5L
#my write key UU2HQ2WXR5L56DDK
#my channel id 1160858

#mikes read api key WQUCC93KDMBOY6V5
#mikes write api key OBGBKNICJSMTDX1G
#mikes channel id 1223588

#ambars read api key B4B863GDK58LVJGP
#amabrs channel id 1226682

#simply prints channel data and feeds 




class Table: 

	def __init__(self,root): 
		# code for creating table 
		for i in range(total_rows): 
			for j in range(total_columns):   
				self.e = Entry(root, width=20, fg='blue', font=('Arial',16,'bold')) 
				self.e.grid(row=i, column=j) 
				#print(TabladeDatos[i][j])
				if TabladeDatos[i][j] is not None:
					#print("No es Vacio")
					self.e.insert(END, TabladeDatos[i][j])
				else:
					#print("Es vacio")
					self.e.insert(END, "Sin coordenadas")
				
				
TabladeDatos = [ ]
a = [' ',' ',' ',' ',' ',' ']
TabladeDatos.append(a)
a = ['ID','G Force','Long','Lat','Direccion', 'Time']
#a = [' ',' ',' ',' ',' ',' ']
TabladeDatos.append(a)

lst = []
a = [' ',' ',' ',' ',' ']
lst.append(a)

a = ['ID','G Force','Long','Lat','Time']
lst.append(a)

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
	ret_json=read_channel('9SO0XFLPB59ODN5L','1160858')
	#disp_text=json.dumps(ret_json, indent=4)

	#print(ret_json)
	print("Inicio de todos mis feeds de datos")
	
	for feed in ret_json['feeds']: 
		temporal = getAddress(feed['field2'],feed['field3'])
		a= [feed['entry_id'],feed['field1'],feed['field2'],feed['field3'],feed['created_at']]
		lst.append(a)
		
		#print (temporal)
		a=[feed['entry_id'],feed['field1'],feed['field2'],feed['field3'], temporal,feed['created_at']]
		TabladeDatos.append(a)
	print(TabladeDatos)

	
	#analyze_field('9SO0XFLPB59ODN5L','1160858','1') 
def hola():
	print("Hello World!")

def FilterTable(Datos, searchValue):
	i=0
	for element in Datos: 
		if Datos[4] == searchValue:
			Datos.pop(i)
		i+=1
	return Datos
3
def printv():
	print(entry_var.get())

	
if __name__ == "__main__":
	main()

	# find total number of rows and 
	# columns in list 
	total_rows = len(TabladeDatos) 
	total_columns = len(TabladeDatos[0]) 
	
	# create root window 
	root = Tk() 
	
	t = Table(root) 
	
	Button(root, text="Show Data", command=hola).grid(column=0, row=0)
	entry_var= StringVar()
	entry=Entry(root, textvariable=entry_var).grid(column=1, row=0)

	Button(root, text="Submit", command=printv).grid(column=2, row=0)
	FilterTable(TabladeDatos, "Annapolis, NS, Canada")
	
	
		
	root.mainloop()
