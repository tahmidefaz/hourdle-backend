from api import get_app

app = get_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
