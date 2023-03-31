from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!"

if __name__=="__main__":
    logger.debug("Application is starting")
    #app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
    app.run(debug=True)


