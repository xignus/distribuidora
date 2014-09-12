var limpiarform = function (){
    $('#contacto_nombre__label').hide();
    $('#contacto_email__label').hide();
    $('#contacto_mensaje__label').hide();
    $('input[type=text]').addClass('form-control');
    $('textarea').addClass('form-control');
    $('input[type=submit]').addClass('btn-primary');
    $('#contacto_nombre').attr('placeholder','Nombre...')
    $('#contacto_email').attr('placeholder','E-mail...')
};

var contact_form = function(){
    $('ul.nav li:nth-child(4)').addClass("contact");
    $('.contact a').attr('data-toggle','modal');
    $('.contact a').attr('data-target','#MyContact');
};

limpiarform();
contact_form();
