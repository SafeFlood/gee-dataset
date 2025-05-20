import marimo

__generated_with = "0.13.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import ee
    import json
    import folium
    import pandas as pd
    import geemap
    import marimo as mo
    return ee, folium, geemap, json, pd


@app.cell
def _(ee):
    ee.Authenticate()
    return


@app.cell
def _(a, ee, geemap, json):
    with open('south_sulawesi.geojson', 'r') as f:
        south_sulawesi = json.load(f)# Load FAO GAUL level0 (country boundaries)
    gaul0 = ee.FeatureCollection('FAO/GAUL/2015/level0')

    # Filter for Indonesia
    indonesia = gaul0.filter(ee.Filter.eq('ADM0_NAME', 'Indonesia'))

    # Get centroid for map centering
    center = indonesia.geometry().centroid().coordinates().getInfo()
    a
    # Create and display the map
    Map = geemap.Map(center=center[::-1], zoom=5)
    Map.addLayer(indonesia, {'color': 'blue'}, 'Indonesia Boundary')
    Map

    return (south_sulawesi,)


@app.cell
def _(ee, south_sulawesi):
    south_sulawesi_fc = ee.Geometry(south_sulawesi['features'][0]['geometry'])

    return (south_sulawesi_fc,)


@app.cell
def _(south_sulawesi_fc):
    south_sulawesi_geojson = south_sulawesi_fc.getInfo()
    return


@app.cell
def _(south_sulawesi):
    feature = {
            "type": "Feature",
            "properties": {},
            "geometry": south_sulawesi
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
def _(pd):
    flood_history = pd.read_csv("south_sulawesi_flood_data.csv")
    flood_history
    return (flood_history,)


@app.cell
def _():
    return


@app.cell
def _(flood_history):
    flood_history_with_kronologi = flood_history.query("penyebab == penyebab and kronologi == kronologi")
    flood_history_with_kronologi

    return (flood_history_with_kronologi,)


@app.cell
def _(flood_history_with_kronologi):
    fluvial_mask = flood_history_with_kronologi['kronologi'].str.contains(r'\bsungai\b', case=False, na=False)
    fluvial_mask
    return (fluvial_mask,)


@app.cell
def _(flood_history_with_kronologi, fluvial_mask):
    fluvial_flood_history = flood_history_with_kronologi[fluvial_mask]
    fluvial_flood_history
    return (fluvial_flood_history,)


@app.cell
def _(fluvial_flood_history, pd):
    month_map = {
            'Januari': '01', 'Februari': '02', 'Maret': '03', 'April': '04',
            'Mei': '05', 'Juni': '06', 'Juli': '07', 'Agustus': '08',
            'September': '09', 'Oktober': '10', 'November': '11', 'Desember': '12'
        }
    fluvial_flood_history_copy = fluvial_flood_history.copy()
    fluvial_flood_history_copy['tanggal'] = fluvial_flood_history_copy['tanggal'].replace(month_map, regex=True)
    fluvial_flood_history_copy['tanggal'] = pd.to_datetime(fluvial_flood_history_copy['tanggal'], format='mixed')
    fluvial_flood_history_copy['tanggal'] = fluvial_flood_history_copy['tanggal'].dt.strftime('%Y-%m-%d')
    fluvial_flood_history_copy
    return (fluvial_flood_history_copy,)


@app.cell
def _(ee, fluvial_flood_history_copy):
    min_date = ee.Date(fluvial_flood_history_copy['tanggal'].min())
    max_date = fluvial_flood_history_copy['tanggal'].max()
    max_date = ee.Date("2020-10-01")
    return max_date, min_date


@app.cell
def _(fluvial_flood_history_copy):
    df = fluvial_flood_history_copy.query("tanggal == tanggal and lat == lat and lng==lng")[['tanggal', 'lat', 'lng']]

    #df.to_csv('south_sulawesi_fluvial_flood_history.csv', index=False)
    return


@app.cell
def _(max_date, min_date):
    min_date , max_date
    return


@app.cell
def _(ee, max_date, min_date, south_sulawesi_fc):
    nasa_gpm = ee.ImageCollection('NASA/GPM_L3/IMERG_V07')
    nasa_gpm.filterBounds(south_sulawesi_fc).filterDate(min_date, max_date).mean().getInfo()
    return


if __name__ == "__main__":
    app.run()
