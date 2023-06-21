from main import create_app
import os

app = create_app()
#un tipo de globalicacion de app
app.app_context().push()

#verificacion de la app de parte de flask
if __name__ == '__main__':
    app.run(port=os.getenv("PORT"), debug=True)