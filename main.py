from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_url = request.form['image_url']
        prompt = request.form['prompt']

        url = "https://api.thenextleg.io/v2/imagine"
        payload = json.dumps({
            "msg": f"{image_url} {prompt}",
            "ref": "",
            "webhookOverride": ""
        })
        headers = {
            'Authorization': 'Bearer 4c6741d5-9907-4bfd-9bf6-f1ab9f901170',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        webhook_image_code = json.loads(response.text)['webhookImageCode']
        return render_template('image.html', webhook_image_code=webhook_image_code)

    return render_template('image.html')
if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, render_template
# import requests
# import json

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         image_url = request.form['image_url']
#         prompt = request.form['prompt']

#         url = "https://api.thenextleg.io/v2/imagine"
#         payload = json.dumps({
#             "msg": f"{image_url} {prompt}",
#             "ref": "",
#             "webhookOverride": ""
#         })
#         headers = {
#             'Authorization': 'Bearer 4c6741d5-9907-4bfd-9bf6-f1ab9f901170',
#             'Content-Type': 'application/json'
#         }

#         response = requests.request("POST", url, headers=headers, data=payload)
#         webhook_image_code = json.loads(response.text)['webhookImageCode']
#         return render_template('result.html', webhook_image_code=webhook_image_code)

#     return render_template('home.html')

# if __name__ == '__main__':
#     app.run(debug=True)