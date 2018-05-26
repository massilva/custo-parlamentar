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
    dados_placeholder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],
    canvas_width = $('.wrapper-itens-graficos > svg').width(),
    canvas_height = $('.wrapper-itens-graficos > svg').height();


function desenhaChart(dados){

  var grupo_bar = canvas.selectAll('.grupo-bar')
    .data(dados)
    .enter()
    .append('g')
      .attr('class', 'grupo-bar');

  var yScale = d3.scaleLinear()
    .domain([0, d3.max(dados)])
    .range([0, ((height - 40 ) * 0.95)]);

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
      })
  grupo_bar
    .append('rect')
      .attr('class', 'data-chart')
      .attr('width', '25px')
      .attr('fill', '#818EA7')
      .attr('rx','5')
      .attr('height', 20)
      .attr('y', function(){
        return canvas_height - 20;
      })
      .attr('x', function(d, i){
        return ((i+1) * (canvas_width / 12) -  (canvas_width / 12));
      });


  // var adicionaGraph = grupo_bar
  //   .append('rect')
  //   .attr('class', 'data-chart')
  //   .attr('width', '25px')
  //   .attr('fill', '#818EA7')
  //   .attr('rx','5')
  //   .attr('height', function(d, i){
  //     return yScale(d);
  //   })
  //   .attr('y', function(d){
  //     return canvas_height - 10 - yScale(d);
  //   })
  //   .attr('x', function(d, i){
  //     return ((i+1) * (canvas_width / 12) -  (canvas_width / 12));
  //   })
  //   .attr('data-title', function(d){
  //     return(d);
  //   });

  // $('[data-title]').parent().hover(function(){
  //   console.log( $(this).find('[data-title]').data('title') );
  // });
}

function updateChart(dados){

  var dadosMentirinha = [50, 60, 34, 56, 78, 12, 90, 43, 56, 76, 60, 54];
  var yScale = d3.scaleLinear()
    .domain([0, d3.max(dadosMentirinha)])
    .range([0, ((height - 40 ) * 0.95)]);

  var graficos = d3.selectAll('.data-chart').transition().duration(5000);

  graficos.attr('height', function(d, i){
    return yScale(d);
  })

  console.log(dados);

}

function getData(){

  var slug_deputado, ano, url_processada;

  url_processada = window.location.href.toString().split(window.location.host)[1].split('/');
  slug_deputado = url_processada[1];

  if (url_processada.length >= 2) {
    ano = url_processada[2];
  }

  return $.ajax({
    type : "POST",
    url: '/ajax/dadosdeputados',
    cache : false,
    data: {'slug_deputado': slug_deputado, 'ano': ano},
    dataType: 'json',
    contentType: "application/x-www-form-urlencoded",
    beforeSend: function(xhr, settings) {
      $('.header-main__wrap__load').addClass('loading');
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });
}

//get data to init graph
var cat = 10;
var ano = new Date();
ano = ano.getFullYear() - 1;
var dadosBrutos;
$(document).ready(function(){
  getData()
    .done( function(data){
      dadosBrutos = treatData(data['dados_brutos'], ano, cat);
      $('.header-main__wrap__load').removeClass('loading');
    })
    .fail( function(data){
      $('.header-main__wrap__load').removeClass('loading');
    });

});

function treatData(data, ano, cat){
  var dadosSelecionados = [];
  for(var i = 1; i <= 12; i++){
    data[ano][i][cat] == 'None'? dadosSelecionados.push(0) : dadosSelecionados.push(parseInt(data[ano][i][cat]));
  }
  desenhaChart(dadosSelecionados);
  console.log(data);
  return(data);
}


$('[data-ano]').click(function(dadosBrutos){
  ano = $(this).data('ano');
  console.log(dadosBrutos);
  updateChart(dadosBrutos);
  //treatData(dadosBrutos, ano, cat);
});
