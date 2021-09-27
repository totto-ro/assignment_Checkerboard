from flask import Flask, render_template

app = Flask(__name__)

@app.route( '/', methods = ['GET'] )
def eightCheckboard():
    return render_template( "index.html", numRow=8, numCol=8)

@app.route( '/<val>', methods=['GET'] )
def narrowCheckboard(val):
    val = int(val)
    return render_template("index.html", numRow=val, numCol=8)

@app.route( '/<x>/<y>', methods=['GET'] )
def anyCheckboard( x, y ):
    valX = int( x )
    valY = int( y )
    return render_template("index.html", numRow=valX, numCol=valY)


if __name__ == "__main__":
    app.run( debug = True)