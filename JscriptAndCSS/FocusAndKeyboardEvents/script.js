$(document).ready(function(){
	$('input').focus(function(){
		$(this).css('outline-color','#FF0000');
	});

	$(document).keydown(function(key){
		$('.anyevent').animate({left:'+=10px'}, 'fast');
		/*alert(key.which); */
		switch(parseInt(key.which,10)){
			case 65:
				$('.moveme').animate({left: "-=10px"}, 'fast');
				break;
			case 68:
				$('.moveme').animate({left: "+=10px"}, 'fast');
				break;
			case 83:
				$('.moveme').animate({top: "+=10px"}, 'fast');
				break;
			case 87:
				$('.moveme').animate({top: "-=10px"}, 'fast');
			default:
				break;
		}
	});
});
