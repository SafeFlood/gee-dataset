import marimo

__generated_with = "0.13.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import ee
    import json
    import folium
    return ee, folium, json


@app.cell
def _(ee):
    ee.Authenticate()
    return


@app.cell
def _(ee):
    ee.Initialize(project='maps-disaster')
    return


@app.cell
def _(json):
    with open('south_sulawesi.geojson', 'r') as f:
        south_sulawesi = json.load(f)
    return (south_sulawesi,)


@app.cell
def _(ee, south_sulawesi):
    south_sulawesi_fc = ee.Geometry(south_sulawesi['features'][0]['geometry'])

    return (south_sulawesi_fc,)


@app.cell
def _(south_sulawesi_fc):
    south_sulawesi_geojson = south_sulawesi_fc.getInfo()
    return (south_sulawesi_geojson,)


@app.cell
def _(south_sulawesi_geojson):
    feature = {
            "type": "Feature",
            "properties": {},
            "geometry": south_sulawesi_geojson
        }
    return (feature,)


@app.cell
def _(feature, folium):
    m = folium.Map(location=[-4.5, 119.25], zoom_start=7)
    folium.GeoJson(
        feature,
        name='South Sulawesi',
        style_function=lambda feat: {
            'fillColor': 'blue',
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.5,
        }
    ).add_to(m)

    folium.LayerControl().add_to(m)
    m
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
