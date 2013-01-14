$(document).ready(function(){
	$('#slider').slideDown('slow');
	$('#clickme').mouseenter(function(){
		$(this).fadeTo('fast', 0.25);
	});
	$('#clickme').mouseleave(function(){
		$(this).fadeTo('fast',1.25)
	});
});