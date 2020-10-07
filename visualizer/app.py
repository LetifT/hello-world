from flask import Flask, request, make_response, Response

from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
from resources.plotting import plot_pred
import pandas as pd
# https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask
# https://gist.github.com/rduplain/1641344
app = Flask(__name__)

@app.route('/visualisation/plot_predict.png', methods = ['GET'])
def visualisation():
        """"
        local solution
        predictions = request.get_json() # NOW IT'S A INPUT OF THE REQUEST BUT HAS TO BE ENVIR VAR
        df = pd.read_json(r"test_data.json", orient="split")  # IS LOCAL (HAS TO BE ENVIR VAR I THINK)
        """
        data_api = os.environ['DATA_API']
        data_json = requests.get(data_api).json()
        df = pd.DataFrame.from_dict(data_json)

        # Plot function to visualize a subset of the images with the predictions of the model
        figure = plot_pred(df)

        # figure is written to a png file
        result = io.BytesIO()
        FigureCanvasAgg(figure).print_png(result)

        resp = make_response(result.getvalue())
        resp.mimetype = 'image/png'
        return resp

app.config["DEBUG"] = True
app.run(host='0.0.0.0', port=5000)