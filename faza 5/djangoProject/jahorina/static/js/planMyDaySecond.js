// teodor & filip

$(document).ready(function() {

    // active listeners for every label tag on the map
    function addListeners() {
        let activities = $("[name='a_id']")
        let a_ids = ","

        activities.each(function() {
            $(this).click(function () {

                let a_id = $(this).val()
                let field = $('#a_id_list')
                if (a_ids.includes("," + a_id + ","))
                {
                    let tmp = a_ids.split("," + a_id + ",")
                    if (tmp.length == 1) {
                        a_ids = "," + tmp[1]
                    }
                    else a_ids = tmp[0] + "," + tmp[1]
                }
                else
                {
                    a_ids += a_id + ","
                }
                field.val(a_ids)
            })
        })
    }

    // for positioning pins on the map
    function positionPins() {
        let pins = $(".pinLabel")
        pins.each(function (event) {
            let arr = this.id.split(" ");
            let regex = /\d\.\d*/;

            let percX = regex.exec(arr[0])[0];
            let percY = regex.exec(arr[1])[0];

            let width = $("#jahorinaPict").width();
            let height = $("#jahorinaPict").height();

            let elem = document.getElementById("jahorinaPict");
            let imgX = elem.offsetTop
            let imgY = elem.offsetLeft

            // koliko levo i dole u odnosu na POCETAK SLIKE
            let x = Math.round(width * percX) + imgX - 50;
            let y = Math.round(height * percY) + imgY ;

            $(this).css({
                "position": "absolute",
                "left": x,
                "top": y
            })
        })
    }

    // for toggling whether the pin is clicked or not
    $(".pinLabel").click(function () {
        $(this).toggleClass("pinClicked");
    })

    // to reposition pins when you resize the window
    $(window).resize(function(){location.reload();});


    // ************ MAIN ************
    addListeners()
    positionPins()
})