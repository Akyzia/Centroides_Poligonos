# 2x2 m Grid Generation and Centroid Extraction

This repository contains a Google Colab notebook developed to generate a regular **2 m x 2 m grid** over polygon features representing buildings/constructions and extract the centroids of the cells intersecting these features.

The script also applies a minimum distance rule, keeping only centroids with at least **2 meters of distance** between each other.

---

# Objective

Automatically generate:

1. A shapefile containing 2 m x 2 m grids intersecting building polygons;
2. A shapefile containing the centroids of the generated grids;
3. A simple visualization of the original polygons, generated grids, and centroids.

---

# Notebook Structure

The notebook is organized into three main stages:

## 1. Google Drive Connection

```python
from google.colab import drive
drive.mount('/content/drive')
```

This step allows access to files stored in Google Drive within the Google Colab environment.

---

## 2. Library Import

```python
import geopandas as gpd
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
```

Libraries used:

- `geopandas` → reading, manipulating, and exporting vector geospatial data;
- `shapely` → geometry creation and manipulation;
- `matplotlib` → visualization of results.

---

## 3. Grid and Centroid Generation

The script creates 2 m x 2 m square cells within the limits of each polygon, selects only the cells intersecting the building geometries, and extracts their centroids.

Additionally, the script removes centroids that are too close, maintaining a minimum distance of 2 m between them.

---

# Expected Input

The notebook expects a polygon shapefile representing buildings or constructions.

Example path used in the notebook:

```python
filepath = '/content/drive/MyDrive/Centroides_AUC_DSA_MuncipioX/Edif_Const_pol.shp'
```

Before running the notebook, update this path to the correct location of your shapefile in Google Drive.

---

# Main Parameters

```python
grid_size = 2.0
min_distance = 2.0
```

| Parameter | Description |
|---|---|
| `grid_size` | Defines the size of the grid cells. In this notebook, 2 m x 2 m was used. |
| `min_distance` | Defines the minimum allowed distance between centroids. In this notebook, 2 m was used. |

> Important: to ensure that distance measurements are calculated in meters, the input shapefile must use a projected coordinate system such as UTM. If geographic coordinates such as EPSG:4326 are used, distances will be calculated in degrees instead of meters.

---

# Generated Outputs

The notebook generates two shapefiles:

```python
output_filepath_grids = '/content/drive/MyDrive/Centroides_AUC_DSA_MunicipioX/Edificacoes_polig_grids_complete.shp'

output_filepath_centroids = '/content/drive/MyDrive/Centroides_AUC_DSA_MunicipioX/Edificacoes_polig_grid_centroids_complete.shp'
```

| File | Description |
|---|---|
| `Edificacoes_polig_grids_complete.shp` | Shapefile containing the 2 m x 2 m grid cells intersecting the building polygons. |
| `Edificacoes_polig_grid_centroids_complete.shp` | Shapefile containing the valid centroids generated from the grids. |

---

# Result Visualization

At the end of the notebook, a simple visualization is generated:

```python
ax = gdf.plot(edgecolor='black', facecolor='none', figsize=(8, 8))
grids_gdf.plot(ax=ax, edgecolor='blue', facecolor='none')
centroids_gdf.plot(ax=ax, color='red', markersize=2)
plt.show()
```

Visualization elements:

- original polygons → black outline;
- generated grids → blue outline;
- centroids → red points.

---

# Libraries Used

```python
geopandas
shapely
matplotlib
```

---

# Installation

This project uses a `requirements.txt` file to install the required libraries automatically.

Install the dependencies using:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```txt
geopandas
shapely
matplotlib
```

---

## Google Colab

```python
!pip install -r requirements.txt
```

---

# Project Structure

```text
Polygon_Centroids/
│
├── notebook.ipynb
├── requirements.txt
├── README.md
└── output_shapefiles/
```

---

# How to Run

## Google Colab

1. Upload the notebook to Google Colab;
2. Upload the `requirements.txt` file;
3. Install the dependencies;
4. Save the input shapefile in Google Drive;
5. Update the `filepath` variable;
6. Run the notebook cells sequentially.

---

# Important Notes

- The input file must be a polygon layer;
- The coordinate system should preferably be projected in meters (UTM);
- The method generates grid cells using each polygon extent and filters only intersecting cells;
- The minimum distance rule prevents the generation of very close centroids;
- Processing large areas or many polygons may require more execution time.

---

# Possible Applications

This workflow can be applied to geospatial analyses requiring regular sampling in small grid cells, such as:

- sample point generation over buildings;
- urban density analysis;
- support for urban studies;
- spatial validation workflows;
- centroid generation for integration with other geospatial datasets.

---

# Technologies

- Python
- GeoPandas
- Shapely
- Matplotlib
- Google Colab
- Jupyter Notebook

---

# Author

Developed by Bruna Rocha.