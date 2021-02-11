<template>
    <div class="container">
        <main>

            <Title imgUrl="images/CHUBB_Logo_Black_RBG.png" msg1="Confirmação de Compra" msg2="Este é o link para você adiquirir nosso seguro de vida, qualquer dado que esteja
                    incorreto você pode corrigir aqui."></Title>

            <div class="row g-3">
                <Cart cart="Carrinho" periodText="Período" ></Cart>


                
            </div>
          
        </main>

        <footer class="my-5 pt-5 text-muted text-center text-small">
            <p class="mb-1">© 2020 Chubb</p>
            <ul class="list-inline">
                <li class="list-inline-item"><a href="#">Privacidade</a></li>
                <li class="list-inline-item"><a href="#">Termos & Condições</a></li>
                <li class="list-inline-item"><a href="#">Suporte</a></li>
            </ul>
        </footer>
    </div>
</template>

<script>

import Title from './Title'
import Cart from './Cart'

export default {
  name: 'Container',
  components:{
    Title,
    Cart
  }
}
</script>
