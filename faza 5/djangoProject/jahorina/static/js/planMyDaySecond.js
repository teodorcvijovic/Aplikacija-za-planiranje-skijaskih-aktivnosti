$(document).ready(function() {

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

    addListeners()
})