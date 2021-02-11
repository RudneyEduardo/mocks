from flask import Flask, request, render_template
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
import time
from twilio.rest import Client
from app_es import app_es

app = Flask(__name__)
app.register_blueprint(app_es)

@app.route("/")
def hello_world():
    return "<p>Olá, Mundo!</p>"

@app.route('/bot', methods=['POST'])
def bot():
    lista_bancos = ["itau", "bradesco", "citibanamex", "banorte", "santander",
                    "banco do brasil", "caixa", "BB", "Nubank", "BTG", "banese"]
    confirmacoes_texto = ["confirmar","confirma","si"]

    incoming_msg = request.values.get('Body', '').lower()
    incoming_num = request.values.get('From', '').lower()

    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'seguro' in incoming_msg:
        # return a quote
        r = "Por favor, digite seu DocId para continuarmos o seu pedido"
        msg.body(r)
        responded = True
    if any(char.isdigit() for char in incoming_msg):
        r = "Por favor, digite um banco no qual você seja correntista"
        msg.body(r)
        responded = True
    if incoming_msg in lista_bancos:
        # return a quote
        r = '''Você confirma que façamos uma consulta dos seus dados na instituição acima? se sim, digite confirmar. Com a sua confirmação,você está de acordo com nossos termos e condições, no qual você pode acessar por este link: 

        https://testesmock.s3-sa-east-1.amazonaws.com/TermosECondicoes.pdf
        '''

        msg.body(r)
        responded = True
    if incoming_msg in confirmacoes_texto:
        mandarMensagem("Obrigado, vamos buscar seus dados no banco utilizando a plataforma Teros Open Banking, com essa operação, "
                       + " seu consentimento será verificado com o banco, aguarde um momento.... ", incoming_num)

        grantCode = getGrantCode()['redirect_uri']
        accessToken = getAccessToken(grantCode)['access_token']
        DocId = getPersonalData(accessToken)

        time.sleep(3)
        mandarArquivo('https://terospricing.github.io/OpenBanking/CotacaoChubb.pdf',
                      'CotacaoChubb', incoming_num)
        time.sleep(3)
        mandarMensagem("Verificamos os seus dados, e segue anexo, a nossa melhor cotação, a senha do arquivo são os 3 digitos do seu CPF 2x caso queira pagar com cartão de crédito no nosso ambiente seguro\n"
                       + ",por favor, acesse o link a seguir: https://terospricing.github.io/OpenBanking/CotacaoChubb.html?From=" + incoming_num + "\r\n"
                       + "Agora, caso queira pagar com o CoDi, digite CoDi para que possamos te mandar um QR Code para efetuar o pagamento",
                       incoming_num)

        # msg.body = "Cotacao Chubb"
        # msg.media('https://terospricing.github.io/OpenBanking/CotacaoChubb.pdf')

        time.sleep(150)
        mandarMensagem("Transação confirmada, estamos mandando sua apólice",
                       incoming_num)
        mandarArquivo(
            "https://terospricing.github.io/OpenBanking/ApoliceChubb.pdf", "Apolice", incoming_num)
        responded = True
    if 'codi' in incoming_msg:
        r = "Segue nosso QR Code do CoDi"
        msg.body(r)
        msg.media('https://br.qr-code-generator.com/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png')
        responded = True
    if not responded:
        msg.body('Desculpe, não conseguimos ver sua verificação, este canal é para aquisição de seguros da Chubb, caso queira contratar u')

    '''
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    '''

    return str(resp)


@app.route('/Cotacao', methods=['GET'])
def Cotacao():
    return render_template('Cotacao.html')


@app.route('/Apolice', methods=['POST', 'GET'])
def Apolice():
    From = request.values.get('From', '').lower()
    mandarArquivo(
        "https://terospricing.github.io/OpenBanking/ApoliceChubb.pdf", From)
    return str("Ok")


def mandarMensagem(msg, incoming_num):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client('AC224a8eac78aa418d169119bf73a86cbb',
                    'cafa73d824af8886d511a563c30d3a7f')

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886'

    incoming_num = str(incoming_num).strip()

    if(not "+" in incoming_num):
        incoming_num = "+" + incoming_num
    if(not "whatsapp:" in incoming_num):
        incoming_num = "whatsapp:" + incoming_num

    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = incoming_num

    client.messages.create(body=msg,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)


def mandarArquivo(media, body, incoming_num):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client('AC224a8eac78aa418d169119bf73a86cbb',
                    'cafa73d824af8886d511a563c30d3a7f')

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886'

    incoming_num = str(incoming_num).strip()

    if(not "+" in incoming_num):
        incoming_num = "+" + incoming_num
    if(not "whatsapp:" in incoming_num):
        incoming_num = "whatsapp:" + incoming_num

    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = incoming_num

    client.messages.create(body=body,
                           media_url=media,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)


def getGrantCode():
    try:
        url = "https://api-terosopenbanking.sensedia.com/oauth/v1/grant-code?response_type=code&client_id=6522944b-8a92-369b-bc9e-7e27b9422fc4&redirect_uri=http://supermock.demo.sensedia.com&state=codestate123456"

        payload = {}
        headers = {
            'callback': '0'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text.encode('utf8'))
    except:
        print("getGrantCodeError")
        return ""


def getAccessToken(redirect_uri):
    try:
        url = "https://api-terosopenbanking.sensedia.com/oauth/v1/access-token"

        redirect_uri_code = ""
        redirect_uri_code = redirect_uri.split('=')[2]
        redirect_uri_code = redirect_uri_code.split('&')[0]

        payload = 'grant_type=authorization_code&code=' + redirect_uri_code
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic NjUyMjk0NGItOGE5Mi0zNjliLWJjOWUtN2UyN2I5NDIyZmM0OmZhNTE4ZGM5LWRmZWEtM2ExOS1hOGRkLTFlMGI2NzE1NTE0MA=='
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return json.loads(response.text.encode('utf8'))
    except:
        print("getAccessToken Error")
        return ""


def getPersonalData(AccessToken):
    try:
        url = "https://api-terosopenbanking.sensedia.com/poc/basic-retail/Inquiries/123A"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + AccessToken
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
        return json.loads(response.text.encode('utf8'))
    except:
        print("getPersonalData")
        return ""


if __name__ == '__main__':
    app.run()