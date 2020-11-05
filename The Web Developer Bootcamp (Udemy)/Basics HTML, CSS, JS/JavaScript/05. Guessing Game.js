var secret_num = 7;

while(1){
	guessed_num = Number(prompt("Have a number guess: "));

	if (secret_num === guessed_num){
		alert("Congrats! You guessed my number");
		break;
	}
	else if (secret_num > guessed_num){
		alert("Too low");
	}
	else {
		alert("Too high")
	}
}