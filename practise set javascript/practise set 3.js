//write a program to print the makrs of a student in an object using for loop
// obj={harry:98,rohan:70,akash:7}

obj = { harry: 98, rohan: 70, akash: 7 };


for (const key in obj) {
        const element = obj[key];
        console.log(element)
}

//write a program to print "try again" until the user enter the correct number

// let i= "10"
// let input = prompt("write your number");

// while(i!=input){
//     alert("try again")
//     input = prompt("write your number");
// }

//write a function to find mean of 5 numbers

function mean(a,b,c,d,e){
    console.log((a+b+c+d+e)/5)
}

mean(23,23,23,23,23)
