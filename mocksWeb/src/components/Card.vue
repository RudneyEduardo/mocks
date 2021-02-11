<template>
    <div id="CreditCardForm" class="row gy-3">
        <div class="col-md-6">
            <label for="cc-name" class="form-label">Nombre de la tarjeta</label>
            <input type="text" class="form-control" id="cc-name" placeholder="" required="">
            <!-- <small class="text-muted">Nombre na tarjeta</small> -->
            <div class="invalid-feedback">
                Nome no cartão é obrigatório.
            </div>
        </div>

        <div class="col-md-6">
            <label for="cc-number" class="form-label">Numero de la tarjeta</label>
            <input type="text" class="form-control" id="cc-number" placeholder="" required="">
            <div class="invalid-feedback">
                Número do cartão é obrigatório.
            </div>
        </div>

        <div class="col-md-3">
            <label for="cc-expiration" class="form-label">Expiración</label>
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

        <button id="btnFinish" class="btn btn-primary btn-lg btn-block" type="button">Terminar la
            compra</button>
    </div>
</template>

<script>
export default {
    name:"Card",
    props:{
        
    }
}
</script>