import pandas as pd # type: ignore
import os # Biblioteca para se comunicar com o sistema operacional
import glob

# Função de extract que le e consolida

def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame: # Aqui criamos a função declarando o nosso parâmetro que chamos só dentro da função.
    arquivos_json = glob.glob(os.path.join(pasta,'*.json')) # Como são vários arquivos json usamos o glob e o os para listar e fazer um join em tudo o que estiver dentro da pasta data e tenham qualquer nome (*) com .json.
    df_list = [pd.read_json(arquivo)for arquivo in arquivos_json] # Agora com o for nos estamos lendo cada arquivo dentro dos arquivos_json e tranformar em um json.
    df_total = pd.concat(df_list, ignore_index=True) # Aqui estamos concatenando os dataframes jsons criados anteriormente e criando um indice novo.
    return df_total

# Função que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

# Função que da load em csv ou parque

def carregar_dados(df: pd.DataFrame, formato_saida: list): # Aqui criamos um parâmetro onde o output vai poder ser um csv, parquet ou os dois. Esse def vai ter uma caracteristica de procedure, porque ele não vai ter return, queremos só que ela salve.
    for formato in formato_saida: # Aqui tivemos que criar um for para interar sobre os metodos de saida.
        if formato == 'csv':
            df.to_csv('dados.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('dados.parquet', index=False)

# Função para a pipeline do usuário final:

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list): # Criamos essa função para facilitar para o usuário
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)




# Area de teste: Usamos na contrução das funções

# if __name__ == "__main__": # Quando formos testar usamos o if __name__ == "__main__":. Dessa maneira garante que não vamos atrapalhar as execuções quando colocarmos os modulos pq o código abaixo só será executado caso esse seja o scrip principal a ser rodado.
#     pasta_argumento: str = 'data' # Esse é o parâmetro real que vamos estar colocando na função conforme print abaixo
#     data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
#     data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
#     formato_de_saida: list = ['csv', 'parquet']
#     carregar_dados(data_frame_calculado, formato_de_saida)