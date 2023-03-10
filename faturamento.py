import json

# Lê os dados de faturamento diário a partir do arquivo JSON
with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

# Calcula o menor valor de faturamento diário
menor_faturamento = min(faturamento_diario.values())

# Calcula o maior valor de faturamento diário
maior_faturamento = max(faturamento_diario.values())

# Calcula a média de faturamento diário, excluindo os dias sem faturamento
dias_com_faturamento = [faturamento for faturamento in faturamento_diario.values() if faturamento > 0]
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for faturamento in faturamento_diario.values() if faturamento > media_faturamento)

# Exibe os resultados
print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_da_media}")   