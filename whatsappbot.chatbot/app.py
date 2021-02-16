from flask import Flask, request, render_template
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
import time
from twilio.rest import Client
from flask_cors import CORS, cross_origin
import config

print(config.data['QRCode'])

app = Flask(__name__)
#cors = CORS(app, resources={r"/": {"origins": ""}})
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
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

@app.route('/bot/es', methods=['POST'])
def botEs():
    try:
        data = request.json
        print(data['Body'])
        print('------')
        print(data['From'])
    except:
        pass

    lista_bancos = ["itau", "bradesco", "citibanamex", "banorte", "santander",
                    "banco do brasil", "caixa", "BB", "Nubank", "BTG", "banese"]
    confirmacoes_texto = ["confirmar", "confirma", "si"]

    incoming_msg = request.values.get('Body', '').lower()
    if not incoming_msg:
        incoming_msg = data['Body']
    incoming_num = request.values.get('From', '').lower()
    if not incoming_num:
        incoming_num = data['From']

    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if (any(char.isdigit() for char in incoming_msg) and len(incoming_msg) == 1) or incoming_msg in lista_bancos:
        # return a quote
        r = "Por favor, ingrese su DocId."
        msg.body(r)
        responded = True
    if (any(char.isdigit() for char in incoming_msg) and len(incoming_msg) > 1) or incoming_msg in lista_bancos:
        # return a quote
        global personalData
        personalData = {"docId": incoming_msg}
        r = '''De acuerdo con la Ley de Datos, sigue el enlace para ver los términos de consentimiento para esta consulta de datos: ''' + config.data['TermosECondicoes']+'''
¿Confirma el consentimiento para la consulta de datos en su banco? Si es así, escriba "confirmar".'''
        
        msg.body(r)
        responded = True
    if incoming_msg in confirmacoes_texto:
        mandarMensagem(
            "Gracias. Usted recibirá un mensaje de su banco, confirme su consentimiento para el envio de sus datos cadastrales.", incoming_num)
        responded = True
    # Se o usuário clicar em confirmar consentimento no celular
    elif incoming_msg == 'confirmarConsentimento':
        try:
            grantCode = getGrantCode()['redirect_uri']
            if(grantCode != None):
                print("Grant Code Successful")
            accessToken = getAccessToken(grantCode)['access_token']
            if(accessToken != None):
                print("access_token")

            print(personalData)
            getPersonalData(accessToken, personalData["docId"])
        except:
            print("Sensedia error")

        mandarArquivo(config.data['CotacionSegYou'],
                    'CotizacionSegyou', incoming_num)
        
        time.sleep(1)
        mandarMensagem("Enviamos una cotización sugerida en este archivo (para abrirlo, escriba su DocId dos veces). Para pagar e adquirir el seguro en estas condiciones, ingrese Codi para recibir un QRCode de pago instantáneo.", incoming_num)
        mandarMensagem("Si desea utilizar otro medio de pago o modificar la cotización sugerida, acceda al ambiente seguro SegYou - Anytime Safe, en el enlace: " + config.data['AmbienteSegYou'],
                    incoming_num)
        responded = True
    # Se o usuário clilcar em confirmar pagamento no celular
    if incoming_msg == 'confirmarPagamento':
        mandarMensagem("Transacción confirmada, te enviamos tu póliza",
                    incoming_num)
        mandarArquivo(
            config.data['PolizaSegYou'], "PolizaSegyou", incoming_num)

        responded = True




    if 'codi' in incoming_msg:
        try:
            postPayments()
        except:
            print("Sensedia error")

        r = "Sigue nuestro QR Code de CoDi"
        msg.body(r)
        msg.media(config.data['QRCode'])
        responded = True
    if not responded:
        mandarMensagem(
            'Hola, bienvenido al canal de cotización y venta de seguros de vida SegYou - Anytime Safe.', incoming_num)
        msg.body('''Para garantizar su facilidad y seguridad de la información, obtenemos los datos para la cotización a través de su registro bancario. Por lo tanto, ingrese el número correspondiente al banco en el que tiene una cuenta: 
        * 1 * - CitiBanamex; 
        * 2 * - Banorte; 
        * 3 * - Santander; 
        * 4 * - BBVA; 
        * 5 * - HSBC; ''')

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
    client = Client(config.data['account_sid'],
                    config.data['auth_token'])

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
    client = Client(config.data['account_sid'],
                    config.data['auth_token'])

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
    app.run(debug=True)
