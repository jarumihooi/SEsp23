'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell, switch to ubuntu rofl. Then use $ . secret.sh (make sure its chmod +x)
% to check, then use $ export -p and look for at the top: declare -x APIKEY="<the key>>"
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"


    def compose(self,compose_prompt):
        '''Compare two number'''
        prompt = "Please give a musical composition or chord changes based on this mood: " + compose_prompt
        print("prompt", prompt)
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt = prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        print("response", response)
        return response

    def compare(self, prompt):
        '''Compare two number'''
        prompt = "What are two numbers you want to compare? enter a full sentence, please: " + prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt = prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    def proof_help(self,prompt):
        '''helps explain math proofs'''
        prompt = "Please explain the following mathematical proof or theorem in plain english: " + prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt = prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def seasonal_fruit(self,prompt):
        '''helps explain math proofs'''
        prompt = "Please give the best season to eat : " + prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt = prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response


if __name__=='__main__':
    import os
    g = GPT(os.environ.get("APIKEY"))
    