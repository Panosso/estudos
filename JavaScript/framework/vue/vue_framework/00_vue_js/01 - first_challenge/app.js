new Vue({
    el: "#challenge",
    data: {
        name: "Pedro Panosso Machado",
        age: 29,
        image: 'data:image/jpeg;base64,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'
    },
    methods: {
        print_name_age: function(){
            return "Hi my name is " + this.name + " and i have " + this.age + " years"
        },
        random_number: function(){
            return Math.random()
        }
    }

})