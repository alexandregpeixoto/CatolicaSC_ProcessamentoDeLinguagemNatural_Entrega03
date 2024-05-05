import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixe os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('vader_lexicon')

# Ler os dados da transcrição
transcricao = pd.read_csv('transcricao_reuniao.csv')

# Função para buscar termos específicos na transcrição
def buscar_termos(termo):
    resultados = []
    for index, row in transcricao.iterrows():
        texto = row['FRASE']
        pessoa = row['LOCUTOR']
        tokens = word_tokenize(texto.lower())
        if termo.lower() in tokens:
            resultados.append((pessoa, texto))
    return resultados

# Função para realizar análise de sentimento em uma frase
def analisar_sentimento(frase):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(frase)
    if score['compound'] >= 0.05:
        return 'positivo'
    elif score['compound'] <= -0.05:
        return 'negativo'
    else:
        return 'neutro'

# Loop principal
while True:
    # Solicitar termo ao usuário
    termo = input("Digite o termo que deseja buscar na transcrição ('sair' para encerrar): ")
    
    # Verificar se o usuário deseja sair
    if termo.lower() == 'sair':
        print("Encerrando o programa...")
        break
    
    # Buscar termo na transcrição e mostrar resultados
    resultados = buscar_termos(termo)
    if len(resultados) > 0:
        print(f"Resultados para o termo '{termo}':")
        for pessoa, texto in resultados:
            sentimento = analisar_sentimento(texto)
            print(f'{pessoa}: {texto} - Sentimento: {sentimento}')
    else:
        print(f"O termo '{termo}' não foi encontrado na transcrição.")
