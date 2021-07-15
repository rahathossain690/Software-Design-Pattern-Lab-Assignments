// Rahat Hossain
// SH - 32


/*
Installation
1. Nodejs
2. Npm
3. Type: `npm install` on the command line

General interaction with the terminal
    Choose design style
    1. Simplistic
    2. Highly detailed
    Your choice: 1 (input)
    1
    Choose file type
    1. XML
    2. ANY
    Your file type:  1 (input)
    Filename : config.xml (input)
    Server started on port 3000 (Go to localhost:3000 on browser)
*/

// supported format: TYPE, value, X, Y, color, bg-color, width, height

const WindowManager = (function () {
    // Window manager class
    // Follows singleton pattern
    
    // stores class instance and html formatted string 
    let instance;
    let _html;

    // constructor
    // param: designStyle - int
    function create (designStyle) {
        return {
            log: () => console.log(designStyle), // logs design style
            loadUI: (configManager) => {        // loads config manager
                let elementStr = "";
                while(configManager.hasMoreItems()) {
                    const windowManager = instance
                    elementStr = elementStr +  windowManager.elementConverter(configManager.nextItem()) + "\n" // converts config manager item to html string
                }
                // stores html formatted string
                _html = `
                    <html>
                        <head>
                            <title>Assignment 3</title>
                        </head>
                        <body style="width: 100%; height: 100%;">
                            ${elementStr}
                        </body>
                    </html>
                `
            },
            getHTML: () => {    // returns html formatted string
                return _html
            }
            ,
            cssConverter: (configManagerItem) => {  // converts config manager item to html string
                let css_str = "position:fixed;"
                configManagerItem.forEach(each => {
                    switch(each.name) {
                        case "X":
                            css_str += "left:" + each.value + ";";
                            break;
                        case "Y":
                            css_str += "top:" + each.value + ";";
                            break;
                        case "Color":
                            css_str += "color:" + each.value + ";";
                            break;
                        case "Bg-color":
                            css_str += "background-color:" + each.value + ";";
                            break;
                        case "Width":
                            css_str += "width:" + each.value + ";";
                            break;
                        case "Height":
                            css_str += "height:" + each.value + ";";
                            break;
                        
                      }
                })
                return css_str
            },
            elementConverter: (configManagerItem) => { // converts config manager item to html string
                const windowManager = instance
                switch(configManagerItem[0].value) {
                    case "Button":
                        return `<button style="${windowManager.cssConverter(configManagerItem)}">${configManagerItem[1].value}</button>`
                    case "EditBox":
                        return `<input type="text" style="${windowManager.cssConverter(configManagerItem)}" value="${configManagerItem[1].value}"/>`
                    case "TextBox":
                        return `<textarea style="${windowManager.cssConverter(configManagerItem)}">${configManagerItem[1].value}</textarea>`
                }
            }
            ,
            getSupportedFormat: () => { // returns supported formats with respect to design style
                if(designStyle == "1") { // simplistic
                    return [
                        {
                            name: "TYPE",
                            default: "Button",
                        },
                        {
                            name: "Value",
                            default: "Default value"
                        },
                        {
                            name: "X",
                            default: 100
                        },
                        {
                            name: "Y",
                            default: 100
                        }
                    ]
                } else { // highly detailed
                    return [
                        {
                            name: "TYPE",
                            default: "Button",
                        },
                        {
                            name: "Value",
                            default: "Default value"
                        },
                        {
                            name: "X",
                            default: 100
                        },
                        {
                            name: "Y",
                            default: 100
                        },
                        {
                            name: "Color",
                            default: "#2d2d2d"
                        },
                        {
                            name: "Bg-color",
                            default: "#696969"
                        },
                        {
                            name: "Width",
                            default: 100
                        },
                        {
                            name: "Height",
                            default: 100
                        }
                    ]
                }
            }
        };
    }

    return {
        getInstance: function(designStyle) { // returns instance of window manager
            if(!instance) { // if instance is not created
                instance = create(designStyle); // create instance
            }
            return instance;
        }
    };
})();

const csv = require('csvtojson');
// const 

class ConfigManager{
    // Config Manager Superclass

    constructor(filename) { // Constructor
        this.filename = filename;
        this.data = []
        this.current_index = 0  
    }

