// use logical operator to find whether age of a person lies between 10 and 20

a = 19
 
if(a>10 && a<20){
    console.log("Age is between 10 and 20")
}
else{
    console.log("not in range")
}
 
//demonstrate the use of switch case statements in javascript
 
/*
switch(expression) {
    case x:
      // code block
      break;
    case y:
      // code block
      break;
    default:
      // code block
  }
*/
 
// write a javascript program to find whether a number is divisible by either 2 or 3
 
if(a%2==0){
    console.log("number is divisible by 2")
}
 
else if(a%3==0){
    console.log("number is divisible by 3")
}
 
else{
    
    console.log("number is not divisible by either 2 nor 3")
}

// write a javascript program to find whether a number is divisible by 2 and 3

if(a%3==0 && a%2==0){
    console.log("number is divisible by 3 and 2")
}
 
else{
    
    console.log("number is not divisible by either 2 nor 3")
}

// print "you can drive" or "you cannot Drive" based on age being grater than 18 using ternary operator

x = (a>18)?"you can drive":"you cannot Drive"

console.log(x)
