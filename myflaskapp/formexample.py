from flask import Flask, render_template, request, flash
from forms import ContactForm
import keras
from keras import layers,models,optimizers
from PIL import Image
import io

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()  
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         print("see below")
#         print(form.name.data)
         print("see abhove")
         return render_template('contact.html', form = form)
      else:
         return render_template('success.html')
   elif request.method == 'GET':
     print("get only")  
     return render_template('contact.html', form = form)
 
@app.route('/',methods=['GET'])
def homepage():
    return '<h1>Welcome to our image classification page</h1>'

@app.route('/showImage',methods=['GET'])
def showImage():
    return '<img src="https://static.agcanada.com/wp-content/uploads/sites/5/2018/11/apple_GettyImages186843005_cmyk.jpg" alt="Smiley face" width="42" height="42">'

if __name__ == '__main__':
   app.run(debug = True)
