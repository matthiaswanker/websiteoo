$(document).ready(function(){

    $(".buddy").on("swiperight",function(){
        var counterValue = parseInt($('#watchlist_bubble').html());
      $(this).addClass('rotate-left').delay(700).fadeOut(1);
      $('.buddy').find('.status').remove();
        var index = document.URL.search("client/[0-9]+") + 7;
        var user_id = document.URL.slice(29, document.URL.length-1);
        //alert(user_id);
      $.get("update/"+$(this).children("div:first").text());
      $(this).append('<div class="status like">Like!</div>');
        $('#watchlist_bubble').html((counterValue+1));
      /*if ( $(this).is(':last-child') ) {
        $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
       } else {
          $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
       }*/
    });

   $(".buddy").on("swipeleft",function(){
    $(this).addClass('rotate-right').delay(700).fadeOut(1);
    $('.buddy').find('.status').remove();
	
    $(this).append('<div class="status dislike">Dislike!</div>');
    /*if ( $(this).is(':last-child') ) {
     $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
     } else {
        $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
    } */
  });

     $(".button_like").on("click",function(){
         var counterValue = parseInt($('#watchlist_bubble').html());
      $(this).parent().addClass('rotate-left').delay(700).fadeOut(1);
      $('.buddy').find('.status').remove();
        var index = document.URL.search("client/[0-9]+") + 7;
        var user_id = document.URL.slice(29, document.URL.length-1);
        //alert(user_id);
      $.get("update/"+$(this).parent().children("div:first").text());
      $(this).parent().append('<div class="status like">Like!</div>');
         $('#watchlist_bubble').html((counterValue+1));
      /*if ( $(this).is(':last-child') ) {
        $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
       } else {
          $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
       }*/
    });

    $(".button_dislike").on("click",function(){
    $(this).parent().addClass('rotate-right').delay(700).fadeOut(1);
    $('.buddy').find('.status').remove();

    $(this).parent().append('<div class="status dislike">Dislike!</div>');
    /*if ( $(this).is(':last-child') ) {
     $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
     } else {
        $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
    } */
  });
});