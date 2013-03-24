$(document).ready(function(){
	$('div').click(function(){
		$(this).fadeOut('fast');
	});	
	
	$('div').hover(function(){
		$(this).toggleClass('red');
	});

	$('.box').click(function(){
		$(this).fadeTo('fast', 0.25);
	});
});
