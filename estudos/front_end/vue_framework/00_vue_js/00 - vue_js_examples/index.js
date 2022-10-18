const datas = {counterApp27: 0}

//Create a global new DOM component
Vue.component('todo-item-component', {
	props: ['id', 'custom_attr'],
	template: '<li v-on:click="showName()">{{ custom_attr.text }}</li>',
	methods: {
		showName: function(){
			alert(this.custom_attr.id +' '+ this.custom_attr.text)
		}
	}
})
  
Vue.component('another-example', {
	template: '<p>This is a Vue Component: {{ 1 + Math.random() }}</p>'
})

Vue.component('countercomponent',{
		template: `
			<div>
				<span>{{ counterApp26 }}</span>
				<button @click="counterApp26++"> ADD </button>
				<button @click="counterApp26--"> SUB </button>
			</div>
			`,
		data() {
			return {
				counterApp26: 0
			}
		}
	}
)

//It's possible usa a variable as data
Vue.component('countercomponent2',
{		template: `
		<div>
			<span>{{ counterApp27 }}</span>
			<button @click="counterApp27++"> ADD </button>
			<button @click="counterApp27--"> SUB </button>
		</div>
		`,
		data() {
			return datas
		}
	}
)

//Will execute when the page is loaded
new Vue({
	data: {
	  a: 1
	},
	created: function () {
	  // `this` points to the vm instance
	  console.log('a is: ' + this.a)
	}
  })
  
  
  var data = {a : 1}
  
  var vm = new Vue({
	  
	  data: data
	  
	  })
	  
  var freeze_obj = {foo: 'bar'}
  
  Object.freeze(freeze_obj)
  
  var vm2 = new Vue({
	  el: "#app10",
	  data: freeze_obj
	  })
  
  new Vue({
	  data: {a:1},
	  created: function(){console.log('A is: '+ this.a)}
	  })
  

var app = new Vue({
	el: "#app",
	data: {
		message: 'Hello World and Vue, now the mark of the curse is gone.'
	}
});

var app2 = new Vue({
	el: '#app2',
	data: {
		message: 'You loaded this page in: ' + new Date().toLocaleString()
		}
});

var app3 = new Vue({
	el: '#app3',
	data: {
		tavendo: true
		}
	});

var app4 = new Vue({
	el: '#app4',
	data: {
			list_itens: [
				{text: 'Vue'},
				{text: 'Django'},
				{text: 'Python'}
				],
			products: [
				{product_title: 'shirt'},
				{product_title: 'sock'},
				{product_title: 'havaina'}
			]
		}

});

var app5 = new Vue({
	el: '#app5',
	data: {
			gona_invert: 'Hello world'
		},
	methods: {
			reverseMessage: function() {
					this.gona_invert = this.gona_invert.split('').reverse('').join('')
				}
		}
	});

var app6 = new Vue({
	el: '#app6',
	data: {
			input_message: 'Hellow Vue'
		}
	});

var app7 = new Vue({
	el: '#app7',
	data: {
		    groceryList: [
			  { id: 0, text: 'Vegetables' },
			  { id: 1, text: 'Cheese' },
			  { id: 2, text: 'Whatever else humans are supposed to eat' }
			]
		}
	})
	
var app8 = new Vue({
	
	el: "#app8",
	data: {mesga: "This is a message"}
	
	})

var app9 = new Vue({
	el: "#app9",
	data: {rawHtml: "<span style='color:red;'>This should be red</span>"}
	})


var app11 = new Vue({
	el: "#app11",
	data: {
		visibleList: true,
		items: [
			{id: 1, name: "item 1"},
			{id: 2, name: "item 2"},
			{id: 3, name: "item 3"}
		]

	}

})

var app12 = new Vue({

	el: "#app12",
	data: {
		isVisible: true,
		message: "Hello Vue!!!"
	},
	methods: {
		toogleMessage: function(){
			this.isVisible = !this.isVisible
		}
	}
})

var data = {numero: 1}

var app13 = new Vue({
	el: "#app13",
	data: data

})

