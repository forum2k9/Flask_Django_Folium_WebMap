from flask import Flask, render_template
import folium

app = Flask(__name__)



@app.route('/index.html')
@app.route('/index')
@app.route('/map')
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/map1')
def index_1():
    start_coords = (9.069, 7.472)
    folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="OpenStreetMap",
        # attr='CartoDB attribution'
        max_zoom=16, 
        min_zoom=10, 
        )

    folium.Marker(
            location = start_coords,
            popup = '<h1>FATIMAH</h1>',
            tooltip = 'HEHEHE,,,,'
        ).add_to(folium_map)

    return folium_map._repr_html_()



@app.route('/map2')
def index_2():
    start_coords = (9.069, 7.472)
    folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="Stamen Terrain",
        # attr='CartoDB attribution'
        )
    return folium_map._repr_html_()



@app.route('/map3')
def index_3():
    start_coords = (9.069, 7.472)
    folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="Stamen Watercolor",
        # attr='CartoDB attribution'
        )
    return folium_map._repr_html_()


@app.route('/map4')
def index_4():
    start_coords = (9.069, 7.472)
    folium_map = folium.Map(location=start_coords, 
        zoom_start=13,
        tiles="Stamen Toner",
        # attr='CartoDB attribution'
        )
    return folium_map._repr_html_()



if __name__ == '__main__':
    app.run(debug=True)

