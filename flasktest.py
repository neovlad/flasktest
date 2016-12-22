
from flask import Flask,render_template
import pandas_highcharts,get_chart_data
from pandas_highcharts.core import serialize

app = Flask(__name__)

@app.route("/")
def getdata():
	mydataless = get_chart_data.getdata("WIKI/FB",1,2)
	return mydataless.to_html()

@app.route("/chart")
def  makechart():
	mydata = get_chart_data.getdata("WIKI/FB",1,2)
	chart = serialize(mydata,render_to='my-chart', output_type='json')
	return render_template("temp.html",chart=chart)

@app.route("/raw")
def rawdata():
	return get_chart_data.getdata("WIKI/FB").to_html()

if __name__ == "__main__":
	app.run(debug=True)
