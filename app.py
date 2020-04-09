import flask
import fitz
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def PdfToPng(): 
    pdffile = 'pdf-sample.pdf'
    doc = fitz.open(pdffile)
    page = doc.loadPage(0) #number of page
    #zoom page
    zoom_x = 10.0
    zoom_y = 10.0
    mat = fitz.Matrix(zoom_x, zoom_y)
    pix = page.getPixmap(matrix = mat)
    #pix = page.getPixmap()
    output = "outfile.png"
    pix.writePNG(output)
    
    return jsonify({"Termino": True})

def main(): 
    PdfToPng()

if __name__ == "__main__": 
    # calling the main function 
    main() 

app.run()