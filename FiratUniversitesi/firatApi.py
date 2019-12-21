from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
@app.route('/firat', methods=['GET'])
def yemekList():
    response = {"result": False, "error": 'Menu Not Found'}
    try:
        returnList = []
        page = requests.get("http://uevi.firat.edu.tr/")
        soup = BeautifulSoup(page.content, 'html.parser')

        menu_HTML = soup.select(
            "div > div > div > div > div.views-field.views-field-body > div")
        date_HTML = soup.select(
            "div > div > div > div > div.views-field.views-field-created > span")

        if(len(menu_HTML) != 0 and len(date_HTML) != 0):
            menuList = menu_HTML[0].text.split('\n')

            for item in menuList:
                if(len(item) > 2):
                    returnList.append(item)
            response = {"result": True, "data": {
                "date": date_HTML[0].text,
                "menu": returnList}}
        else:
            print("hata")
            response = {"result": False, "error": 'Menu Not Found'}
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify(response)
    return jsonify(response)


app.run(host='0.0.0.0', port=5002, debug=True)
