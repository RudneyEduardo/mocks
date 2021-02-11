<template>
    <div class="py-5 text-center">
        <img class="d-block mx-auto mb-4" src="../images/SegYou.png" alt="" width="300" height="250">
        <h2>{{ msg1 }}</h2>
        <p class="lead">{{ msg2 }}</p>
    </div>
</template>

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