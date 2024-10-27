new Vue({
    el: '#challenge',
    data: {
        value: ''
    },
    methods: {
        show_alert: function(){
            alert("You click on me, how dare you?")
        },
        store_keydown_value: function(event){
            this.value = event.target.value
        }
    }
})