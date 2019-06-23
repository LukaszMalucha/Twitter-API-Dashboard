
$('.dropdown-trigger').dropdown();


$(".alert-user").delay(3000).fadeOut(200, function() {
    $(this).alert('close');
});



$(document).ready(function() {

    $('select').formSelect();

    $('.sidenav').sidenav();

    $('.modal').modal();

    $('#flashButton').on('click', function(event){

        $('.card-menu').fadeOut(150).fadeIn(150);

    });


});


