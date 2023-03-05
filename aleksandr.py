import sys
import logging
import re
import openai
import os
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("OPENAI")

input_1 = sys.argv[1]

#
# A function to remove URLs
#
def remove_urls(text):
    return re.sub(r'http\S+', '', text)

#
# A function to mentions from tweets 
#
def remove_mentions(text):
  return re.sub(r'@\S+', '', text)

#
# A function to remove special characters
#
def remove_special_characters(text):
  return re.sub(r'[^\w\s]', '', text)


def clean_tweet(text):
    text = remove_urls(text)
    text = remove_mentions(text)
    text = remove_special_characters(text)
    return text


def getPrompt(prompt_text):
    
    question = f'''
    The topic is ChatGPT. Based on the following text, identify if the author is confident in ChatGPT / not confident in ChatDPT / neutral.
    Text: "{prompt_text}"

    Answer (one word lowercase):
    '''
    
    return question


openai.api_key = key

prompt = getPrompt(clean_tweet(input_1))

response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0)

answer = str(response.choices[0].text)
answer = answer.replace(" ", "")
answer = answer.replace("\n", "")
answer = answer.replace("notconfident", "not confident")

print(answer)
