<template>

    <div class="col-md-5 col-lg-4 order-md-last">
        <h4 class="d-flex justify-content-between align-items-center mb-3">
            <span class="text-muted">{{ cart }}</span>
            <span class="badge bg-secondary rounded-pill">3</span>
        </h4>
        <ul class="list-group mb-3">
            <li class="list-group-item d-flex justify-content-between lh-sm">
                <div>
                    <h6 class="my-0">{{ product }}</h6>
                    <small class="text-muted">{{ description }} </small>
                </div>
                <span id="lblValor" class="text-muted">{{valueString}}: {{valueType}}{{valueNum}}</span>
                <span id="lblPremio" class="text-muted">{{ prizeString }}: {{ prizeType }}{{ prizeNum }}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between lh-sm">
                <div>
                    <h6 class="my-0">{{ typeString }}</h6>
                    <small class="text-muted">{{ typeDescription }}</small>
                </div>
                <span class="text-muted">{{ price1String }}: {{ price1Type }}{{ price1Num }} / {{ price1Year }}</span>
                <span class="text-muted">{{ price2String }}: {{ price2Type }}{{ price2Num }} / {{ price2Year }}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between bg-light">
                <div class="text-success">
                    <h6 class="my-0">{{ periodText }}</h6>
                    <small>{{ periodByTime }}</small>
                </div>
                <span class="text-success">{{ periodValue }}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between">
                <span>{{ total }}</span>
                <strong id="lblTotal">{{ totalPriceType }}{{ totalPriceNum }}</strong>
            </li>
        </ul>
    </div>

</template>


<script>
    export default {
        name: 'Title',
        props: {
            cart: String,
            num: Int8Array,
            product: String,
            description: String,
            valueString: String,
            valueType: String,
            valueNum: Float64Array,
            prizeString: String,
            prizeType: String,
            prizeNum: Float64Array,
            typeString : String,
            typeDescription: String,
            price1String: String,
            price1Type: String,
            price1Num: Float64Array,
            price1Year: String,
            price2String: String,
            price2Type: String,
            price2Num: Float64Array,
            price2Year: String,
            periodText: String,
            periodByTime: String,
            periodValue: String,
            total: String,
            totalPriceType: String,
            totalPriceNum: Float64Array
        }
    }
</script>