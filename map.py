import folium as f
dum = f.Map(location=[25.5501,84.1500],width='90%',height='90%')
f.Marker(location=[25.5501,84.1500],popup='Dumraon').add_to(dum)
print(dum)

