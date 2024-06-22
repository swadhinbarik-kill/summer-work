//strings

let name='human'

console.log(name.length)

//template literals
//use of backtics instead of qoates to define a funtion

let Pname=`swadhin`

//string interpolation
console.log(`my name is ${Pname}`)

//accessing character in string
for (let i = 0; i < Pname.length; i++) {
    console.log(Pname[i])    
}

//escape sequence
// let x = `i cann`t live` // js will missunderstand it 
let x = `i cann\`t live`    // similarly \"
//also 
// \n -->newline
// \t --> tab 
// \r -->carriage return


//string properties
console.log(Pname.toUpperCase)
console.log(Pname.toLowerCase)
console.log(Pname.slice(1,4)) //4 not included
console.log(Pname.slice(1))   //1 to end
console.log(Pname.replace('sw','para')) // First occurance is only replaced
console.log(Pname.concat(" is ",name))
let y = x.trim()
console.log(y) //removes white spaces

//strings are immutable 

