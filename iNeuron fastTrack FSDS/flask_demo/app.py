from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#For url
@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

#for url
@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)

#For Postman
@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)

#for postman
@app.route('/shiks' , methods=['POST'])
def info():
    if (request.method=='POST'):
        name=request.json['name']
        student_id=request.json['student_id']
        phone_number = request.json['phone_number']
    return jsonify(name + student_id + str(phone_number))
# http://127.0.0.1:5000/shiks
#{'name':"shiks,"student_id":123,"phone_number":991231242} jason input to postman


#for url
@app.route("/abc")
def add_url():
    test1 = request.args.get("val1")
    test2 = request.args.get("val2")
    test3 = int(test1) + int(test2)
    return '''<h1>The result is: {}</h1>'''.format(test3)
#http://127.0.0.1:5000/abc?val1=10&val2=5 put in browser url
#The result is: 15

if __name__ == '__main__':
    app.run()
