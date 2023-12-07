import xmltodict
import json
from datetime import datetime, timedelta



########### 1.1 #############

# Abre o arquivo XML no modo de leitura
with open('DOC-20231129-WA0008_.xml', 'r') as arquivo:
    data_dict = xmltodict.parse(arquivo.read())

# Transforma o dados de xml para json 
json_data = json.dumps(data_dict, indent=4, ensure_ascii=False).encode('utf-8').decode()

# Cria arquivo data.json 
with open('data.json', "w") as json_file:
    json_file.write(json_data)

# Carrega o arquivo JSON
with open('data.json', 'r') as arquivo:
    dados = json.load(arquivo)


########### 1.2 #############

# Encontra a segunda chave 'trkpt' (que corresponde a segunda chave <trkseg> do arquivo xml)
segunda_trkpt = dados['gpx']['trk']['trkseg'][1]['trkpt']

# Inicializando variáveis para armazenar o primeiro e o último valor de 'time'
primeiro_tempo = segunda_trkpt[0]['time']
ultimo_tempo = segunda_trkpt[-1]['time']

# Converte os tempos para objetos datetime
primeiro_tempo_dt = datetime.strptime(primeiro_tempo, "%Y-%m-%dT%H:%M:%SZ")
ultimo_tempo_dt = datetime.strptime(ultimo_tempo, "%Y-%m-%dT%H:%M:%SZ")
tempo_total = ultimo_tempo_dt - primeiro_tempo_dt


# Converte a diferença de tempo para minutos:segundos
tempo_total_minutos_segundos = tempo_total.total_seconds()
minutos = int(tempo_total_minutos_segundos // 60)
segundos = int(tempo_total_minutos_segundos % 60)
tempo_total_horas_decimal = tempo_total_minutos_segundos / 3600

print("1.2 ) O tempo total do trecho analisado é ")
print(f"      em minutos e segundos: {minutos:02d}:{segundos:02d}")
print(f"      em hora decimal: {tempo_total_horas_decimal:.3f} ")


########### 1.3 #############

contador = 0

for p in segunda_trkpt:
    lat = p['time']

    contador += 1


print(f"\n 1.3) Total de trackpoints registrados no segmento analisado: {contador}")


########### 1.4 #############

# Inicializando variáveis para armazenar o primeiro e o último valor de '@lat' e '@lon'
primeiro_lat = float(segunda_trkpt[0]['@lat'])
ultimo_lat = float(segunda_trkpt[-1]['@lat'])
primeiro_lon = float(segunda_trkpt[0]['@lon'])
ultimo_lon = float(segunda_trkpt[-1]['@lon'])

# Diferença absoluta entre o primeiro e ultimo lat e lon
dif_absoluta_lat = abs(primeiro_lat - ultimo_lat)
dif_absoluta_lon = abs(primeiro_lon - ultimo_lon)


print(f"\n 1.4) Diferença absoluta da latitude e longitude entre o primeiro e ultimo trackpoint da etapa")
print(f"      latitude: {dif_absoluta_lat:.5f}")
print(f"      longitude: {dif_absoluta_lon:.5f} ")
