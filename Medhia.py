# Este programa calcula a média dos alunos da rede pública do Estado de São Paulo. 
# É uma ferramenta simples, mas que pode ser muito útil tanto para alunos quanto para professores.

# Solicita as notas dos quatro bimestres.
bimestre1 = float(input('Digite a sua nota no primeiro semestre:\n'))
bimestre2 = float(input('Digite a sua nota no segundo semestre:\n'))
bimestre3 = float(input('Digite a sua nota no terceiro semestre:\n'))
bimestre4 = float(input('Digite a sua nota no quarto semestre:\n'))

# Calcula a média.
media = (bimestre1 + bimestre2 + bimestre3 + bimestre4)/4
print ("Sua média é:",media)

# Verifica se o aluno foi aprovado ou reprovado.
if media >= 5:
    print ("Você foi aprovado(a)")
else:
    print ("Você foi reprovado(a)")