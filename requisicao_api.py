import requests

def return_data_delivery(data_item):

    print(f"======= DADOS DA ENTREGA =======")
    print(f'CEP: {data_item["cep"]}')
    print(f'localidade: {data_item["localidade"]}')
    print(f'uf: {data_item["uf"]}')
    print(f'bairro: {data_item["bairro"]}')
    print(f'complemento: {data_item["complemento"]}')
    print(f'logradouro: {data_item["logradouro"]}')
    print("======= ============ ==========\n")

def query_CEP(cep_len):

    if len(cep_len) != 8:
        print("----------   FORMATACAO DE CEP INVALIDA  ---------")  
        exit()
    
def data_json(cep_item):
    r = requests.get(f"http://viacep.com.br/ws/{cep_item}/json/")
    addres_data = r.json()
    return addres_data

def main():
    print("#### CONSULTA CEP VIA CONSUMO DE API ####")
    cep = input("Digite o CEP: ")
    query_CEP(cep)
    json = data_json(cep)
    if "erro" in json:
        print("CEP NAO EXISTE")
    else:
        print("\x1b[2J")
        return_data_delivery(json)
    repeat_action()
    
def repeat_action():
    print("Deseja Repetir a operação?")
    result = input("1 - SIM \n2 - NAO \n\nOpcao: ")
    match result:
        case '1':
            return main()
        case '2':
            return print("Saindo...")
        case _:
            return print("Resposta Invalida")

 
if __name__ == "__main__":
    main()
