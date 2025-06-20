from flask import Flask, request
import logging

app = Flask(__name__)

# Set up basic file logging
logging.basicConfig(
    filename='app.log',        # Log file name
    level=logging.INFO,        # Log level
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)

@app.route('/')
def home():
    app.logger.info('Home page accessed')
    return 'Hello, Flask with logging! AGAIN!!!'

@app.route('/admin')
def admin():
    app.logger.info('ALERT!!! Admin page accessed')
    return 'You should not be here!'

@app.route('/log')
def log_example():
    user_ip = request.remote_addr
    app.logger.info(f'Log endpoint accessed from {user_ip}')
    return 'Check the log file!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=50001)
