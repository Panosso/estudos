new Vue({
	el: '#challenge',
	data: {
		applySpotlight: true,
		applyShorter: false,
		class1: 'class1',
		class2: 'class2',
		class4: '',
		color: 'red',
		color1: 'green',
		danger: '',
		message: "Now i have a CSS class :)"
	},
	methods: {
		changeClass() {
			setInterval(() => {
				this.applySpotlight = !this.applySpotlight
				this.applyShorter = !this.applyShorter
			}, 5000)
		},
		iniciarProgresso() {
			let valor = 0
			const temporizador = setInterval(() => {
				valor += 5
				this.width = `${valor}%`
				if(valor == 100) clearInterval(temporizador)
			}, 500)
		},
		startEfect() {
			this.changeClass()
		},
		setDanger(event) {
			console.log("Iniciei o evento: ", event)
			if(event.target.value == "true"){
				this.danger = true
			} else if(event.target.value == "false"){
				this.danger = false
			}
		}
	},
	computed: {
		myStyle(){
			return{
				backgroundColor: this.color,
				width: 100 + 'px',
				height: 100 + 'px'
			}
		}
	}
})
