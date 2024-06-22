//faulty calculator

// + ---> -
// * ---> +
// - ---> /
// / ---> **


a = Math.random()
let n1 = prompt("Enter first number")
let n2 = prompt("Enter second number")
let op = prompt("select the criteria")

obj={
    '+': '-',
    '*': '+',
    '-': '/',
    '/': '**'
}

if(a>0.1){
    alert(`answer is ${eval(`${n1} ${op} ${n2}`)}`)
}

if(a<0.1){
    c=obj[c]
    alert(`answer is ${eval(`${n1} ${op} ${n2}`)}`)
}

