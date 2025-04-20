#AQUI EU GERO O GRID DE 2M X 2M QUE INTERSECCIONAM COM AS FEIÇÕES DE EDIFICAÇÕES, E DEPOIS EXTRAIO OS CENTROIDES DESSES GRIDS
#NO ENTANTO, EXCLUO OS centroides que nao possuem ao menos 2m de distancia do outro centroide


import geopandas as gpd
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

#from google.colab import drive
#drive.mount('/content/drive') #se for usar arquivo do drive

# Função para gerar uma grade de células dentro de um polígono
def generate_grid_within_bounds(bounds, grid_size):
    minx, miny, maxx, maxy = bounds  # Limites do polígono
    cells = []
    x = minx
    while x < maxx:
        y = miny
        while y < maxy:
            # Criar uma célula quadrada de grid_size x grid_size
            cell = Polygon([(x, y), (x + grid_size, y),
                            (x + grid_size, y + grid_size), (x, y + grid_size)])
            cells.append(cell)  # Adicionar célula completa
            y += grid_size
        x += grid_size
    return cells

# Função para verificar a distância mínima de 2m entre os centróides
def is_valid_centroid(new_centroid, existing_centroids, min_distance):
    for centroid in existing_centroids:
        if new_centroid.distance(centroid) < min_distance:
            return False
    return True

#Caminho para o shapefile no Google Drive
filepath = '/content/Centroides_Disciplina_Visualizacao_de_Inf/Edificacoes_Construcoes_OpenBuildings_APP_AU.shp' #aqui eu capturo o arquivo do drive, que são os limites das edificações da área de estudo

#Carregar os dados da camada poligonal (edificações)
gdf = gpd.read_file(filepath)

#Definir o tamanho da grade (2m x 2m) e a distância mínima
grid_size = 2.0
min_distance = 2.0  # Distância mínima entre centróides

#Armazenar todos os grids e centróides das células geradas, sem duplicação
grids = []
centroids = []

#Usar um conjunto para rastrear os grids que já foram adicionados
grid_set = set()

#Iterar sobre todas as feições poligonais (edificações)
for _, row in gdf.iterrows():
    polygon = row['geometry']  #Polígono da edificação
    bounds = polygon.bounds  #Limites do polígono
    cells = generate_grid_within_bounds(bounds, grid_size)  #Gerar células de grid completas

    #Filtrar células que intersectam o polígono
    intersecting_cells = [cell for cell in cells if cell.intersects(polygon)]

    for cell in intersecting_cells:
        # Verificar se o grid já foi processado, evitando sobreposição
        if tuple(cell.exterior.coords) not in grid_set:
            grid_set.add(tuple(cell.exterior.coords))  # Adicionar o grid único ao conjunto
            new_centroid = cell.centroid  # Novo centróide

            # Verificar se a distância mínima é respeitada
            if is_valid_centroid(new_centroid, centroids, min_distance):
                grids.append(cell)  # Armazenar o grid único
                centroids.append(new_centroid)  # Armazenar o centróide válido

# Converter a lista de grids e centróides para GeoDataFrames
grids_gdf = gpd.GeoDataFrame(geometry=grids, crs=gdf.crs)
centroids_gdf = gpd.GeoDataFrame(geometry=centroids, crs=gdf.crs)

# Salvar os grids e centróides gerados em shapefiles
output_filepath_grids = '/content/Centroides_Disciplina_Visualizacao_de_Inf/Edificacoes_polig_grids_complete.shp'
output_filepath_centroids = '/content/Centroides_Disciplina_Visualizacao_de_Inf/Edificacoes_polig_grid_centroids_complete.shp'

grids_gdf.to_file(output_filepath_grids)  # Salvar os grids
centroids_gdf.to_file(output_filepath_centroids)  # Salvar os centróides

# Plotar os resultados (opcional)
ax = gdf.plot(edgecolor='black', facecolor='none', figsize=(8, 8))  # Polígonos das edificações
grids_gdf.plot(ax=ax, edgecolor='blue', facecolor='none')  # Grids completos
centroids_gdf.plot(ax=ax, color='red', markersize=2)  # Centròides da grade
plt.show()
