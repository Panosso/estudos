new Vue({
    el: '#challenge',
    data: {
        value: 0
    },
    computed: {
        result(){
            return this.value === 37 ? 'Equal Value' : 'Diference Value'
        }
    },
    watch: {
        value(){
            setTimeout(() => {
                this.value = 0
            }, 5000)
        }
    }
});