import subprocess
import json
from analyse import data_append_to_json
from flask import Flask, render_template, request, jsonify, send_file
app = Flask(__name__)

def read_from_terminal(command:str)-> str:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode().strip()

@app.route("/")
def hello():
    return render_template('chat.html')

def read_from_json():
    with open('data.json', 'r') as file:
        data = json.load(file)

    input_values = [item['input'] for item in data]
    return input_values


@app.route("/get")
def get_bot_response():
        message = request.args.get('msg')

        print(message)
        if 'http' in message:
            company_names = read_from_json()
            company_names = ','.join(company_names)
            data_append_to_json(message)
            print("succesfuly data append to json")
            mesage = f'find the three most similar companies {company_names} compared to this {message} company '
            comand = f'ollama run llama3 {mesage}'
            print(comand)
            result = read_from_terminal(comand) 
            print(result)  
            return result
        else :
            print('yes')
            comand = f'ollama run llama3 {message}'
            result = read_from_terminal(comand) 
            print(result)  
            return result
        
@app.route('/download_csv')
def download_csv():
    return send_file('data.json', as_attachment=True)        

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




