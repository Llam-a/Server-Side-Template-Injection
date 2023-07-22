from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    template = '''
    <html>
    <head><title>SSTI Example</title></head>
    <body>
        <h1>Xin chào, {{ name }}!</h1>
    </body>
    </html>
    '''
    name = request.args.get('name', 'Guest')
    return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run(debug=True)
