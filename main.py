import csv

def normalize_phone(phone):
    if phone.startswith('0') or len(phone) not in (7, 10, 11):
        result = None
    elif len(phone) == 10:
        result = '7' + phone
    elif len(phone) == 7:
        result = '7812' + phone
    elif len(phone) == 11 and phone.startswith('7'):
        result = phone
    else:
        result = None

    return result

with open('phones.txt') as file:
    phones = file.read().splitlines()

result = [normalize_phone(phone) for phone in phones if normalize_phone(phone)]

with open('output.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(('external_id', 'phone'))
    for i, phone in enumerate(result):
        writer.writerow((i + 1, phone))
