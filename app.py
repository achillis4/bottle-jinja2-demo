from bottle import Bottle, run
from jinja2 import Environment, FileSystemLoader

app = Bottle()

# Configure the Jinja2 environment
jinja_env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=True
)

@app.route('/')
def home():
    user_data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com',
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'CA',
            'zip': '12345'
        },
        'hobbies': ['reading', 'hiking', 'photography']
    }
    
    template = jinja_env.get_template('home.html')
    return template.render(title='Home', user=user_data)

if __name__ == '__main__':
    run(app, host='localhost', port=8080)