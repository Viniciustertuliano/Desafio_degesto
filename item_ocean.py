from crawler import crawler_ocean
import json
import csv
import re

instances = {}
num = 0
fieldnames = []
element_header, element_body = crawler_ocean()


def limpa_element(element_header, element_body):
    aux = []
    for i in range(6):
        aux.append(element_header[i])
    aux.pop(4)
    element_header = aux

    aux = []
    for a in range(6):
        for b in range(6):
            aux.append(element_body[0])
            element_body.pop(0)
    element_body = aux
    return element_header, element_body


element_header, element_body = limpa_element(element_header, element_body)


def organiza_element(num, element_header, element_body):
    for b in element_body[::6]:
        num += 1
        instances[num] = {}
        for i in element_header:
            print(element_body)
            if i == 'Memory':
                instances[num][i] = element_body[0]
                element_body.pop(0)
                print(element_body)
            elif i == 'vCPUs':
                instances[num][i] = element_body[0]
                element_body.pop(0)
                print(element_body)
            elif i == 'Transfer':
                instances[num][i] = element_body[0]
                element_body.pop(0)
                print(element_body)
            elif i == 'SSD Disk':
                instances[num][i] = element_body[0]
                element_body.pop(0)
                print(element_body)
                element_body.pop(0)
                print(element_body)
            if i == '$/MO':
                instances[num][i] = element_body[0]
                element_body.pop(0)
                print(element_body)
    return instances


element = organiza_element(num, element_header, element_body)


def escrever_json(element):
    with open('instances_ocean.json', 'w') as f:
        json.dump(element, f)


def escrever_csv(element):
    for a in element[1]:
        fieldnames.append(a)

    with open('instances_ocean.csv', mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, 7):
            aux = []
            for b in element[1]:
                aux.append(element[i][b])
            writer.writerow(
                {"Memory": aux[0], "vCPUs": aux[1],
                 "Transfer": aux[2], "SSD Disk": aux[3], "$/MO": aux[4]})


print(element)
escrever_json(element)
escrever_csv(element)