    async read(){ 
        // reads csv file
        // Subclasses are going to have their own implementation
        console.log(`Sould read ${this.filename}`)
    }

    convert(data) {
        // Converts data to object
        this.data = data;
        const supportedFormat = WindowManager.getInstance().getSupportedFormat()
        const new_data = []
        for(let index = 0; index < this.data.length; index++) { 
            let to_insert = []
            for(let position = 0; position < this.data[index].length && position < supportedFormat.length; position++) { 
                to_insert.push({
                    name: supportedFormat[position].name,
                    value: !!this.data[index][position] ? this.data[index][position]: supportedFormat[position].default
                })
            }
            new_data.push(to_insert)
        }
        return this.data = new_data
    }

    nextItem() { // returns next item
        return this.data[this.current_index++];
    }

    hasMoreItems() { // returns true if more items are available
        return this.data.length != this.current_index;
    }
}


class ConfigManagerFile extends ConfigManager{
    // Congiuration Manager File Class
    constructor(filename){
        super(filename)
    }

    async read() { // reads csv file
        return new Promise((resolve, reject) => {
            csv({
                noheader: true,
                output: "csv"
            }).fromFile(this.filename)
            .then(out => {
                resolve(this.convert(out))
            }).catch(err => {
                reject(err.message)
            })
        })
    }
}

const fs = require('fs');
const xml2js = require('xml2js')

class ConfigManagerXML extends ConfigManager{
    // Configuration Manager XML Class
    constructor(filename){
        super(filename)
    }

    async read() { // reads csv file
        return new Promise((resolve, reject) => { 
            const parser = new xml2js.Parser()
            parser.parseString(fs.readFileSync(this.filename, 'utf8'), (err, result) => {
                if(err) {
                    reject(err.message)
                } else {
                    result = result.wraper;
                    let to_insert = [];
                    Object.keys(result).forEach(type => {
                        result[type].forEach(item => {
                            let new_array = [type]
                            Object.keys(item.$).forEach(thing => {
                                new_array.push(item.$[thing])
                            })
                            to_insert.push(new_array)
                        })
                    })
                    resolve(this.convert(to_insert))
                }
            })
        })
    }
}


class WindowManagerAdapter{
    // Window Manager Adapter Class
    constructor(designStyle, windowManager) {
        this.designStyle = designStyle
        this.windowManager = windowManager
    }

    loadConfigManager(configManager) { // loads config manager
        this.windowManager.loadUI(configManager) // loads config manager
    }
}

class AbstractFactory{
    // Abstract Factory Class
    getConfigManager(fileType, filename) { // returns config manager
        if(fileType == "1"){ // any
            return new ConfigManagerXML(filename);
        } else {
            return new ConfigManagerFile(filename);
        }
    }
}

class Util{ // Util class
    async scan(scanString="") { // Scanning function
        return new Promise((resolve, reject) => {
            const readline = require('readline').createInterface({
                input: process.stdin,
                output: process.stdout
              })
            readline.question(`${scanString} `, output => {
                readline.close()
                resolve(output)
            })
        })
    }

    print(str) { // Print function
        console.log(str)
    }
}

const express = require('express');
const app = express();

async function main() {
    const util = new Util()
    try{
        // Takes a config file type and a filename
        util.print("Choose design style")
        util.print("1. Simplistic")
        util.print("2. Highly detailed")
        const designStyle = await util.scan("Your choice:")
        const windowManager = WindowManager.getInstance(designStyle);
        windowManager.log()

        util.print("Choose file type")
        util.print("1. XML")
        util.print("2. ANY")

        const fileType = await util.scan("Your file type: ")
        const filename = await util.scan("Filename :")

        // Creates an instance of config manager
        const configManager = (new AbstractFactory()).getConfigManager(fileType, filename)
        await configManager.read() // reads file

        const windowManagerAdapter = new WindowManagerAdapter(designStyle, windowManager) // creates window manager adapter
        windowManagerAdapter.loadConfigManager(configManager) // loads config manager

        // express app start and render html from raw string
        app.get("/", (req, res) => {
            res.send(windowManager.getHTML())
        })
        // start server
        app.listen(3000, () => {
            util.print('Server started on port 3000')  
        })

    } catch(err) {
        // catch error
        util.print(err)
    }
}

// run the main function
main() 