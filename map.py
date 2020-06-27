import folium  # for Creating a Visual map

#in the location we add what called COORDINATES be sure to get them from safe place
newMap = folium.Map(location=[51.478418, 7.223265], zoom_start=17,
                    title='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}')

tooltip = "This is my location"

#if you press at tooltip it gonna show that message
# if you would like to add new features like icon first you need to
# download the icon and put it in the folder here and i will show you how
logo = folium.features.CustomIcon('ge.png', icon_size=(50, 50))

folium.Marker([51.478418, 7.223265],
              popup='<strong>you are here</strong>',
              tooltip=tooltip,
              icon=logo).add_to(newMap)

#now we gonna use poly mark to draw some line
folium.PolyLine(locations=[(51.478418, 7.223265), (51.479460, 7.221972)],
                line_opacity=0.6, color='gold').add_to(newMap)

#this to create satellite view

tile = folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    name='Esri Satellite',
    overlay=False,
    control=True
).add_to(newMap)
newMap.save("my-map.html")
