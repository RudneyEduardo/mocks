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
                                    Segyou solicita una autorizacíon de compra de: $367,00/mes con recurrencia mensual por un período de 12 meses

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

<style scoped>
   @import "../styles/iphone.css";
   @import "../styles/index.css";
   @import "../styles/notification.css";
   @import "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";

</style>


<script>
    import axios from 'axios'


    export default {
        name: 'PhoneConsentimento',
        data() {
            return {
                divModalPhone: 'on'
            }
        },
        methods: {
            postData() {
                var fromParam = this.$route.params.From


                axios.post('http://13.58.21.71:5050/bot/es', {
                    Body: "confirmarPagamento",
                    From: fromParam
                });
                this.divModalPhone = 'off'
            }


        }
    }
</script>