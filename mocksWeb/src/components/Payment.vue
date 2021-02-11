<template>
    <div>
    <hr class="my-4">

            <h4 class="mb-3">Payment</h4>

            <div class="my-3">
                <div class="form-check">
                    <input id="credit" name="paymentMethod" type="radio" class="form-check-input credit-card" checked=""
                        required="">
                    <label class="form-check-label" for="credit">Cartão de Crédito</label>
                </div>
                <div class="form-check">
                    <input id="debit" name="paymentMethod" type="radio" class="form-check-input credit-card"
                        required="">
                    <label class="form-check-label" for="debit">Cartão de Débito</label>
                </div>
                <div class="form-check">
                    <input id="paypal" name="paymentMethod" type="radio" class="form-check-input credit-card"
                        required="">
                    <label class="form-check-label" for="paypal">PayPal</label>
                </div>
                <div class="form-check">
                    <input id="CoDi" name="paymentMethod" type="radio" class="form-check-input" required="">
                    <label class="form-check-label" for="CoDi">CoDi</label>
                </div>
                <div class="form-check">
                    <input id="GetAPay" name="paymentMethod" type="radio" class="form-check-input" required="">
                    <label class="form-check-label" for="GetAPay">Get a Pay</label>
                </div>
            </div>

            <div id="CreditCardForm" class="row gy-3">
                <div class="col-md-6">
                    <label for="cc-name" class="form-label">Nome no cartão</label>
                    <input type="text" class="form-control" id="cc-name" placeholder="" required="">
                    <small class="text-muted">Nome completo escrito no cartão</small>
                    <div class="invalid-feedback">
                        Nome no cartão é obrigatório.
                    </div>
                </div>

                <div class="col-md-6">
                    <label for="cc-number" class="form-label">Numero do cartão</label>
                    <input type="text" class="form-control" id="cc-number" placeholder="" required="">
                    <div class="invalid-feedback">
                        Número do cartão é obrigatório.
                    </div>
                </div>

                <div class="col-md-3">
                    <label for="cc-expiration" class="form-label">Data de expiração.</label>
                    <input type="text" class="form-control" id="cc-expiration" placeholder="" required="">
                    <div class="invalid-feedback">
                        Data de expiração é obrigatório.
                    </div>
                </div>

                <div class="col-md-3">
                    <label for="cc-cvv" class="form-label">CVV</label>
                    <input type="text" class="form-control" id="cc-cvv" placeholder="" required="">
                    <div class="invalid-feedback">
                        Código de segurança é obrigatório.
                    </div>
                </div>
                <hr class="my-4">

                <button id="btnFinish" class="btn btn-primary btn-lg btn-block" type="button">Continue para
                    finalizar a
                    compra</button>
            </div>

            <div id="CoDiForm" class="row gy-3" style="display: none">
                <div class="col-md-12">
                    <img src="https://br.qr-code-generator.com/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png"
                        width="400" height="400">
                </div>
            </div>

            <div id="GetAPayForm" style="display: none">
                <div class="col-md-12">
                    <button id="btnGetAPay" class="btn btn-primary btn-lg btn-block" type="button">Get a Pay</button>
                </div>
            </div>
    </div>
</template>

<script>
export default {
    name:'Payment',
    props:{
        
    }
}
</script>
