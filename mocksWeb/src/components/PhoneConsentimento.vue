<template>
    <body>
    <figure class="iphone">
        <div class="side-buttons">
            <div></div>
        </div>

        <div class="phone">
            <div class="top">
                <div>
                    <span class="camera"></span>
                    <span class="speaker"></span>
                </div>
            </div>

            <div class="screen">
                <img src="../images/apps.png">
                <div id="page-container">


                    <div id="dialog-container">

                        <div v-if="divModalPhone==='on'" id="screen_data_share" class="dialog-box">
                            <div class="background-blur"></div>
                            <div class="header">
                                <div class="background-blur"></div>
                                <div class="contents">
                                    <div class="left">
                                        <i class="fa fa-envelope" aria-hidden="true"></i> App Banco
                                    </div>
                                    <div class="right">
                                        Sun 1:20 pm
                                    </div>
                                </div>
                            </div>
                            <div class="contents main-content">
                                <strong>

                                </strong>
                                Hola, hemos recibido consentimiento para compartir sus datos de registro.
                                Favorito: SEGYOU.
                                Acceda a la aplicación del Banco para
                                autenticar la presentación.

                                <br><br>
                                <span style="text-align: center;"><button id="confirmaConsentimento"
                                       v-on:click="postData()">Confirmar</button></span>
                                <hr>
                                <span style="text-align: center;"><button
                                        id="btn_data_share_cancel">Rechazar</button></span>
                            </div>
                        </div>
                        <div id="screen_credit_confirm" class="dialog-box" style="display: none">
                            <div class="background-blur"></div>
                            <div class="header">
                                <div class="background-blur"></div>
                                <div class="contents">
                                    <div class="left">
                                        <i class="fa fa-envelope" aria-hidden="true"></i> App Banco
                                    </div>
                                    <div class="right">
                                        <!-- Sun 1:20 pm -->
                                    </div>
                                </div>
                            </div>
                            <div class="contents main-content">
                                <!-- <strong>
                    00
                  </strong> -->
                                <br />
                                <p><br></p>
                                <br>
                                <span style="text-align: center;"><button
                                        id="btn_credit_confirm_ok_chubb">Confirmar</button></span>
                                <hr>
                                <span style="text-align: center;"><button
                                        id="btn_credit_confirm_cancel">Rechazar</button></span>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </figure>
</body>
</template>



<script>
import axios from 'axios'


export default {
    name:'PhoneConsentimento',
    data(){
        return{ 
            divModalPhone: 'on'
        }
    },
    methods:{
        postData(){
            axios.post('http://127.0.0.1:5000/es/bot', {
            confirmar: "confirmar"
        });
        this.divModalPhone = 'off'
        }
    }
}

</script>