$(document).ready(function() {
   $('div').mouseenter(function() {
       $(this).animate({
           height: '+=10px'
       });
   });
   
   $('div').mouseleave(function() {
		$(this).animate({
			height: '-=10px'
		});
   });
   
   $('div').click(function(event){
		alert('This square will now dissapear');
		$(this).slideUp();
   });
});