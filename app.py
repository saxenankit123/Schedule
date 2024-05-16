from flask import Flask, render_template

app = Flask(__name__)

data = {
    "child_details":{
        "child_name": "Suraj Mani", 
        "age": 1, 
        "parent_name": "Raja Mani",
    },
    "vaccine_details":[
    {"age": "At birth", "vaccine": "HepB: 1st Dose", "due_date": "15-04-2024"},
    {"age": "2 Months", "vaccine": "Hep B: 2nd Dose", "due_date": "15-04-2024"},
    {"age": "2 Months", "vaccine": "RV: 1st Dose", "due_date": "15-04-2024"},
    {"age": "2 Months", "vaccine": "DTaP: 1st Dose", "due_date": "15-04-2024"},
    {"age": "2 Months", "vaccine": "Hib: 1st Dose", "due_date": "15-04-2024"},
    {"age": "Snazzy", "vaccine": "PCV13: 1st Dose", "due_date": "15-04-2024"},
    {"age": "Snazzy", "vaccine": "IPV: 1st Dose", "due_date": "15-04-2024"},
    {"age": "4 Months", "vaccine": "RV: 2nd Dose", "due_date": "15-04-2024"},
    {"age": "4 Months", "vaccine": "DTaP: 2nd Dose", "due_date": "15-04-2024"},
]
    }


@app.route("/")
def index():
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True,port=8000)