$(document).ready(function(){
    $('#text').click(function(){
        $('#text').addClass('highlighted');
    });

		$('#text2').click(function(){
			$('#text2').toggleClass('highlighted');
		});
});
