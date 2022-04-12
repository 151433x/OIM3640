from tempfile import tempdir
from flask import Flask



@app.route('/weather/',methods=['GET',"POST"])
def show_weather():
    if request.method == "POST":
        city_name=request.form['city']
        temerature=get_temp(city_name)
        return render_template('weather-result.html',city=city_name,temp=str(temerature)
