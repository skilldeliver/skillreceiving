function printReverse(list){
	for (var i = list.length - 1; i >= 0; i--){
		console.log(list[i]);
	}
}

function isUniform(list){
	first = list[0]
	for (var i = 1; i < list.length; i++){ /* Mistakenly I did the i start from zero but a better 
		                                      and efficient solution is to start from 1 */
		if (first !== list[i]){
			return false;
		}
	}
	return true;
}

function sumArray(list){
	var total = 0;
	for (var i = 0; i < list.length; i++)
	{
		total += list[i]
	}
	return total;
}


function max(list) {
	max_num = list[0]
	for (var i = 0; i < list.length; i++)
	{
		if (list[i] > max_num){
			max_num = list[i]
		}
	}
	return max_num
}

printReverse([1, 2, 3, 4]);
console.log(sumArray([1, 2, 3]))
console.log(isUniform([1, 1, 1, 1, 1]))
console.log(isUniform([1, 1, 1, 1, 2]))
console.log(max([10, 3, 10, 4]))
console.log(max([11, 5, 17, 3, 14, 9]))