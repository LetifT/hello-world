from flask import Flask, request, make_response, Response
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

# https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask
# https://gist.github.com/rduplain/1641344
app = Flask(__name__)

@app.route('/visualisation/plot_predict.png', methods = ['GET'])
def visualisation():
        figure = Figure()
        x = [1,2,3,4,5]
        y = [2,2,2,2,2]

        f = figure.add_subplot(1,1,1)
        f.plot(x,y)

        result = io.BytesIO()
        FigureCanvasAgg(figure).print_png(result)
        resp = make_response(result.getvalue())
        resp.mimetype = 'image/png'
        return resp

app.run(debug=True)
app.run(host='0.0.0.0', port=5000)