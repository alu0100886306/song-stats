Este programa calcula para cada canción(por año): 
Valor = (100-pos) por dia
TopPos Posición más alta en el ranking
TopMes Mes en el que alcanzó TopPos

Requiere el archivo waf.csv con los atributos y devuelve "song_stats_region_waf.csv" en la carpeta del ejecutable

Primero:
make install

Para ejecutar con make ejemplo:
make ARGS="global_waf.csv"
