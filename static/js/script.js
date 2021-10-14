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
    
    initTheme();
});

 // function to set a given theme/color-scheme
 function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-light');
        document.querySelector("#site-logo").src="/static/images/logo_dark.png";
    } else {
        setTheme('theme-dark');
        document.querySelector("#site-logo").src="/static/images/logo_light.png";
    }
}

// Immediately invoked function to set the theme on initial load
function initTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.querySelector("#site-logo").src="/static/images/logo_light.png";
    } else {
        setTheme('theme-light');
        document.querySelector("#site-logo").src="/static/images/logo_dark.png";
    }
};