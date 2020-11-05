var movies = [
{title: "Fight Club",
 rating: 5,
 hasWatched: true}, 
{title: "Black Swan",
 rating: 4.5,
 hasWatched: true},
{title: "Being John Malchovich",
 rating: 0,
 hasWatched: false},
 {title: "Prisoners",
 rating: 4,
 hasWatched: true}
]

movies.forEach(function(name, i){
	if (name.hasWatched === true){
		console.log("You have watched " + "\"" + name.title + "\" - " + name.rating + " stars");
	}
	else {
		console.log("You have not seen " + "\"" + name.title + "\" - " + name.rating + " stars");
	}
})