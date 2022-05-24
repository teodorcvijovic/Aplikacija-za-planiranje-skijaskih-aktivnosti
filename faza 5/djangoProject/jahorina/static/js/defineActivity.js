$(document).ready(function() {

    $("#jahorinaMap").click(function (event) {
        let elem = document.getElementById("jahorinaMap");
        let imgX = 0
        let imgY = 0

        do {
            imgY += elem.offsetTop  || 0;
            imgX += elem.offsetLeft || 0;
            elem = elem.offsetParent;
        } while(elem);

        let width = $(this).width();
        let height = $(this).height();

        let x = event.pageX - imgX;
        let y = event.pageY - imgY;

        let percX = x / width;
        let percY = y / height;
        $("#coordx").val(percX);
        $("#coordy").val(percY);

        $('#poruka').html('<i class="fa-solid fa-check"></i>&nbsp;Lokacija je uspešno selektovana.')

        $('#marker')
            .css({
                'position': 'relative',
                'left': x,
                'top': y,
            })
            .show(700);
    })

    $(window).resize(function(){location.reload();});
})