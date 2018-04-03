'use strict';

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          //Does this cookie string begin with the name we want?
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
  //these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var scopeGraph = (function(){
  var ano = $('#gastos_deputado').data('ano');
  var id_antiga = '';
  var id_atual = 10;
  if(typeof ano == 'undefined' ){
    var ano = new Date();
    ano = ano.getFullYear();
  }

  var canvas = d3.select('.wrapper-itens-graficos')
    .append('svg')
      .attr('width', '100%')
      .attr('height', '95%')
      .attr('style', 'margin-top: 10px');

  var width = $('.wrapper-itens-graficos').innerWidth(),
      height = $('.wrapper-itens-graficos').innerHeight(),
      dados_placeholder = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],
      canvas_width = $('.wrapper-itens-graficos > svg').width(),
      canvas_height = $('.wrapper-itens-graficos > svg').height();
      
  var grupo_bar = canvas.selectAll('.grupo-bar')
  .data(dados_placeholder)
  .enter()
  .append('g')
    .attr('class', 'grupo-bar');

  grupo_bar
  .append('rect')
  .attr('class', 'wrapper-chart')
    .attr('fill', '#DFECF4')
    .attr('width', '25px')
    .attr('height', function(){
      return canvas_height - 15;
    })
    .attr('x', function(d, i){
      return ((i+1) * (canvas_width / 12) - (canvas_width / 12));
    });

  function desenhaChart(dados_utilizados){

    console.log(dados_utilizados);
  
    var yScale = d3.scaleLinear()
      .domain([0, d3.max(dados_utilizados)])
      .range([0, ((height - 40 ) * 0.95)]); 

    var adicionaGraph = grupo_bar
      .append('rect')
        .attr('class', 'data-chart')
        .attr('width', '25px')
        .attr('fill', '#818EA7')
        .attr('rx','5')
        .attr('height', function(d){
          return yScale(d);
        })
        .attr('y', function(d){
          return canvas_height - 10 - yScale(d);
        })
        .attr('x', function(d, i){
          return ((i+1) * (canvas_width / 12) -  (canvas_width / 12));
        });

        return{
          quadro: canvas,
          adicionaGraph: adicionaGraph
        }
  }
  
    canvas = desenhaChart(dados_placeholder);
  
  $(function(){

      function reloadGraph(ano){
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
            // console.log(response['gastos']);
            // //charts(response['gastos'], ano);
            // console.log('ano');
            // console.log(ano);
            charts(response['gastos'], ano, id_atual); 
          },
          error: function(response){
            $('.wrapper-load-graficos').removeClass('loading');
          }
        });
      }

      // dados ajax
      $('.anos > .badge-pill')
        .click(function(e, ano){
            console.log('anoooo');
            console.log(ano);
            var ano = $(this).data("ano");
            reloadGraph(ano);
          }
        );
  
      // Categorias
      $('.dropdown-menu .dropdown-item')
        .click(function(e, ano){ 
          // console.log(ano);
          if(typeof id_atual == 'undefined' ){
            var id_atual = 10;
          }
          var id_atual = $($(this).find('.dropdown-menu__item__title').parent()[0]).data("categoria");
          $('.categoria-atual').text($(this).find('.dropdown-menu__item__title').text());
          $('.categoria-atual').addClass(id_atual).removeClass(id_antiga);
          id_antiga = id_atual;
          if(typeof ano == 'undefined' ){
            var ano = new Date();
            ano = ano.getFullYear();
            // var ano = 2017;
          }
          charts(dados, ano, id_atual); 
        })
    });
     
    function charts(data, ano, categoria){
      console.log("Data: "+ dados + " Ano:" + ano + " Categoria: "+ categoria);
      var dados_selecionados = [];
      for(var i = 1; i <=12; i++){
        data[i][categoria] == 'None'? dados_selecionados.push(0) : dados_selecionados.push(parseFloat(data[i][categoria]));
      }
      desenhaChart(dados_selecionados)
    }

    return{
      quadro: canvas
    }

  })(dados, year);
  

    