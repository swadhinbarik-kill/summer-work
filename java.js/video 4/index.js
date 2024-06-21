//loops


//for
for (let i = 1; i <= 100; i++) {
    console.log(i);
}

//for in
let obj={
    name:"swadhin",
    branch:"civil",
    college:"NITJ"
}
for (key in obj) {
        element = obj[key]
        console.log(key,element)        
}

//for of 

for (const char of "Swadhin") {
    console.log(char)
}

//while loop
let i=5
while (i==5) {
   console.log(i)
   i++; 
}

//do while
// executed for atleast 1 time 
do{
    console.log("hello")
    i++
}while(i<4)