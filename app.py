from flask import Flask, render_template, request, escape, session
import requests
import os

app = Flask(__name__)
app.secret_key = "Kommernetkrumm"

api_key = os.environ['APIKEY']

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Fahrplanauskunft")


@app.route('/results', methods=['Post'])
def results():
    station = request.form['station']
    res = RMVquery(station, request.form['lines'])
    title = 'Fahrplanauskunft'
    return render_template('results.html', the_station=station,
                                          the_title=title, the_result=res)


def RMVquery(station, lines):
    url = "http://www.rmv.de/hapi/DepartureBoard"
    duration = "60" 
    querystring = {"accessId":api_key,"extId":station, "format":"json","lines":lines,"duration":duration}
    response = requests.get(url, params=querystring, verify=False)
    r_json = response.json()
    return r_json["Departure"]


    


if __name__ == '__main__':
    app.run(debug=True)
    