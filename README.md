## Sobre o arquivo analisado 
Os dados contidos em "DOC-20231129-WA0008_.xml" consistem em dados capturados por um dispositivo móvel que registra coordenadas de latitude e longitute, informação de altitude e marca de tempo (timestamp) adquiridas por um GPS durante um treino de corrida. 

## Proposta deste exercício
A partir dos dados presentes em "DOC-20231129-WA0008_.xml" :

1.1) Abrir o arquivo e colocar os dados em um string

1.2) Determinar o tempo total do percurso da segunda etapa da corrida (segundo < trkseg >) em mm:ss (minutos:segundos) e em hh,hhh (hora em formato decimal)

1.3) Informar o número total de trackpoints registrados no segmento analisado.

1.4) A diferença absoluta (sem sinal) da latitude e da longitude entre o primeiro e o último trackpoint da etapa.


## Como executar este código

1 - Primeiramente você deve ter python instalado em sua máquina

2 - Instalar as dependências deste projeto  
No terminal, dentro do diretório **running-route-xml-file-analysis**, executar o seguinte comando:

``` 
pip install -r requirements.txt
``` 

3 - Por fim, executar o script principal

``` 
python main.py 
```


O output do script são as respostas para as questões 1.2, 1.3 e 1.4