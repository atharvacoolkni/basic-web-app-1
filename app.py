from flask import Flask , render_template


app = Flask(__name__)

JOBS = [
    {'id' : 1,
     'title' : 'data analyst',
     'location' : 'bangalore',
     'salary' : 'rs.10,00,000'
    },
    {'id' : 2,
     'title' : 'SDE',
     'location' : 'HYD',
     'salary' : 'rs.5,00,000'
    },
    {'id' : 1,
     'title' : 'research',
     'location' : 'usa',
     'salary' : 'rs.60,00,000'
    },

]

@app.route("/")

def hello():
    return render_template('home.html' , jobs = JOBS)

if __name__ == "__main__":
    app.run( host = '0.0.0.0'  ,debug = True)