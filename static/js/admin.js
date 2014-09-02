var new_content = function(){
    $('.add_new').click(function(){
	$('.new_form').show('slide');
	$('.add_new').hide('slide')
    });
};

$(document).ready(function(){
    
    $('.new_form').hide();
    new_content();
})
