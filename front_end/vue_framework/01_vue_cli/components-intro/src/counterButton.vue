<template>
    <div id="app" class="counter">
        <h2> {{ counter }} </h2>
        <button @click="addValue">ADD</button>
        <button @click="subValue">SUB</button>
        <button>?</button>
    </div>
</template>

<script>
export default {

    data() {
        return{
            counter: 0
        }
    },
    methods: {
        addValue() {
            return this.counter++
        },
        subValue() {
            return this.counter--
        }        
    }

}
</script>

<!-- When the style has scoped, will grant that style will work only in created components-->
<style scoped>

    span{
        border-bottom: 1px solid white;
        height: 30px;
        padding: 5px 25px;
    }

    button{
        height: 40px;
        width: 40px;
        border-radius: 15px;
        background-color: coral;
        color: #fff;
        margin-left: 10px;
        outline: none;
    }

</style>