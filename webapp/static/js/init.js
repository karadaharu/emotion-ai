(function($){
  $(function(){
    $('.button-collapse').sideNav();
    $('.btn-q').click( function () {
      console.log('click');
      $.post("/vote", function (result) {
        console.log(result);
      });
    });
  }); // end of document ready
})(jQuery); // end of jQuery name space