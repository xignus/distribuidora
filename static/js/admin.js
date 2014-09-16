var new_content = function(){
    $('.add_new').click(function(){
	$('.new_form').show('slide');
	$('.add_new').addClass('disabled')
    });
};

var form_pretty = function(){
    $('input[type=text]').addClass('form-control');
    $('textarea').addClass('form-control');
    $('.ui-button-text-icon-primary').addClass('btn btn-primary')
};

var datatables=function(){
    $('#tabla').dataTable();
};

$(document).ready(function(){
    
    $('.new_form').hide();
    new_content();
    form_pretty();
})
