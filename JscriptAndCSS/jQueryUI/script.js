$(document).ready(function(){
	$('.bounce').click(function(){
		$(this).effect('explode');
	});

	$('.bounce').hover(function(){
		$(this).effect('bounce', {times:3}, 500);
	});

	$('.slide').click(function(){
		$(this).effect('slide');
	});


});
