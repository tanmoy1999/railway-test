from flask import Flask, jsonify
import os
from lxml import etree
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/mmi')
def mmi():
    URL = 'https://www.tickertape.in/market-mood-index'
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                'Accept-Language': 'en-US, en;q=0.5'})
  
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    mmi = dom.xpath('//*[@id="app-container"]/div/div[1]/div[1]/div/div[2]/span')[0].text
    day = dom.xpath('//*[@id="app-container"]/div/div[1]/div[1]/div/div[2]/p/text()[2]')[0]
#     return render_template("MMI.html",mmi_page = mmi,last_updated = day)
    return jsonify({mmi: day})

# if __name__ == '__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000))
if __name__ == "__main__":
    app.run(debug=True, port=8000)
