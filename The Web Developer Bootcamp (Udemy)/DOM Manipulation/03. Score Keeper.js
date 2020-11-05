var game = 1;
var playingTo = 5;
pl1_val = 0;
pl2_val = 0;

var inp = document.querySelector("input");
var pl1_btn = document.querySelector("#pl1");
var pl2_btn = document.querySelector("#pl2");
var res_btn = document.querySelector("#res");

inp.addEventListener("input", function(){
	playingTo = Number(inp.value);
	document.querySelector("p").innerHTML = "Playing to: " + playingTo;
})

pl1_btn.addEventListener("click", function(){
	if (game){
		pl1_val++;
		document.querySelector("h1").innerHTML = "<span id=\"fir\">" + pl1_val + "</span> " + " to " + "<span id=\"sec\">" + pl2_val + "</span>";
	}
	if (pl1_val === playingTo) {
		document.querySelector("#fir").style.color = "green"
		game = 0;
	}
})

pl2_btn.addEventListener("click", function(){
	if (game) {pl2_val++;
		document.querySelector("h1").innerHTML = "<span id=\"fir\">" + pl1_val + "</span> " + " to " + "<span id=\"sec\">" + pl2_val + "</span>";
	}
	if (pl2_val === playingTo) {
		document.querySelector("#sec").style.color = "green";
		game = 0;
	}
})

res_btn.addEventListener("click", function(){
	game = 1;
	pl1_val = 0;
	pl2_val = 0;
	document.querySelector("h1").innerHTML = pl1_val + " to " + pl2_val;
})
