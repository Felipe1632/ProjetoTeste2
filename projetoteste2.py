import pandas as pd


# 1 - Leitura do arquivo
df = pd.read_csv('feedbacks.csv', sep=',', encoding='utf-8')
print(df, "\n")



# 2 - Média por curso
media_por_curso = df.groupby("curso")["nota"].mean().reset_index()
print("Média das notas por curso:")
print(media_por_curso, "\n")


# 3 - Melhor e pior curso
melhor_curso = media_por_curso.loc[media_por_curso["nota"].idxmax()]
print("Curso com melhor avaliação:")
print(melhor_curso, "\n")


pior_curso = media_por_curso.loc[media_por_curso["nota"].idxmin()]
print("Curso com pior avaliação:")
print(pior_curso, "\n")


# 4 - Recomendações
recomendacoes = df[df["recomendaria"] == "Sim"]
recomendacoes = recomendacoes.groupby("curso")["recomendaria"].count().reset_index()
recomendacoes = recomendacoes.rename(columns={"recomendaria": "quantidade_recomendacoes"})
print("Recomendações por curso:")
print(recomendacoes, "\n")


# 5 - Feedbacks por dia
df["data"] = pd.to_datetime(df["data"], errors="coerce")
feedbacks_por_dia = df.groupby("data").size().reset_index(name="quantidade_feedbacks")
print("Feedbacks por dia:")
print(feedbacks_por_dia, "\n")


# 6 - Feedbacks negativos
feedbacks_negativos = df[df["nota"] <= 2]
print("Feedbacks negativos:")
print(feedbacks_negativos, "\n")


# 7 - Exportar feedbacks negativos
feedbacks_negativos.to_csv("feedbacks_negativos.csv", index=False, encoding="utf-8")
print("Arquivo 'feedbacks_negativos.csv' criado com sucesso!")
