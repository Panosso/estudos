var fs = require("fs")
var util = require("util")

class Reader{

    constructor(){
        this.reader = util.promisify(fs.readFile)
    }

    async Read(filepath){
        try{

            return await this.reader(filepath, "utf-8")

        }catch{

            return undefined;

        }
    }

}

module.exports = Reader;