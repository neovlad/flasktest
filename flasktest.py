
from flask import Flask,render_template,request
import pandas_highcharts,get_chart_data
from pandas_highcharts.core import serialize
from get_code import get_next
app = Flask(__name__)
mycode="WIKI/MDT"
@app.route("/")
def getdata():

	mydataless = get_chart_data.getdata("WIKI/FB",1,2)
	return mydataless.to_html()

@app.route("/chart",methods=['GET'])
def  makechart(code='WIKI/MDT'):
	global mycode
	mycode= code

	mydata = get_chart_data.getdata(code,1,2)
	chart = serialize(mydata,render_to='my-chart', output_type='json')
	return render_template("temp.html",chart=chart)

@app.route("/raw")
def rawdata():
	global mycode
	return get_chart_data.getdata( mycode).to_html()
@app.route("/nextchart")
def nextchart():
	global mycode
	return makechart(get_next(mycode))
if __name__ == "__main__":
	app.run(debug=True)
