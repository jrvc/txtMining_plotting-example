from flask import Flask, render_template, request
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt
import re
import nltk

fpath='data/enwiki-20181001-corpus.100-articles.txt'
with open(fpath,'r') as f:
    soup = BeautifulSoup(f)

example_data = {art['name']:art.text for art in soup.find_all('article') }
#Initialize Flask instance
app = Flask(__name__)

def generate_plot(query,art_name, content, pieces):
    fig = plt.figure()
    plt.title(art_name)
    #pieces.split('...\n...')
    fdist = nltk.FreqDist(content.split())
    plt.savefig('static/'+art_name+'_plt.jpg')

    #fig
def extract_pieces(query,content):
    start_indexes = [m.start() for m in re.finditer(query,content.lower())]
    pieces=[]
    for i in start_indexes: 
        index1=content[max(i-15,0):i].find('\n')+1
        index2=content[i:i+100].find('\n')
        pieces.append('...'+content[i-15+index1:i+100-(100-index2)*(index2>0)]+'...')
        #print(i, content[i-15+index1:i+100-(100-index2)*(index2>0)])
    return pieces

#Function search() is associated with the address base URL + "/search"
@app.route('/search')
def search():

    #Get query from URL variable
    query = request.args.get('query')

    #Initialize list of matches
    matches = []

    #If query not empty
    if query:
        #Look at each entry in the example data
        for art_name,content in example_data.items():
            #If an entry name contains the query, add the entry to matches
            if query.lower() in content.lower():
                extracted_content = extract_pieces(query.lower(),content)
                matches.append({'name':art_name,'content':extracted_content,'pltpath':art_name+'_plt.jpg' })
                generate_plot(query.lower(),art_name,content,extracted_content)

    #Render index.html with matches variable
    return render_template('index.html', matches=matches)
