$(function(){

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
      }
      return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $('.anos > .badge-pill').click(function(){
    var ano = $(this).attr('id');
    var slug_deputado = window.location.href.toString().split(window.location.host)[1].replace('/', '');
    var data_deputado = {'slug_deputado': slug_deputado, 'ano': ano};
    $.ajax({
      type : "POST",
      url: '/ajax/dadosdeputados',
      cache : false,
      data: data_deputado,
      contentType: "application/x-www-form-urlencoded",
      beforeSend: function(xhr, settings) {
        $('.wrapper-load-graficos').addClass('loading');
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      },
      success: function(response){
        console.log(response);
        $('.wrapper-load-graficos').removeClass('loading');
      },
      error: function(response){
        console.log(response);
        $('.wrapper-load-graficos').removeClass('loading');
      }
    })
  });
});
