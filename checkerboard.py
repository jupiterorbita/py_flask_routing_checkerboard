from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<path:dummy>')
def fallback(dummy):
    return 'This one catches everything else, Sorry! No response. Try again.'

@app.route('/')
def index():
  print('\n-------> /')
  x = 8
  y = 8
  return render_template('index.html', x=x, y=y)

@app.route('/4') # 8x4
def eightByFour():
  print('\n-------> /4')
  x = 4
  y = 4
  return render_template('index.html', x=x, y=y)

@app.route('/<int:x>/<int:y>')
def xByY(x,y):
  print(f'\n------> /{x}/{y}')
  return render_template('index.html', x=x, y=y,)

# SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2

if __name__=="__main__":
  app.run(debug=True)