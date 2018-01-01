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
    console.log(slug_deputado);
    console.log(ano);
    // console.log(csrftoken);
    // console.log($(this).attr('id'));
    // console.log(slug_deputado);
    // var url_req = 'dados'+slug_deputado+'/'+ano;
    var data_deputado = {'slug_deputado': slug_deputado, 'ano': ano};
    $.ajax({
      type : "POST",
      url: '/ajax/dadosdeputados',
      cache : false,
      data: data_deputado,
      contentType: "application/x-www-form-urlencoded",
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      },
      success: function(response){
        console.log(response)
      },
      error: function(){
        console.log('droga')
      }
    })
  });
});


// url : "/cms/login/",
// type : "POST",
// data : 	data,
// cache: false,
// processData: false,
// contentType: false,
