# Geração de grids 2x2 m e extração de centroides

Este repositório contém um notebook desenvolvido no Google Colab para gerar uma grade regular de **2 m x 2 m** sobre feições poligonais de edificações/construções e extrair os centroides das células que intersectam essas feições.

O script também aplica uma regra de distância mínima, mantendo apenas centroides com pelo menos **2 metros de distância** entre si.

## Objetivo

Gerar automaticamente:

1. Um shapefile com os grids de 2 m x 2 m que intersectam polígonos de edificações;
2. Um shapefile com os centroides desses grids;
3. Uma visualização simples com os polígonos originais, os grids e os centroides gerados.

## Estrutura geral do notebook

O notebook está organizado em três etapas principais:

### 1. Conexão com o Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
```

Essa etapa permite acessar os arquivos armazenados no Google Drive dentro do ambiente do Google Colab.

### 2. Importação das bibliotecas

```python
import geopandas as gpd
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
```

Bibliotecas utilizadas:

- `geopandas`: leitura, manipulação e exportação de dados geoespaciais vetoriais;
- `shapely`: criação e manipulação de geometrias;
- `matplotlib`: visualização dos resultados.

### 3. Geração dos grids e centroides

O código cria células quadradas de 2 m x 2 m dentro dos limites de cada polígono, seleciona apenas as células que intersectam as edificações e extrai seus centroides.

Além disso, o script remove centroides muito próximos, mantendo uma distância mínima de 2 m entre eles.

## Entrada esperada

O código espera como entrada um shapefile de polígonos, representando edificações ou construções.

Exemplo de caminho utilizado no notebook:

```python
filepath = '/content/drive/MyDrive/Centroides_AUC_DSA_MuncipioX/Edif_Const_pol.shp'
```

Antes de executar, altere esse caminho para o local correto do seu shapefile no Google Drive.

## Parâmetros principais

```python
grid_size = 2.0
min_distance = 2.0
```

| Parâmetro | Descrição |
|---|---|
| `grid_size` | Define o tamanho das células da grade. No notebook, foi utilizado 2 m x 2 m. |
| `min_distance` | Define a distância mínima permitida entre centroides. No notebook, foi utilizado 2 m. |

> Importante: para que as medidas em metros estejam corretas, o shapefile de entrada deve estar em um sistema de coordenadas projetado, como UTM. Se o arquivo estiver em coordenadas geográficas, como EPSG:4326, as distâncias serão calculadas em graus, não em metros.

## Saídas geradas

O notebook gera dois shapefiles:

```python
output_filepath_grids = '/content/drive/MyDrive/Centroides_AUC_DSA_MunicipioX/Edificacoes_polig_grids_complete.shp'

output_filepath_centroids = '/content/drive/MyDrive/Centroides_AUC_DSA_MunicipioX/Edificacoes_polig_grid_centroids_complete.shp'
```

| Arquivo | Descrição |
|---|---|
| `Edificacoes_polig_grids_complete.shp` | Shapefile contendo as células de grid de 2 m x 2 m que intersectam as edificações. |
| `Edificacoes_polig_grid_centroids_complete.shp` | Shapefile contendo os centroides válidos dos grids gerados. |

## Visualização dos resultados

Ao final, o notebook gera uma visualização simples:

```python
ax = gdf.plot(edgecolor='black', facecolor='none', figsize=(8, 8))
grids_gdf.plot(ax=ax, edgecolor='blue', facecolor='none')
centroids_gdf.plot(ax=ax, color='red', markersize=2)
plt.show()
```

Na visualização:

- polígonos originais: contorno preto;
- grids gerados: contorno azul;
- centroides: pontos vermelhos.

## Como executar no Google Colab

1. Faça upload do notebook para o Google Colab;
2. Salve o shapefile de entrada no Google Drive;
3. Atualize o caminho da variável `filepath`;
4. Atualize os caminhos de saída `output_filepath_grids` e `output_filepath_centroids`;
5. Execute as células do notebook em sequência.

## Requisitos

As principais bibliotecas utilizadas são:

```txt
geopandas
shapely
matplotlib
```

No Google Colab, caso alguma biblioteca não esteja instalada, execute:

```python
!pip install geopandas shapely matplotlib
```

## Observações importantes

- O arquivo de entrada deve ser uma camada poligonal.
- O sistema de referência deve estar em metros, preferencialmente UTM.
- O método usa a extensão de cada polígono para gerar as células e depois filtra apenas aquelas que intersectam a geometria.
- A regra de distância mínima evita a geração de centroides muito próximos.
- Para áreas muito grandes ou muitos polígonos, o processamento pode ser demorado.

## Aplicações possíveis

Este procedimento pode ser utilizado em análises geoespaciais que exigem amostragem regular em pequenas células, como:

- geração de pontos amostrais sobre edificações;
- análise de densidade construtiva;
- apoio a estudos urbanos;
- preparação de dados para validação espacial;
- geração de centroides para integração com outras bases geográficas.

## Autoria

Desenvolvido por Bruna Rocha.
