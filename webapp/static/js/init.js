(function($){
  $(function(){
    $('.button-collapse').sideNav();
    $('.btn-q').click( function() {
      var img = $('#q-img').attr('data-img');
      var ans = $(this).attr('data-ans');
      $.post("/vote", {"img":img, "ans":ans}, function (result) {
        console.log(result);
      });
    });
  }); // end of document ready
})(jQuery); // end of jQuery name space