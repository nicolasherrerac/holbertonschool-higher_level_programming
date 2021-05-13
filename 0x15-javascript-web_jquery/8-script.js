#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
	for (const dict of data.results) {
		const lis = $('<li></li>').text(dict.title);
		$('#list_movies').append(lis);
	}
});
