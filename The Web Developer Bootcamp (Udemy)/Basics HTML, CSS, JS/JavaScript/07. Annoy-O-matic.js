
// var command = " "
// while (!(command === "yes" || command === "yeah")){
// 	command = prompt("Are we there yet")
// }
// alert("Yay, we finally made it!")



// indexOf method search in the entire string the given string as parameter
// if it is not findined returns a -1 else return the index of the finded string

var answer = prompt("Are we there yet?")

while (answer.indexOf("yes") === -1 && answer.indexOf("yeah") === -1){
	answer = prompt("Are we there yet?")
}

alert("YAY, WE MADE IT!!!")