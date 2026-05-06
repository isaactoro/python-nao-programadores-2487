# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;

nome = input('Digite suo nome: ');


# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
Total_dias = input('Digite total dias que estudo pela semana: ');
#print('total', Total_dias);

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
Total_horas = input('Digite horas que estudo por dia: ');

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Digite nome do curso: ');

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print('A pessoa ' + nome + ' estudo em ' + Total_dias + ' dias ' + Total_horas + ' horas por dia, em total estudo' + (Total_dias * Total_horas) + ' horas pela semana pra o curso ' + curso);