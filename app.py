from flask import Flask, request

app = Flask(__name__)
tasks = []

# Beispiel für eine reine Funktion (A1G)
def quadrat_berechnen(zahl):
    return zahl ** 2

@app.route('/quadrat', methods=['POST'])
def quadrat_endpunkt():
    zahl = float(request.form.get('zahl'))
    quadrat_resultat = quadrat_berechnen(zahl)
    return f"Eingegebene Zahl: {zahl}, Quadrat Resultat: {quadrat_resultat}"

# (A1F) & Erweitert (A1E)
def create_task(description):
    return {'description': description, 'completed': False}

def add_task(task):
    tasks.append(task)

@app.route('/add_task', methods=['POST'])
def add_task_route():
    task = create_task(request.form.get('task'))
    add_task(task)
    return "Aufgabe hinzugefügt: " + task['description']

# (C1G) addon
def get_task_description(task):
    return task['description']
# (B2F), (B1E) & Ein Teil von (B1G) noch übrig
@app.route('/sort_tasks', methods=['GET'])
def sort_tasks():
    sorted_tasks = sorted(tasks, key=get_task_description)
    return {"sorted_tasks": sorted_tasks}

# (B2G) & ein Teil von (B1F)
def sort_task_list(task_list, key_function):
    return sorted(task_list, key=key_function)

# (B3E): (Sortieren nach Länge der Beschreibung)
@app.route('/sort_tasks_lambda', methods=['GET'])
def sort_tasks_lambda():
    sorted_tasks = sort_task_list(tasks, key_function=lambda x: len(x['description']))
    return {"sorted_tasks": sorted_tasks}

def sort_task_list(task_list, key_function):
    return sorted(task_list, key=key_function)

# (C1F) ein teil von (B2E)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Division durch Null nicht möglich!"

@app.route('/calculate', methods=['POST'])
def calculate_endpoint():
    expression = request.form.get('expression')
    x = float(request.form.get('x'))
    y = float(request.form.get('y'))

    # Verwendung der neuen Funktionen
    result = None
    if expression == 'add':
        result = add(x, y)
    elif expression == 'subtract':
        result = subtract(x, y)
    elif expression == 'multiply':
        result = multiply(x, y)
    elif expression == 'divide':
        result = divide(x, y)

    return f"Ergebnis: {result}"

# (B3G): Einfacher Lambda-Ausdruck zur Großschreibung
@app.route('/uppercase', methods=['POST'])
def uppercase_endpoint():
    text = request.form.get('text')
    uppercase_conversion = lambda x: x.upper()
    result = uppercase_conversion(text)
    return f"Umgewandelter Text: {result}"

# (B3F): Lambda-Ausdruck mit mehreren Argumenten für Potenz
@app.route('/power', methods=['POST'])
def power_endpoint():
    base = float(request.form.get('base'))
    exponent = float(request.form.get('exponent'))

    power_calculation = lambda x, y: x ** y
    result = power_calculation(base, exponent)

    return f"Ergebnis der Potenz: {result}"

# (B4G)
@app.route('/map_example', methods=['POST'])
def map_example():
    numbers = list(map(int, request.form.get('numbers').split(',')))
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squared_numbers = list(map(lambda x: x ** 2, even_numbers))
    return {"even_squared_numbers": squared_numbers}

# (B4F)
@app.route('/data_processing', methods=['POST'])
def data_processing():
    numbers = list(map(int, request.form.get('numbers').split(',')))
    # Using Map, Filter, and Reduce Combined
    processed_data = sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    return {"processed_data": processed_data}

# B4E: Using Map, Filter, and Reduce for Complex Data Processing
@app.route('/complex_data_processing', methods=['POST'])
def complex_data_processing():
    data_strings = request.form.get('data_strings').split(',')

    # Map, Filter, and Reduce
    processed_data = ', '.join(map(lambda s: s.upper(), filter(lambda s: len(s) > 3, data_strings)))
    return {"processed_data": processed_data}


@app.route('/')
def home():
    return "Willkommen wähle ein Endpoint!"


if __name__ == '__main__':
    app.run(debug=True)



