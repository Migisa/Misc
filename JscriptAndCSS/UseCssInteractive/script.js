$(document).ready(function(){
		$('div').click(function(){
			$(this).height('200px');
		  $(this).width('200px');
		  $(this).css('border-radius','10px');
		});

    $('p').mouseenter(function(){
       $(this).html('jQuery magic in action!'); 
    });  

    $('p').mouseleave(function(){
       $(this).html('back to normal!'); 
    });  
})
