class Table {

    constructor(arr){
        this.header = arr[0];
        // remove o primeiro elemento do array
        arr.shift();
        this.rows = arr;
    }

    //Get transforma o método em um atributo, obrigatoriamente retornando algo.
    get RowCount(){
        return this.rows.length;
    }

    get ColumnCount(){
        return this.header.length;
    }

}

module.exports = Table;