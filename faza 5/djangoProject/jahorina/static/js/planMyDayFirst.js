
function changeRangeLabel(input) {
    if(input == 0) {
        document.getElementById("rangeLabel")
            .innerHTML = "<h5><i class=\"fa-solid fa-person-skiing-nordic\"></i> Ne baš najbolje...</h5>";
    }
    else if(input == 1) {
        document.getElementById("rangeLabel")
            .innerHTML = "<h5><i class=\"fa-solid fa-person-skiing\"></i> Dosta dobro</h5>";
    }
    else {
        document.getElementById("rangeLabel")
            .innerHTML = "<h5><i class=\"fa-solid fa-person-snowboarding\"></i> Najjače na svijet!</h5>";
    }
}
