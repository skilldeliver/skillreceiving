
// WAY 1
toggle = 1;
var but = document.querySelector("button");

but.addEventListener("click", function(){
	console.log(toggle)
	if (toggle) {
		document.body.style.background = "purple";
		toggle = 0;
	}
	else {
		document.body.style.background = "white";
		toggle = 1;
	}
})

// WAY 2
toggle = 1;
var but = document.querySelector("button");

but.addEventListener("click", function(){
	console.log(toggle)
	if (toggle) {
		document.body.style.background = "purple";
	}
	else {
		document.body.style.background = "white";
	}
	toggle = !toggle;
})

// WAY 3
var but = document.querySelector("button");
but.addEventListener("click", function(){
	document.body.classList.toggle("purple");
})