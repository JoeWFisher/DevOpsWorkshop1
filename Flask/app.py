from flask import Flask, render_template

app = Flask(__name__)

@app.route('/films/list')
def get_films_list():
   return render_template('film_list.html')
   

@app.route('/films/table')
def get_films():
   with open('filmreviews.txt') as d:
      text_list = d.read().splitlines()
      for line in text_list:
         films = line.split(',')
   return render_template('film_details.html', films = films)    
