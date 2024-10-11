import {Animal} from "./animal.js"
let p = document.getElementsByTagName('p')[0]
p.textContent = "Hello from js script"

let sophie = new Animal('Sophie', 'cow')

p.textContent = sophie.getName()
console.log(sophie.getName())