from datetime import datetime, date

def calcular_idade(data_nasc_str):
    data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
    hoje = date.today()
    idade = hoje.year - data_nasc.year
    if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
        idade -= 1
    return idade

def verificar_idade(data_nasc_str):
    try:
        data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
        return data_nasc
    except ValueError:
        raise ValueError("Data inválida! Use o formato DD/MM/AAAA.")


