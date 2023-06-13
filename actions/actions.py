import os
from typing import Any, Text, Dict, List
import pandas as pd
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import openai
from dotenv import load_dotenv



class ChatGPT(object):

    def __init__(self):
        load_dotenv()
        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-3.5-turbo"
        self.headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('Open_API_key')}"
            
        }
        

    def ask(self, article, question):
        prompt =f" Give a desciption for the text delimited by  triple backticks ```{article}``` "
        content  = prompt + '/n/n' + article + '/n/n' + question
        body = {
            "model":self.model, 
            "messages":[{"role": "user", "content": content}]
        }
        result = requests.post(
            url=self.url,
            headers=self.headers,
            json=body,
        )
        #print(result)
        return result.json()["choices"][0]["message"]["content"]



chatGPT = ChatGPT()

class ActionDescribe(Action):

    def name(self) -> Text:
        return "action_describe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message["text"]
        print(os.getenv('Open_API_key'))
        # summary.append(question)
        # content = (','.join(summary))
        

        with open("test.txt") as file:
            lines = file.readlines()
        article = '\n'.join(lines)
        print(article)
        reply_content = chatGPT.ask(article, question)
        print(reply_content)
        dispatcher.utter_message(text=f"Here are some description\n{reply_content}")
