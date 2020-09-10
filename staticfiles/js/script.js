$(document).ready(function() {
    $('#sidebarCollaps').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#content').toggleClass('active');
        $('#sidebarCollaps').toggleClass('change');
    });
});

$(window).scroll(function() {    
    var scroll = $(window).scrollTop();

    //>=, not <=
    if (scroll >= 1) {
        //clearHeader, not clearheader - caps H
        $("#sidebar").removeClass("active");
        $('#content').removeClass('active');
        $('#sidebarCollaps').removeClass('change');
    }
});

$('.carousel').carousel({
    interval: 2000
  })

  /*Upload File Name*/
  $('#inputGroupFile01').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#inputGroupFile01')[0].files[0].name;
    $(this).prev('label').text(file);
    $('#inputGroupFile01_chng').html(file)
  });

  $('#inputGroupFile02').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#inputGroupFile02')[0].files[0].name;
    $(this).prev('label').text(file);
    $('#inputGroupFile02_chng').html(file)
  });

  $('#Carousel_1').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#Carousel_1')[0].files[0].name;
    $(this).prev('label').text(file);
    $('#Carousel_1_chng').html(file)
  });

  $('#Carousel_2').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#Carousel_2')[0].files[0].name;
    $(this).prev('label').text(file);
    $('#Carousel_2_chng').html(file)
  });

  $('#Carousel_3').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#Carousel_3')[0].files[0].name;
    $(this).prev('label').text(file);
    $('#Carousel_3_chng').html(file)
  });

  function textAreaAdjust(element) {
    element.style.height = "1px";
    element.style.height = (25+element.scrollHeight)+"px";
  }
