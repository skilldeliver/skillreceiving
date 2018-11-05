// var todos = [];
// window.setTimeout(function() {
// 	var command = " ";
// 	while (command !== "quit"){
// 		command = prompt("What you would like to do?")
// 		if (command === "new"){
// 			var new_item = prompt("Add someting new")
// 			todos.push(new_item)
// 		}
// 		else if(command === "list"){
// 			console.log(todos)
// 		}
// 	}
// }, 500);

function displayList(){
	todos.forEach(function (task, i)
	{
		console.log("-------------------")
		console.log(i + 1 + ":" + task)
	}
	)
	console.log("-------------------")

}

function removeItem(){
	which_item = Number(prompt("Enter index of todo to remove"))
	console.log(todos[which_item - 1] + " removed")
	todos.splice(which_item - 1, 1)
}

function addItem(){
	var new_item = prompt("Add someting new")
	todos.push(new_item);
	console.log(new_item + " added to the list")
}
window.setTimeout(function() {
	todos = [];
	var command = " ";
	while (command !== "quit"){
		command = prompt("What you would like to do?")
		if (command === "new"){
			addItem();

		}
		else if(command === "list"){
			displayList();

		}
		else if (command === "remove"){
			removeItem();
			displayList();
		}
		else if (command !== "quit") {
			alert("Unknown command!")
		}
	}
}, 500);

