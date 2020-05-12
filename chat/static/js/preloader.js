$(document).ready(function(){
    var Body = $('body');
    Body.addClass('preloader-site');
})

onload = (function(){
    $('.preloader-wrapper').fadeOut();
    $('body').removeClass('preloader-site');
})