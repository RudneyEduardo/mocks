<template>
    <div style="display: block;
                margin-left: auto;
                margin-right: auto;
                height: 50%;
  width: 50%;" class="py-5 text-center">
        <img class="d-block mx-auto mb-4" src="../images/SegYou.png" alt="" width="300" height="250">
        <h2>{{ msg1 }}</h2>
        <p class="lead">{{ msg2 }}</p>
    </div>
</template>

<style scoped>
    .container img {
        max-height: 100%;
        max-width: 100%;
    }
</style>


<script>
    export default {
        name: 'Title',
        props: {
            imgUrl: String,
            msg1: String,
            msg2: String
        }
    }
</script>