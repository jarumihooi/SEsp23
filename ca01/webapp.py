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


@app.route('/')
def index():
    ''' display links to each team member's page '''
    print('processing / route')
    return '''
      <h1>Following links are our team members' links</h1>
      <ul type="circle">
        <li><a href = "/compose">Jeremy Huey</a></li>
        <li><a href = "/proofhelp">Chris Tighe's Math Proof Explainer</a></li>
        <li><a href = "/seasonalfruit">Ijeoma Ogbogu</a></li>
        <li><a href = "/compare">Mengli Yang</a></li>
        <li><a href = "/about">About the Project</a></li>
        <li><a href = "/team">About the Team</a></li>
    </ul>

    '''

@app.route("/about")
def hello_world():
    '''explains what our programs do'''
    return '''<h1> Programs by person: </h1>
        <h3> Chris </h3>
        <p>Math proofs can be difficult to understand. Provide the name of a proof and get an explanation.</p>
        <h3> Mengli </h3>
        <p>Compare program asks the user to ask what numbers they want to compare.</p>
        <h3> Ijeoma </h3>
        <p>Eating seasonally is the best for the environment and the quality of fruit, find out the 
        the best seasons to eat certain fruits.</p>
    '''

@app.route("/team")
def profile():
    '''display team members'pages'''
    return '''
    <h1>This is our team's bio page</h1>
        <p>Our team has four members. They are Jeremy Huey, Mengli Yang, 
         Chris Tighe, and Ijeoma Ogbogu.</p>
        <h3>Chris</h3>
        <p>Chris is a Master's student in the Computer Science department at Brandeis University.<br>
         He finished undergraduate studies in Spring 2022 with a BS in Math and Computer Science.<br>
         His role was general guidance and organization in addition to resolving merge conflicts.</p>
    '''

#leaving in just in case, written: by Tim Hickey
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
    
@app.route('/proofhelp', methods=['GET', 'POST'])
def proofhelp():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        print(prompt)
        answer = gptAPI.proof_help(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('proofhelp')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter the name of a proof or theorem you want explained below.
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        ''' 

@app.route('/compose', methods=['GET', 'POST']) # GET is to jsut get the page. Post is if they pushed the button.
def compose():
    '''
    Explanation of this method
    '''
    if request.method == "POST":
        prompt = request.form['prompt']
        answer = gptAPI.compose(prompt)
        # bug fix lol i put the f behind teh three dashes.
        return f'''
        <h1>Compose-based on mood GPT Demo App</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode: 
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('compose')}> make another query</a>
        '''
        # bugfix: change /proofhelp to /compose
    else:
        return '''
        <h1>Compose-based on mood GPT Demo App</h1>
        Enter a mood that you want musical composition help with:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/seasonalfruit', methods=['GET', 'POST'])
def seasonalfruit():
    '''
        Uses chatgpt to find the best season to eat fruit
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        print(prompt)
        # I'll need to add the string append here for prompt engineering
        answer = gptAPI.seasonal_fruit(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('seasonalfruit')}> make another query</a>
        '''
    else:
        return '''
        <h1>Seasonal Fruit Demo App</h1>
        Enter the name of the fruit to find the best season to eat/buy the fruit.
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''


@app.route('/compare', methods=['GET', 'POST'])
def compare():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.compare(prompt)
        return f'''
        <h1>Compare your numbers here!</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('compare')}> make another query</a>
        '''
    else:
        return '''
        <h1>You are using compare method</h1>
        What are two numbers you want to compare? Enter a full setence below:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
        # makes an html method called post.




if __name__=='__main__':
    app.run(debug=True,port=5001)

