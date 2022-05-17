$(document).ready(function() {

    $("#jahorinaMap").click(function (event) {
        let realX = $(this).width();
        let realY = $(this).height();

        let x = event.pageX - this.offsetLeft;
        let y = event.pageY - this.offsetTop;

        let percX = x / realX;
        let percY = y / realY;
        $("#coordx").val(percX);
        $("#coordy").val(percY);

        $('#marker')
            .css('left', event.pageX - 10)
            .css('top', event.pageY - 28)
            .show(700);

    })
})