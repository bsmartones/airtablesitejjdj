from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<page_id>')
def serve_page(page_id):
    return send_from_directory('generated_html', f'{page_id}.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