var app14 = new Vue({
	el: '#app14',
	data: {
		title: "French fries 1 2 3",
		link_ref: "http://www.google.com.br"
	},
	methods: {
		hello_stranger: function(){
			return "This is a VUE JS course, Good Week and eat " + this.title + "!!!"
		}
	}
})

new Vue({
	el: '#app15',
	data: {
		title: "App15 Title"
	},
	methods: {
		change_title: function() {
			this.title = "New Title"
			return this.title
		}
	}

})

new Vue({
	el: '#app16',
	data: {
		link_ref_html: '<a href="http://www.google.com.br">Google</a>'
	}
})

new Vue({
	el: '#app17',
	data: {
		counter: 0
	},
	methods: {
		counter_add: function(){
			this.counter++
		}
	}
})

app18 = new Vue({
	el: '#app18',
	data: {
		value: parseInt(document.getElementById("values").value) != null ? parseInt(document.getElementById("values").value) : 20
	},
	methods: {
		value_change: function(){
			new_value_sum = parseInt(document.getElementById("values").value)
			this.value += new_value_sum
		}
	},
	watch: {
		value(new_value, old_value){
			this.value = parseInt(document.getElementById("values").value) != null ? parseInt(document.getElementById("values").value) : 20
		}
	}
})

new Vue({
	el: '#app19',
	data: {
		value: 0,
		x: 0,
		y: 0
	},
	methods: {
		get_mouse_coordinate: function(event){
			this.x = event.clientX
			this.y = event.clientY
		},
		sum_number: function(number, ev){
			console.log(ev)
			this.value += number
		},
		stop_propagation: function(ev)
		{
			ev.stopPropagation()
		},
		show_alert: function(){
			alert("Apertou uma tecla.")
		}
	}
})

new Vue({
	el: "#app20",
	data: {
		title: "Hello Stranger"
	}
})

new Vue({
	el: "#app21",
	data: {
		counter: 0,
		counter2: 0
	},
	methods: {
		increase: function(){
			this.counter++
		},
		increase2: function(){
			this.counter2++
		}		
	},
	computed: {
		// This is a syncroned prop
		results(){
			console.log("Computed methos is called")
			return this.counter >= 5 ? 'Value equal or higher than 5' : 'Value lower than 5'
		}
	},
	watch: {
		// This method is the same variable on data.counter, for default you can get the new and old value
		// This watch is used for monitoring a variable, html dom, a method or anything can change in your app
		counter(new_value, old_value){
			console.log(old_value, new_value)
			// this setTimeout will call the arrow function after 2 seconds
			setTimeout(() => {
				this.counter = 0
			}, 2000)
		}
	}
})

new Vue({

	el: "#app22",
	data: {
		applyC1: false,
		classCSS: 'c3',
		applyRotate: true
	},
	computed:{
		style1(){
			return {
				c1: this.applyC1,
				c2: !this.applyC1
			}
		}
	}

})

new Vue({
	el: "#app23",
	data: {
		color: 'red',
		vueWidth: 100,
		vueHeight: 50
	},
	computed: {
		myStyle(){
			return { 
				// JavaScrip notation
				backgroundColor: this.color,
				width: this.vueWidth + 'px',
				height: this.vueHeight + 'px'
			}
		} 
	}
})

new Vue({
	el: '#app24',
	data: {
		name: 'Pedro',
		loged: false,
		anonimous: false
	}
})

new Vue({
	el: '#app25',
	data: {
		colors: ['red', 'green', 'blue'],
		people: [ 
			{name: 'Pedro', age: 29, weight: 120},
			{name: 'Yago', age: 29, weight: 87},
			{name: 'Zaque', age: 34, weight: 97}
		]
	}
})

new Vue({
	el: '#app26',
	data: {
		app: "App26"
	}
})

new Vue({
	el: '#app27',
	data: {
		app: "App27"
	}
})

// Global const
const counterApp28 = {
	template: `
		<div>
			<span>{{ counterApp281 }}</span>
			<button @click="counterApp281++"> ADD </button>
			<button @click="counterApp281--"> SUB </button>
		</div>
		`,
		data() {
			return {
				counterApp281: 0
			}
	}
}

new Vue({
	el: '#app28',
	components: {
		// Local component
		counter1: counterApp28
	},
	data: {
		app: "App28"
	}
})