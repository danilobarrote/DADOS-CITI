import pandas as pd

#carregando a base despadronizada
df = pd.read_csv("Base_despadronizada.csv")

#padronizando a coluna sexo
sexo_map = {
    'm': 'Masculino', 'masc': 'Masculino', 'masculino': 'Masculino',
    'f': 'Feminino', 'fem': 'Feminino', 'feminino': 'Feminino'
}
#tirei os espaços e deixei tudo minusculo para mapear
df['sexo'] = df['sexo'].str.strip().str.lower().map(sexo_map)

# Corrige notas para float (separadas por virgula)
df['nota_matematica'] = df['nota_matematica'].astype(str).str.replace(',', '.').astype(float)
df['nota_portugues'] = df['nota_portugues'].astype(str).str.replace(',', '.').astype(float)

# Calcula média
df['media'] = (df['nota_matematica'] + df['nota_portugues'] + (df['frequencia'] / 10)) / 3

# Adiciona coluna de aprovação
df['aprovado'] = df['media'].apply(lambda x: 'Sim' if x >= 7 else 'Não')

# Salva resultado
df.to_csv("Base_tratada.csv", index=False)
print("Arquivo salvo como Base_tratada.csv")