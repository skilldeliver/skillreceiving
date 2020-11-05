var age = Number(prompt("Enter age"));

if (age < 18){
	console.log("Sorry, you are not old enough to enter the venue");
}
else if(age < 21){
	console.log("You can enter, but cannot drink");
}
else {
	console.log("Come on in. You can drink");
}

if (age < 0){
	console.log("Error message")
}
if (age === 21){
	console.log("Happy 21st birthday!!")
}
if (age % 2 !== 0){
	console.log("Your age is odd")
}

if (Math.sqrt(age) % 1 === 0){
	console.log("Perfect square")
}
// or look at this 

// if(age % Math.sqrt(age) === 0) {
//   console.log("Your age is a perfect square!");
// }