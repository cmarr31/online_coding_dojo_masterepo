from flask import Flask, render_template, request, redirect
app = Flask(__name__)   


@app.route('/')                                             
def user_info():
  return render_template('index.html') 


@app.route('/result', methods=['POST'])
def display_info():
	print "User's Information"
	name = request.form['users_name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return redirect('/')


# @app.route('/dojos/new')
# def dojos():
#   return render_template('dojos.html')





app.run(debug=True)