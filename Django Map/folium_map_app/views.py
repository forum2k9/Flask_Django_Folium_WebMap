from django.shortcuts import render
from django.http import HttpResponse
import folium


# Create your views here.

def index(request):
	context = {
		'map_title': 'Map Home Page...'
	}
	# return HttpResponse('<h1>This is index page</h1>')
	return render(request, 'index.html', context)
# -------------------------------------------------


def map1(request):
	start_coords = (9.069, 7.472)
	folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="OpenStreetMap",
        # attr='CartoDB attribution'
        max_zoom=16, 
        min_zoom=10, 
        )

	mymap = folium_map._repr_html_() # HTML representation of the map

	context = {
		'map': mymap,
		'map_title': 'Map 1 - OpenStreetMap'
	}

	# return HttpResponse('<h1>This is map page</h1>')
	return render(request, 'map1.html', context)



# -------------------------------------------------
def map2(request):
	start_coords = (9.069, 7.472)
	folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="Stamen Terrain",
        # attr='CartoDB attribution'
        max_zoom=16, 
        min_zoom=10, 
        )

	mymap = folium_map._repr_html_() # HTML representation of the map

	context = {
		'map': mymap,
		'map_title': 'Map 2 - Stamen Terrain'
	}

	# return HttpResponse('<h1>This is map page</h1>')
	return render(request, 'map2.html', context)


# -------------------------------------------------
def map3(request):
	start_coords = (9.069, 7.473)
	folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="Stamen Watercolor",
        # attr='CartoDB attribution'
        max_zoom=16, 
        min_zoom=10, 
        )

	mymap = folium_map._repr_html_() # HTML representation of the map

	context = {
		'map': mymap,
		'map_title': 'Map 3 - Stamen Watercolor'
	}

	# return HttpResponse('<h1>This is map page</h1>')
	return render(request, 'map3.html', context)


# -------------------------------------------------
def map4(request):
	start_coords = (9.069, 7.474)
	folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="Stamen Toner",
        # attr='CartoDB attribution'
        max_zoom=16, 
        min_zoom=10, 
        )

	mymap = folium_map._repr_html_() # HTML representation of the map

	context = {
		'map': mymap,
		'map_title': 'Map 4 - Stamen Toner'
	}

	# return HttpResponse('<h1>This is map page</h1>')
	return render(request, 'map4.html', context)



