import requests
from flask import Flask
from flask import request, jsonify
from lxml import html
import unicodedata


app = Flask(__name__)
@app.route('/firat', methods=['GET'])
def yemekList():
    try:
        returnList=[]
        pageContent = requests.get('http://uevi.firat.edu.tr/')
        tree = html.fromstring(pageContent.content)
        
        yemekList = tree.xpath('//div/div/div/div/div[4]/div')
        
        tarih = tree.xpath('//*[@id="block-views-haberler-block"]/div/div/div/div/div[3]/span/text()')
        
        if(tarih[0] != '' or tarih[0] != None):
            returnList.append(tarih[0])
        
        for item in yemekList[0]:
            new_str = unicodedata.normalize("NFKD", item.text)
            if(new_str != ' '):
                returnList.append(new_str)
        return jsonify(returnList)
    except:
        print("Hata")
        return jsonify(-1)
    return jsonify(-1)

app.run(host='0.0.0.0', port=5002, debug=True)
