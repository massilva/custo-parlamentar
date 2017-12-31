$(function(){
  $('.anos > .badge-pill').click(function(){
    var ano = $(this).attr('id');
    var slug_deputado = window.location.href.toString().split(window.location.host)[1];

    console.log($(this).attr('id'));
    console.log(slug_deputado);
    var url_req = 'dados'+slug_deputado+'/'+ano;

    $.ajax({
      type : "POST",
      url: url_req,
      cache : false,
      processData: false,
      contentType: false,
      success: function(){
        console.log('Supimpa!')
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
