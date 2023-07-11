from app.controllers import login 
from app.controllers import base 
from app.controllers import menu_principal

from app import app
if __name__=="__main__":
    app.run(debug=True, port=3000)   