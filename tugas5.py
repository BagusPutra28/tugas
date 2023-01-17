from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hobi')
def gethobi():

 hobi  = 'Game'
 hobi1 = 'tidur'
 hobi2 = 'makan'
 return render_template('hobiku.html', hobi = hobi, hobi1=hobi1, hobi2=hobi2)

if __name__ == '__main__':
 app.run(debug=True)