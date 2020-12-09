from tkinter import *
import tkinter.scrolledtext as st 
import http.client
import urllib.parse
import requests
import json
import folium
import webbrowser
import thingspeak_test.py

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
					self.e.insert(END, TabladeDatos[i][j])
				else:
					self.e.insert(END, "Sin coordenadas")
				
				
TabladeDatos = [ ]
a = [' ',' ',' ',' ']
TabladeDatos.append(a)
a = ['G Force','LAT','LONG','Direction']
#a = [' ',' ',' ',' ',' ',' ']
TabladeDatos.append(a)



read_channel(api_key,channel_id):

analyze_field(api_key,channel_id,field_id):
	
	
getAddress(lt,ln): 

	
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
	
	
	#for feed in ret_json['events']: 
	#	temporal = getAddress(feed['LAT'],feed['LONG'])
		#a= [feed['entry_id'],feed['field1'],feed['field2'],feed['field3'],feed['created_at']]
		#lst.append(a)
		
		#print (temporal)
	#	a=[feed["G's"],feed['LAT'],feed['LONG'],feed['ADDRESS'], temporal]
	#	TabladeDatos.append(a)
	#print(TabladeDatos)

	
	#analyze_field('9SO0XFLPB59ODN5L','1160858','1') 
def FilterTable(Data, searchValue):
	i=0
	for elemento in Data: 
		if elemento[4] == searchValue:
			Datos.pop(i)
		i+=1
	return Data


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

