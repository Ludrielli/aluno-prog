def calcular_media(notas):
  """Calcula a média de uma lista de notas."""
  return sum(notas) / len(notas) if notas else 0

def classificar_aluno(media):
  """Classifica o aluno com base na sua média."""
  if media >= 7.0:
    return "Aprovado"
  elif media >= 5.0:
    return "Recuperação"
  else:
    return "Reprovado"

# Entrada de dados
notas_str = input("Digite as notas dos alunos separadas por espaço: ")
notas = [float(nota) for nota in notas_str.split()]
num_alunos = len(notas)

# Processamento das notas e classificação dos alunos
situacoes = []
for nota in notas:
  media_aluno = nota  # No nosso caso simples, a nota já é a média
  situacao = classificar_aluno(media_aluno)
  situacoes.append(situacao)

# Cálculo da média geral
if notas:
  media_geral = calcular_media(notas)
else:
  media_geral = 0

# Saída de dados
print(f"\nMédia geral da turma: {media_geral:.1f}")
for i in range(num_alunos):
  print(f"Aluno {i+1}: Nota = {notas[i]:.1f}, Situação = {situacoes[i]}")