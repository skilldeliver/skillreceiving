// function isEven(num){
// 	if (num % 2 == 0){
// 		return true;
// 	}
// 	return false;
// }

// better - 
function isEven(num){
	return num % 2 === 0
}

function factorial(num){
	var total = 1;
	for (var i = num; i >= 1; i--){
		total *= i;
	}
	return total;
}

function kebabToSnake(str){
	res = str.replace("-", "_");
	return res
}


function printMyName(){
	console.log("Vladislav")
}
