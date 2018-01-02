var myScope = (function(){
  // var dados;

  var d3graph = d3.select('.wrapper-itens-graficos');
  var svg = d3graph.append("svg");

  var width = $('.wrapper-itens-graficos').innerWidth();
  var height = $('.wrapper-itens-graficos').innerHeight();
  svg.attr("height", height).attr("width", width);

  for(var i = 0; i < 13; i++){
    svg.append('div')
        .attr('class','div-chart');
  }

  $(function(){

    // dados ajax
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


    reloadGraph = function(ano){
      var slug_deputado = window.location.href.toString().split(window.location.host)[1].replace('/', '');
      var data_deputado = {'slug_deputado': slug_deputado, 'ano': ano};
      var resultado = $.ajax({
        type : "POST",
        url: '/ajax/dadosdeputados',
        cache : false,
        data: data_deputado,
        dataType: 'json',
        contentType: "application/x-www-form-urlencoded",
        beforeSend: function(xhr, settings) {
          $('.wrapper-load-graficos').addClass('loading');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(response){
          $('.wrapper-load-graficos').removeClass('loading');
          //return resposta;
          // var legal = response;
          // return legal;
          dados_deputado = response;
          // pegaDados(response);
        },
        error: function(response){
          console.log(response);
          $('.wrapper-load-graficos').removeClass('loading');
        }
      });
    }

    $('.anos > .badge-pill').click(
      function(){
        var ano = $(this).attr('id');
        var dados = reloadGraph(ano);
      }
    );

    // Categorias

    $('.dropdown-menu .dropdown-item')
      .click(function(){
        var categoria = $(this).find('.title-categoria').text();
        var categoria_atual = $('.categoria-atual').text(categoria);
      })

  });

})();
