import json
from flask import Flask, render_template

app = Flask(__name__)


path_to_json = 'data/PeriodicTableJSON.json'


class Element(object):
    def __init__(self, **kwargs):
        self.attributes = kwargs


class ElementStore(object):
    def __init__(self):
        self.data = ElementStore.get_element_data_from_file(path_to_json)
        self.elements = self.map_nrs_to_details()

        def cut_first_phrase(elements):
            for number in elements:
                item = elements[number]
                item['summary'] = '.'.join(item['summary'].split('.')[1:])

        cut_first_phrase(self.elements)
        self.lanthanides_and_actinides = self.get_lanthanides_and_actinides()


    def get_element_by_number(self, number):
        return [item for item in self.data if item['number'] == number].pop()

    def map_nrs_to_details(self):
        return {item['number']: {attribute: item[attribute] for attribute in item.keys()} for item in self.data}

    @staticmethod
    def get_element_data_from_file(json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        return data['elements']

    def get_lanthanides_and_actinides(self):
        return [{element[0]: element[1] for element in self.elements.items() if element[1]['category'] == 'lanthanide'},
                {element[0]: element[1] for element in self.elements.items() if element[1]['category'] == 'actinide'}]


class PeriodicLayout(object):
    def __init__(self):
        periodic_table = [[1 if PeriodicLayout.valid_row_and_column(row, column)
                             else 0 for column in range(18)] for row in range(7)]
        PeriodicLayout.fill_atomic_numbers(periodic_table)
        PeriodicLayout.insert_lanthanides_and_actinides(periodic_table)
        self.layout = periodic_table


    @staticmethod
    def valid_row_and_column(row, column):
        if (row in range(3,7) or
            column in (0,1,12,13,14,15,16,17) and row in (1,2) or
            column in (0,17) and row == 0):
            return True
        else:
            return False

    @staticmethod
    def fill_atomic_numbers(table):
        index = 1
        for row_n, row in enumerate(table):
            for column, item in enumerate(row):
                if item:
                    table[row_n][column] = index
                    index += 1

    @staticmethod
    def insert_lanthanides_and_actinides(table):
        for row_n, row in enumerate(table):
            for column, item in enumerate(row):
                if item == 57:
                    table[row_n][column] = 0
                if item > 57:
                    table[row_n][column] = item + 14

        for row_n, row in enumerate(table):
            for column, item in enumerate(row):
                if item == 89:
                    table[row_n][column] = 0
                if item > 89:
                    table[row_n][column] = item + 14


@app.route('/')
def index():
    element_store = ElementStore()
    elements = element_store.elements
    lanthanides_and_actinides = element_store.lanthanides_and_actinides
    return render_template('index.html',
                            periodic_table=PeriodicLayout().layout,
                            data=elements,
                            lanthanides_and_actinides=lanthanides_and_actinides)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
