<template>

    <div class="col-md-7 col-lg-8">

        <hr class="my-4">
        <form class="">
            <div class="row g-3">
                <div class="col-sm-6">
                    <label for="firstName" class="form-label">Valor do Prêmio</label>
                    <input id="txtValorDoPremio" type="text" class="form-control" placeholder="" value="100000"
                        required="">
                </div>
            </div>
        </form>
        <hr class="my-4">

        <h4 class="mb-3">Endereço de cobrança</h4>
        <form class="needs-validation" novalidate="">
            <div class="row g-3">
                <div class="col-sm-6">
                    <label for="firstName" class="form-label">Nome</label>
                    <input type="text" class="form-control" id="firstName" placeholder="" value="Ramon" required="">
                    <div class="invalid-feedback">
                        Digite um nome válido.
                    </div>
                </div>

                <div class="col-sm-6">
                    <label for="lastName" class="form-label">Sobrenome</label>
                    <input type="text" class="form-control" id="lastName" placeholder="" value="Valdés" required="">
                    <div class="invalid-feedback">
                        Digite um sobrenome válido.
                    </div>
                </div>

                <div class="col-12">
                    <label for="username" class="form-label">Nome de usuário</label>
                    <div class="input-group">
                        <span class="input-group-text">@</span>
                        <input type="text" class="form-control" id="username" placeholder="Username" required="">
                        <div class="invalid-feedback">
                            Digite um nome de usuário válido.
                        </div>
                    </div>
                </div>

                <div class="col-6">
                    <label for="email" class="form-label">E-mail <span class="text-muted">(Optional)</span></label>
                    <input type="email" class="form-control" id="email" placeholder="you@example.com"
                        value="ramonv@gmail.com">
                    <div class="invalid-feedback">
                        Por favor entre com um endereço de e-mail para receber atualizações do seu seguro.
                    </div>
                </div>

                <div class="col-6">
                    <label for="borndate" class="form-label">Born date </label>
                    <input type="borndate" class="form-control" id="borndate" value="02/09/1923">
                    <div class="invalid-feedback">
                        Por favor entre com uma data de nascimento valida
                    </div>
                </div>

                <div class="col-4">
                    <label for="borndate" class="form-label">DocId </label>
                    <input type="borndate" class="form-control" id="DocId" value="123A">
                    <div class="invalid-feedback">
                        Por favor entre com um DocId valido
                    </div>
                </div>

                <div class="col-4">
                    <label for="borndate" class="form-label">Genero</label>
                    <select class="form-select" id="state" required="">
                        <option value="">Escolha...</option>
                        <option selected>Masculino</option>
                        <option>Feminino</option>
                    </select>
                </div>

                <div class="col-4">
                    <label for="borndate" class="form-label">Estado Civil</label>
                    <select class="form-select" id="state" required="">
                        <option value="">Escolha...</option>
                        <option selected>Solteiro</option>
                        <option>Casado</option>
                    </select>
                </div>

                <div class="col-12">
                    <label for="address" class="form-label">Endereço</label>
                    <input type="text" class="form-control" id="address" value="Av. Paulista, 2000" required="">
                    <div class="invalid-feedback">
                        Digite um endereço válido.
                    </div>
                </div>

                <div class="col-12">
                    <label for="address2" class="form-label">Endereço comercial <span
                            class="text-muted">(Optional)</span></label>
                    <input type="text" class="form-control" id="address2" value="Av. Maria Otilia, 4580">
                </div>

                <div class="col-md-5">
                    <label for="country" class="form-label">País</label>
                    <select class="form-select" id="country" required="">
                        <option value="">Escolha...</option>
                        <option>México</option>
                        <option selected>Brasil</option>
                        <option>United States</option>
                    </select>
                    <div class="invalid-feedback">
                        Escolha um país válido.
                    </div>
                </div>

                <div class="col-md-4">
                    <label for="state" class="form-label">Estado</label>
                    <select class="form-select" id="state" required="">
                        <option value="">Escolha...</option>
                        <option selected>São Paulo</option>
                    </select>
                    <div class="invalid-feedback">
                        Escolha um estado válido.
                    </div>
                </div>

                <div class="col-md-3">
                    <label for="zip" class="form-label">CEP</label>
                    <input type="text" class="form-control" id="zip" placeholder="" required="" value="03351090">
                    <div class="invalid-feedback">
                        Digite um CEP válido.
                    </div>
                </div>
            </div>

            <hr class="my-4">
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="save-info">
                <label class="form-check-label" for="save-info">Salvar essas informações para próxima
                    compra</label>
            </div>

            <Payment></Payment>
        </form>
    </div>
</template>


<script>
    export default {
        name: 'Form',

    }
</script>