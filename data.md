# MODIS Flood Features Dataset

## Overview
This dataset contains spatially and temporally indexed flood “event” samples over South Sulawesi, Indonesia. For each pixel where a MODIS‐detected flood occurred, a suite of environmental predictor variables (precipitation, vegetation indices, terrain metrics, etc.) is sampled and exported as a CSV for downstream analysis (e.g., modeling flood susceptibility or impacts).

## Study Area
- **Region**: Sulawesi Selatan (South Sulawesi), Indonesia  
- **Boundary Source**: FAO GAUL 2015, level-1 administrative units

## Temporal Coverage
- All flood events in the MODIS Global Flood Database (V1) within the study area  
- Date format: `YYYY-MM-DD`  
- Sampling window for time‐varying predictors spans from three days before to one day after each event date (depending on the variable)

## Data Sources & Processing
| Variable            | Source                                       | Notes                                                                                 |
|---------------------|----------------------------------------------|---------------------------------------------------------------------------------------|
| flooded             | GLOBAL_FLOOD_DB/MODIS_EVENTS/V1              | Binary flood mask (0=no flood, 1=flood)                                              |
| jrc_perm_water      | GLOBAL_FLOOD_DB/MODIS_EVENTS/V1              | JRC permanent water mask (0/1)                                                        |
| precip_1d           | UCSB-CHG/CHIRPS/DAILY                        | 1-day accumulated precipitation preceding event                                       |
| precip_3d           | UCSB-CHG/CHIRPS/DAILY                        | 3-day accumulated precipitation preceding event                                       |
| NDVI                | MODIS/061/MOD13A2                            | 16-day average normalized difference vegetation index                                 |
| NDWI                | MODIS/061/MOD09GA                            | 16-day average normalized difference water index (B02 vs. B04)                         |
| water_occurrence    | JRC/GSW1_4/GlobalSurfaceWater                | Long-term water occurrence percentage                                                |
| LST_day             | MODIS/061/MOD11A2                            | Daytime land surface temperature (Kelvin × 0.02 scaling)                              |
| soil_moisture       | NASA_USDA/HSL/SMAP_soil_moisture             | 3-day average surface soil moisture                                                   |
| landcover           | MODIS/061/MCD12Q1                            | IGBP land-cover classification (integer codes 1–17)                                   |
| elevation           | USGS/SRTMGL1_003                             | Elevation (meters above sea level)                                                   |
| slope               | USGS/SRTMGL1_003 via `ee.Terrain.slope`      | Terrain slope (degrees)                                                               |
| aspect              | USGS/SRTMGL1_003 via `ee.Terrain.aspect`     | Terrain aspect (degrees clockwise from north)                                         |
| upstream_area       | MERIT/Hydro/v1_0_1                           | Upstream drainage area (m²)                                                           |
| TWI                 | Computed Topographic Wetness Index (log scale) | TWI = ln( ups / tan(slope) ), slope in radians, floor at 0.001 to avoid singularities  |

## Schema
| Column Name      | Type    | Description                                                           |
|------------------|---------|-----------------------------------------------------------------------|
| date             | string  | Event date in `YYYY-MM-DD`                                            |
| lon              | float   | Longitude of the sample point (EPSG:4326)                             |
| lat              | float   | Latitude of the sample point (EPSG:4326)                              |
| flooded          | int     | MODIS flood flag (0 or 1)                                             |
| jrc_perm_water   | int     | JRC permanent water flag (0 or 1)                                     |
| precip_1d        | float   | 1-day precipitation total (mm)                                        |
| precip_3d        | float   | 3-day precipitation total (mm)                                        |
| NDVI             | float   | Normalized Difference Vegetation Index                                |
| NDWI             | float   | Normalized Difference Water Index                                     |
| water_occurrence | float   | Water occurrence (%) over multi-year record                           |
| LST_day          | float   | Land Surface Temperature (Kelvin)                                     |
| soil_moisture    | float   | Surface Soil Moisture (m³/m³)                                         |
| landcover        | int     | MODIS IGBP land-cover class                                           |
| elevation        | float   | Elevation in meters                                                  |
| slope            | float   | Terrain slope in degrees                                             |
| aspect           | float   | Terrain aspect in degrees                                            |
| upstream_area    | float   | Upstream drainage area (m²)                                           |
| TWI              | float   | Topographic Wetness Index (unitless, log scale)                       |

## Usage
1. Download the CSV from your Google Drive export.  
2. Load into your analysis environment (e.g., pandas, R, GIS).  
3. Use the predictor variables to train classification/regression models of flood occurrence, severity, or risk mapping.

```python
import pandas as pd

df = pd.read_csv("modis_flood_features_full_latest.csv")
print(df.head())