window.onlload = function () {
	new Vue({
		el: '#challenge',
		data: {
			showMessage: true,
			names: ['Pedro', 'Bia', 'Ana', 'Rebeca'],
			livros: {
				titulo: 'O Senhor dos Aneis',
				autor: 'J.R.R. Tolkiens',
				volume: '3'
			},
			aluno: {
				id: 10,
				nome: 'Maria',
				notas: [7.67, 8.33, 6.98, 9.21]
			}
		}
	});
}