from crawler import element_header, element_body, element_memory
import json, csv


instances = {}
num = 0
fieldnames = []


def organiza_element(num, element_header, element_body, element_memory):
    element_header.pop(0)
    for b in element_body[::4]:
        num += 1
        instances[num] = {}
        for i in element_header:
            if i == 'Storage':
                instances[num][i] = element_body[0]
                element_body.pop(0)
            elif i == 'CPU':
                instances[num][i] = element_body[0]
                element_body.pop(0)
            elif i == 'Memory':
                instances[num][i] = element_memory[0]
                element_memory.pop(0)
            elif i == 'Bandwidth':
                instances[num][i] = element_body[0]
                element_body.pop(0)
            elif i == 'Price':
                instances[num][i] = element_body[0]
                element_body.pop(0)
    return(instances)


element = organiza_element(num, element_header, element_body, element_memory)


def escrever_json(element):
    with open('instances_vultr.json', 'w') as f:
        json.dump(element, f)


def escrever_csv(element):
    for a in element[1]:
        fieldnames.append(a)

    with open('instances_vultr.csv', mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, 11):
            aux = []
            for b in element[1]:
                aux.append(element[i][b])
            writer.writerow(
                {"Storage": aux[0], "CPU": aux[1],
                 "Memory": aux[2], "Bandwidth": aux[3], "Price": aux[4]})


print(element)
escrever_json(element)
escrever_csv(element)
