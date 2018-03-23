var myScope = (function(){
  id_antiga = '';
  var dados = $('#gastos_deputado').val();

  console.log(dados);
  //canvas
  var canvas = d3.select('.wrapper-itens-graficos')
    .append('svg')
      .attr('width', '100%')
      .attr('height', '95%')
      .attr('style', 'margin-top: 10px');
  
  var width = $('.wrapper-itens-graficos').innerWidth();
  var height = $('.wrapper-itens-graficos').innerHeight();
  var dados_placeholder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ];
  canvas_width = $('.wrapper-itens-graficos > svg').width();
  canvas_height = $('.wrapper-itens-graficos > svg').height();
  var grupo_bar = canvas.selectAll('.grupo-bar')
  .data(dados_placeholder)
  .enter()
  .append('g')
    .attr('class', 'grupo-bar');
    //DFECF4 claro
    //818EA7 escuro

  grupo_bar
    .append('rect')
    .attr('class', 'wrapper-chart')
      .attr('fill', '#DFECF4')
      .attr('width', '25px')
      .attr('height', function(){
        return canvas_height - 15;
      })
      .attr('x', function(i){
        return (i * (canvas_width / 12) - (canvas_width / 12));
      });

  grupo_bar
    .append('rect')
      .attr('class', 'data-chart')
      .attr('width', '25px')
      .attr('fill', '#818EA7')
      .attr('rx','5')
      .attr('height', function(d){
        return d * 10;
      })
      .attr('y', function(d){
        return canvas_height - 10 - d * 10;
      })
      .attr('x', function(i){
        return (i * (canvas_width / 12) - (canvas_width / 12));
      });

  
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
        var slug_deputado = window.location.href.toString().split(window.location.host)[1].split('/')[1];
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
            charts(response['gastos'], ano);
          },
          error: function(response){
            $('.wrapper-load-graficos').removeClass('loading');
          }
        });
      }
  
      $('.anos > .badge-pill').click(
        function(){
          reloadGraph($(this).attr('id'));
          
        }
      );
  
      // Categorias
      $('.dropdown-menu .dropdown-item')
        .click(function(){         
          var id_atual = $($(this).find('.dropdown-menu__item__title').parent()[0]).attr('id');
          $('.categoria-atual').text($(this).find('.dropdown-menu__item__title').text());
          $('.categoria-atual').addClass(id_atual).removeClass(id_antiga);
          id_antiga = id_atual;
        })
    });
  
    function charts(data, ano){
      console.log(data);
      console.log(ano);
      var cat_10, cat_11, cat_12, cat_13, cat_14, cat_15;
    }
  })();
  