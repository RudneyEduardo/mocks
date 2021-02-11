from flask import Flask, Blueprint, request, render_template
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
import time
from twilio.rest import Client

app_es = Blueprint('app_es', __name__)

personalData = {
    "docId": "123"
}


@app_es.route("/es/")
def hello_world():
    return "<p>Hello, World!</p>"


@app_es.route('/es/bot', methods=['POST'])
def bot():
    lista_bancos = ["itau", "bradesco", "citibanamex", "banorte", "santander",
                    "banco do brasil", "caixa", "BB", "Nubank", "BTG", "banese"]
    confirmacoes_texto = ["confirmar", "confirma", "si"]

    incoming_msg = request.values.get('Body', '').lower()
    incoming_num = request.values.get('From', '').lower()

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
        r = '''De acuerdo con la Ley de Datos, sigue el enlace para acceder a nuestra Política de Privacidad: https://testesmock.s3-sa-east-1.amazonaws.com/TermosECondicoes.pdf. ¿Confirma la consulta de datos en su banco? Si es así, escriba "confirmar".'''
        msg.body(r)
        responded = True
    if incoming_msg in confirmacoes_texto:
        mandarMensagem(
            "Gracias. Usted recibirá un mensaje de su banco, confirme su consentimiento para el envio de sus datos cadastrales.", incoming_num)

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

        time.sleep(3)
        mandarArquivo('https://terospricing.github.io/OpenBanking/CotizacionSegyou.pdf',
                      'CotizacionSegyou', incoming_num)
        time.sleep(3)
        mandarMensagem("Enviamos una cotización sugerida en este archivo (para abrirlo, escriba su DocId dos veces). Para pagar e adquirir el seguro en estas condiciones, ingrese Codi para recibir un QRCode de pago instantáneo.", incoming_num)
        mandarMensagem("Si desea utilizar otro medio de pago o modificar la cotización sugerida, acceda al ambiente seguro SegYou - Anytime Safe, en el enlace: " + "https://terospricing.github.io/OpenBanking/CotacaoSegyou.html?From=" + incoming_num + "\r\n",
                       incoming_num)

        time.sleep(150)
        mandarMensagem("Transacción confirmada, te enviamos tu póliza",
                       incoming_num)
        mandarArquivo(
            "https://terospricing.github.io/OpenBanking/PolizaSegyou.pdf", "PolizaSegyou", incoming_num)

        responded = True
    if 'codi' in incoming_msg:
        # grantCode = getGrantCode()['redirect_uri']
        # if(grantCode != None):
        #     print("Grant Code Successful")
        # accessToken = getAccessToken(grantCode)['access_token']
        # if(grantCode != None):
        #     print("Grant Code Successful")
        # postProposal(accessToken)
        try:
            postPayments()
        except:
            print("Sensedia error")

        r = "Sigue nuestro QR Code de CoDi"
        msg.body(r)
        msg.media('https://br.qr-code-generator.com/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png')
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


@app_es.route('/es/Cotacao', methods=['GET'])
def Cotacao():
    return render_template('Cotacao.html')


@app_es.route('/es/Apolice', methods=['POST', 'GET'])
def Apolice():
    From = request.values.get('From', '').lower()
    mandarArquivo(
        "https://terospricing.github.io/OpenBanking/PolizaSegyou.pdf", From)
    return str("Ok")


def mandarMensagem(msg, incoming_num):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client('ACcbbaf828ffce32173b9b53f6fd7aaf12',
                    '156f49ecefa9c71630f2ecbba4832a31')

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = incoming_num

    client.messages.create(body=msg,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)


def mandarArquivo(media, body, incoming_num):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client('ACcbbaf828ffce32173b9b53f6fd7aaf12',
                    '156f49ecefa9c71630f2ecbba4832a31')

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = incoming_num

    client.messages.create(body=body,
                           media_url=media,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)


def getGrantCode():
    print("getGrantCode inititate")
    try:
        url = "https://api-terosopenbanking.sensedia.com/oauth/v1/grant-code?response_type=code&client_id=6522944b-8a92-369b-bc9e-7e27b9422fc4&redirect_uri=http://supermock.demo.sensedia.com&state=codestate123456"

        payload = {}
        headers = {
            'callback': '0'
        }

        response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
        print(response.text.encode('utf8'))
        return json.loads(response.text.encode('utf8'))
    except:
        print("getGrantCode error")
        return None


def getAccessToken(redirect_uri):
    print("getAccessToken inititate")
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
        response = requests.request("POST", url, headers=headers, data=payload, timeout=5)
        print(response.text.encode('utf8'))
        return json.loads(response.text.encode('utf8'))
    except:
        print("getAccessToken error")
        return None


def getPersonalData(AccessToken, documento):
    print("getPersonalData inititate")
    try:
        if(documento == ""):
            documento = "123"
        url = "https://api-terosopenbanking.sensedia.com/poc/basic-retail/Inquiries/" + documento
        print(url)
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + AccessToken
        }

        response = requests.request("GET", url, headers=headers, data=payload, timeout=5)
        print(response.text.encode('utf8'))
        return json.loads(response.text.encode('utf8'))
    except:
        print("getPersonalData error")
        return None

def postProposal(AccessToken):
    try:
        url = "https://api-terosopenbanking.sensedia.com/poc/basic-retail/proposals/9394C8BD-248A-4361-B324-D55F7C2E7461"

        payload = "{\r\n  \"tax\": 8,\r\n  \"amount\": 100.00,\r\n  \"amountTax\": 108.00,\r\n  \"comments\": \"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin a risus vitae ex convallis ullamcorper non in felis. Suspendisse malesuada dictum nunc, ac porta sapien sagittis ut. Maecenas eu luctus ante, a varius eros.\"\r\n}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + AccessToken
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text.encode('utf8'))
        return "OK"
    except:
        print("postProposal Error")
        return "Error"


def postPayments():
    print("postPayments inititate")
    try:
        url = "https://api-terosopenbanking.sensedia.com/payments/v1/payments"

        payload = {}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload,timeout=5)

        print(response.text.encode('utf8'))
    except:
        print("postPayments Error")
        return "Error"
