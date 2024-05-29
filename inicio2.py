dia_semana = input("Digite os três primeiros dígitos da semana: ")

dia_semana = dia_semana.upper()

if dia_semana == "SEG":
    print("Segunda-feira")
elif dia_semana == "TER":
    print("Terça-feira")
elif dia_semana == "QUA":
    print("Quarta-feira")
elif dia_semana == "QUI":
    print("Quinta-feira")
elif dia_semana == "SEX":
    print("Sexta-feira")
elif dia_semana == "SAB":
    print("Sábado")
elif dia_semana == "DOM":
    print("Domingo")
else:
    print("Entrada inválida Por favor digite os três primeiros dígitos da semana.")