from datetime import datetime

def formata_data(dia, mes, ano):
    data = datetime.today().replace(month=mes, day=dia, year=ano)
    return data.strftime('%d de %B de %Y')

print(formata_data(9, 6, 1993))