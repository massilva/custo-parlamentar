var myScope = (function(){

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
          console.log(cookies);
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
        }
        console.log('cookievalue'+ cookieValue);
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken); 
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
          console.log(response['gastos']);
          $('.wrapper-load-graficos').removeClass('loading');
          charts(response['gastos'], ano);
        },
        error: function(response){
          console.log(response);
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
        $('.categoria-atual').text($(this).find('.dropdown-menu__item__title').text());
      })
  });

  function charts(data, ano){
    console.log(data[ano]);
    var cat_10;
    var cat_11;
    var cat_12;
    var cat_13;
    var cat_14;
    var cat_15;
  }
})();


var menu = (function(){
  //desktop
  var depu = '.deputados__item';
  var sear = "#procurar";

  //mobile
  var depuM = '.deputados__item__mobile';
  var searM = "#searchMobile";


  //busca dinamica deputados
  function listaDeputados(cssDeputados, searchId, mobile=false){
    var deputados = $(cssDeputados);
    var search = $(searchId)[0];

    $(searchId).on('input', function(){
      $(deputados).parent().css('display', 'none');
      var exp = new RegExp(search.value, 'i');
      for(var j = 0; j < deputados.length; j++){
        var depWrapper = deputados[j];
        var dep = $(depWrapper).text();
        if(dep.search(exp) != -1){
            $(depWrapper).parent().css('display', 'block');
        }
      }
    });
  }

  listaDeputados(depuM, searM);
  listaDeputados(depu, sear);

  //input desencadeia abertura do menu em mobile
  $("#searchMobile").on('focus', function(){
    if( !$('#navbarMobDeputado').hasClass('show')  ){
      $('#navbarMobDeputado').addClass('show')
      $('#navbarMobDeputado').addClass('collapsed');
    }  
  });

  $("#searchMobile").on('blur', function(){
    $('.deputados-mobile button').click();
    if( !$('#searchMobile').val() == "" ){
      $('#navbarMobDeputado').removeClass('show');
      $('#navbarMobDeputado').removeClass('collapsed');
    }  
  });

  
})();

(function(){
  $('.aside-desktop *').mouseover(
    function(){
      if(($(window).innerWidth() < 992) && ($(window).innerWidth() > 767)){
        $('.expand-menu').css('width', '230px');
        $('.deputados__item').css('display', 'block');
        console.log('foi o hover');
      }    
    });
  $('.aside-desktop *').mouseleave(
    function(){
      if(($(window).innerWidth() < 992) && ($(window).innerWidth() > 767)){
        $('.deputados__item').css('display', 'none');
        $('.expand-menu').css('width', '64px');
        console.log('saiu o hover');
      }    
    });

})();