$(document).ready(function(){
     $("#show-button").click(function () {
         $("#main-menu").show("slow") //addClass('show-menu');
     });

     $("#close-button").click(function () {
        $("#main-menu").hide("fast") //removeClass('show-menu');
    })

    $('#greeting').setGreeting('Reader');

    $('#file-btn').click(function(){
        $('#pr-image').click()
    })
});