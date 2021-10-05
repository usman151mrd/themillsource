(function ($) {

    $.fn.setGreeting = function(username){
      var now = new Date().getHours();
      var text, color;
  
      if (now >= 6 && now < 12){
        text = 'Good Morning';
        color = '#008100';
      }
      else if (now >= 12 && now < 17){
        text = 'Hello';
        color = '#CC7A29';  
      }
      else if (now >= 17 && now < 22 ){
        text = 'Good Evening';
        color = '#005CE6';
      }
      else{
        text = 'Good Night';
        color = '#001C53';
      }
  
      return this.each(function(){
        var $div = $(this);
  
        // $div.html(text + ' ' + username);
        $div.html(text);
        // $div.css({
        //   'padding': '5px 10px',
        //   'backgroundColor': color,
        //   'color': '#fff'
        // });
      });
    }
  
  }(jQuery));