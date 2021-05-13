#!/usr/bin/node
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
	$.get('#hello').text(data.hello);
})
