<template>
    <div class="container">
        <main>
            <Title imgUrl="../images/SegYou.png"></Title>

            <div class="row g-3">
                <div class="col-md-5 col-lg-4 order-md-last" id="valueDiv">
                    <h4 class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-muted">Su carrito</span>
                        <span class="badge bg-secondary rounded-pill">1</span>
                    </h4>
                    <ul class="list-group mb-3">
                        <li class="list-group-item d-flex justify-content-between lh-sm">
                            <div>
                                <h6 class="my-0">Seguro de vida estándar</h6>
                                <!-- <small class="text-muted">Nuestro producto de seguro de vida estándar </small> -->
                            </div>
                            <span id="lblValor" class="text-muted">Prima: ${{ primaVal }} /ano</span>
                            <span id="lblPremio" class="text-muted">Cobertura del seguro: ${{ coberturaVal }}</span>
                        </li>
                        <!-- <li class="list-group-item d-flex justify-content-between lh-sm">
                            <div>
                                <h6 class="my-0">Seguro de accidentes personales</h6>
                                 <small class="text-muted">Agregar accidentes personales a su seguro de vida</small>
                            </div>
                            <span class="text-muted">Prima: $792 /ano</span>
                            <span class="text-muted">Cobertura del seguro: $36000 /ano</span>
                        </li> -->
                        <li class="list-group-item d-flex justify-content-between bg-light">
                            <div class="text-success">
                                <h6 class="my-0">Período</h6>
                                <small>Nº de meses</small>
                            </div>
                            <span class="text-success">12</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Parcela </span>
                            <strong id="lblTotal">${{ mensalVal }} /mes</strong>
                        </li>
                    </ul>

                    <!-- <form class="card p-2">
                        <div class="input-group">
                            <input type="text" class="form-control" placeholder="Promo code">
                            <button type="submit" class="btn btn-secondary">Aplicar</button>
                        </div>
                    </form> -->
                </div>
                <div class="col-md-7 col-lg-8">

                    <hr class="my-4">
                    <form class="">
                        <div class="row g-3">
                            <div class="col-sm-6">
                                <label for="firstName" class="form-label">Cobertura del Seguro</label>
                                <input id="txtValorDoPremio" type="text" class="form-control" :placeholder="value"
                                    v-on:input="changeValueReactive($event)" required="">


                            </div>
                        </div>
                    </form>
                    <hr class="my-4">

                    <h4 class="mb-3">Dirección de Envio</h4>
                    <form class="needs-validation" novalidate="">
                        <div class="row g-3">
                            <div class="col-sm-6">
                                <label for="firstName" class="form-label">Nombre</label>
                                <input type="text" class="form-control" id="firstName" placeholder="" value="Ramon"
                                    required="">
                                <div class="invalid-feedback">
                                    Digite um nome válido.
                                </div>
                            </div>

                            <div class="col-sm-6">
                                <label for="lastName" class="form-label">Apellido</label>
                                <input type="text" class="form-control" id="lastName" placeholder="" value="Valdés"
                                    required="">
                                <div class="invalid-feedback">
                                    Digite um sobrenome válido.
                                </div>
                            </div>

                            <div class="col-12">
                                <label for="username" class="form-label">Nombre de usuário</label>
                                <div class="input-group">
                                    <span class="input-group-text">@</span>
                                    <input type="text" class="form-control" id="username" placeholder="Username"
                                        required="">
                                    <div class="invalid-feedback">
                                        Digite um nome de usuário válido.
                                    </div>
                                </div>
                            </div>

                            <div class="col-6">
                                <label for="email" class="form-label">E-mail <span
                                        class="text-muted">(Opcional)</span></label>
                                <input type="email" class="form-control" id="email" placeholder="you@example.com"
                                    value="ramonv@gmail.com">
                                <div class="invalid-feedback">
                                    Por favor entre com um endereço de e-mail para receber atualizações do seu seguro.
                                </div>
                            </div>

                            <div class="col-6">
                                <label for="borndate" class="form-label">Fecha de nacimiento</label>
                                <input type="borndate" class="form-control" id="borndate" value="02/09/1923">
                                <div class="invalid-feedback">
                                    Por favor entre com uma data de nascimento valida
                                </div>
                            </div>

                            <div class="col-4">
                                <label for="borndate" class="form-label">DocId </label>
                                <input type="borndate" class="form-control" id="DocId" value="123">
                                <div class="invalid-feedback">
                                    Por favor entre com um DocId valido
                                </div>
                            </div>

                            <div class="col-4">
                                <label for="borndate" class="form-label">Género</label>
                                <select class="form-select" id="state" required="">
                                    <option value="">Opciones...</option>
                                    <option selected>Masculino</option>
                                    <option>Feminino</option>
                                </select>
                            </div>

                            <div class="col-4">
                                <label for="borndate" class="form-label">Estado Civil</label>
                                <select class="form-select" id="state" required="">
                                    <option value="">Opciones...</option>
                                    <option selected>No casado</option>
                                    <option>Casado</option>
                                </select>
                            </div>

                            <div class="col-12">
                                <label for="address" class="form-label">Dirección de casa</label>
                                <input type="text" class="form-control" id="address" value="Av. Paulista, 2000"
                                    required="">
                                <div class="invalid-feedback">
                                    Digite um endereço válido.
                                </div>
                            </div>

                            <div class="col-12">
                                <label for="address2" class="form-label">Dirección de negocios <span
                                        class="text-muted">(Opcional)</span></label>
                                <input type="text" class="form-control" id="address2" value="Av. Maria Otilia, 4580">
                            </div>

                            <div class="col-md-5">
                                <label for="country" class="form-label">País</label>
                                <select class="form-select" id="country" required="">
                                    <option value="">Opciones...</option>
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
                                    <option value="">Opciones...</option>
                                    <option selected>São Paulo</option>
                                </select>
                                <div class="invalid-feedback">
                                    Escolha um estado válido.
                                </div>
                            </div>

                            <div class="col-md-3">
                                <label for="zip" class="form-label">Código postal</label>
                                <input type="text" class="form-control" id="zip" placeholder="" required=""
                                    value="03351090">
                                <div class="invalid-feedback">
                                    Digite um CEP válido.
                                </div>
                            </div>
                        </div>

                        <hr class="my-4">
                        <div class="form-check">
                            <input type="checkbox" class="form-check-input" id="save-info">
                            <label class="form-check-label" for="save-info">Guarde esta información para su próxima
                                compra</label>
                        </div>

                        <hr class="my-4">

                        <h4 class="mb-3">Opciones de Pago</h4>

                        <div class="my-3">
                            <div class="form-check">
                                <input value="Card" v-model="paymentMethod" type="radio"
                                    class="form-check-input credit-card" checked="" required="">
                                <label class="form-check-label">Tarjeta de Crédito (Credit Card)</label>
                            </div>
                            <div class="form-check">
                                <input value="CoDi" v-model="paymentMethod" type="radio" class="form-check-input"
                                    required="">
                                <label class="form-check-label">CoDi</label>
                            </div>
                            <div class="form-check">
                                <input value="GetAPay" v-model="paymentMethod" type="radio" class="form-check-input"
                                    required="">
                                <label class="form-check-label">Get a Pay</label>
                            </div>
                        </div>

                        <div v-if="paymentMethod === 'Card'" class="row gy-3">
                            <div class="col-md-6">
                                <label class="form-label">Nombre de la tarjeta</label>
                                <input type="text" class="form-control" placeholder="" required="">
                                <!-- <small class="text-muted">Nombre na tarjeta</small> -->
                                <div class="invalid-feedback">
                                    Nome no cartão é obrigatório.
                                </div>
                            </div>

                            <div class="col-md-6">
                                <label class="form-label">Numero de la tarjeta</label>
                                <input type="text" class="form-control" placeholder="" required="">
                                <div class="invalid-feedback">
                                    Número do cartão é obrigatório.
                                </div>
                            </div>

                            <div class="col-md-3">
                                <label class="form-label">Expiración</label>
                                <input type="text" class="form-control" placeholder="" required="">
                                <div class="invalid-feedback">
                                    Data de expiração é obrigatório.
                                </div>
                            </div>

                            <div class="col-md-3">
                                <label class="form-label">CVV</label>
                                <input type="text" class="form-control" placeholder="" required="">
                                <div class="invalid-feedback">
                                    Código de segurança é obrigatório.
                                </div>
                            </div>
                            <hr class="my-4">

                            <button class="btn btn-primary btn-lg btn-block" type="button">Terminar la
                                compra</button>
                        </div>

                        <div v-if="paymentMethod === 'CoDi'" class="row gy-3">
                            <div class="col-md-12">
                                <img src="https://br.qr-code-generator.com/wp-content/themes/qr/new_structure/markets/core_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png"
                                    width="400" height="400">
                            </div>
                        </div>

                        <div v-if="paymentMethod === 'GetAPay'">
                            <div class="col-md-12">
                                <router-link :to="{ name: 'Home'}" target="_blank">
                                    <a id="btnGetAPay" class="btn btn-primary btn-lg btn-block">Get a
                                        Pay</a>
                                </router-link>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

        </main>

        <footer class="my-5 pt-5 text-muted text-center text-small">
            <p class="mb-1">© 2020 SegYou</p>
            <ul class="list-inline">
                <li class="list-inline-item"><a href="#">Privacidad</a></li>
                <li class="list-inline-item"><a href="#">Términos & Condiciones</a></li>
                <li class="list-inline-item"><a href="#">Soporte</a></li>
            </ul>
        </footer>

    </div>


</template>



<script>
    import Title from './Title'





    export default {
        name: 'Container',
        components: {
            Title,

        },
        data() {
            return {
                value: 10000,
                coberturaVal: 10000,
                primaVal: 220,
                mensalVal: 18,
                paymentMethod: 'Card'
            }
        },

        methods: {
            changeValueReactive(event) {
                this.coberturaVal = event.target.value
                this.primaVal = Math.round(this.coberturaVal * 0.022)
                this.mensalVal = Math.round(this.primaVal / 12)
            }
        }

    }
</script>