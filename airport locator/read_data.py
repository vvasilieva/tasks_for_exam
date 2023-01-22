"""Модуль чтения файла формата json."""

import json


def read_file(name):
    """Функция чтения файла json."""
    with open(name, 'r') as f_obj:
        airports = json.load(f_obj)
        countries = {}
        for elem in airports:
            if elem['country'] not in countries:
                countries[elem['country']] = []
            airport = elem['city']
            if elem['iata'] is not None and elem['iata'] != '\\N':
                airport += '-' + elem['iata']
            elif elem['icao'] is not None and elem['icao'] != '\\N':
                airport += '-' + elem['icao']
            countries[elem['country']].append(airport)
    return countries

