from flask import request
from flask_api import FlaskAPI, status, exceptions
from datetime import datetime
from persistqueue import FIFOSQLiteQueue

q = FIFOSQLiteQueue('my_queue', multithreading=True, auto_commit=True)
app = FlaskAPI(__name__)

"""
- [ ] Create endpoints for POST and GET
- [ ] Think about DELETE...
"""

@app.route('/', methods=['GET', 'POST'])
def manage_queue():
    """
    Pop or Put message in the Queue
    """
    if request.method == 'POST':
        # Create a new queue entry
        msg = request.data.get('message', '')
        data = {'message':msg, 'created_at':datetime.now()}
        q.put(data)
        return f'OK {len(q)} in QUEUE', status.HTTP_201_CREATED
    else:
        # request.method == 'GET'
        msg = q.get()
        return msg

@app.route('/count')
def count_queue():
    return str(len(q))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)


