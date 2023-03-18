'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 webapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display links to each team member's page '''
    print('processing / route')
    return '''
      <h1>Following links are our team members' links</h1>
      <ul type="circle">
        <li><a href = "https://github.com/jarumihooi">Jeremy Huey</a></li>
        <li><a href = "https://github.com/ctighebrandeis">Chris Tighe</a></li>
        <li><a href = "https://github.com/i-bog?tab=repositories">Ijeoma Ogbogu</a></li>
        <li><a href = "https://github.com/mengliyang2023">Mengli Yang</a></li>
    </ul>

    '''

@app.route("/about")
def hello_world():
    '''explains what our programs do'''
    return "<h1> compare program is used to compare two numbers </h1>"

@app.route("/team")
def profile():
    '''display team members'pages'''
    return '''
    <h1>this is our team's bio page</h1>
        <p>Our team has four members. They are Jeremy Huey, Mengli Yang, 
         Chris Tighe, and Ijeoma Ogbogu.</p>
    '''

@app.route('/form', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.compare(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

if __name__=='__main__':
    app.run(debug=True,port=5001)
