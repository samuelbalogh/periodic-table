from flask import Flask, render_template

app = Flask(__name__)

periodic_table = [[1 if row in range(3,7) or column in (0,1,12,13,14,15,16,17) and row in (1,2)
                     or column in (0,17) and row == 0 else 0 for column in range(18)] for row in range(7)]


def fill_table(table):
    index = 1
    for row_n, row in enumerate(table):
        for column, item in enumerate(row):
            if item:
                table[row_n][column] = index
                index += 1

def insert_lanthanides_and_actinides(table):
    for row_n, row in enumerate(table):
        for column, item in enumerate(row):
            if item > 56:
                table[row_n][column] = item + 14


@app.route('/')
def index():
    fill_table(periodic_table)
    insert_lanthanides_and_actinides(periodic_table)
    for row in periodic_table:
        print(row)

    return render_template('index.html', periodic_table=periodic_table)

if __name__ == '__main__':
    app.run(debug=True)
