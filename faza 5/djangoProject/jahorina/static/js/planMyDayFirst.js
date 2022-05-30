
function changeRangeLabel(input) {
    if(input == 0) {
        document.getElementById("rangeLabel")
            .innerHTML = "<h5><i class=\"fa-solid fa-person-skiing-nordic\"></i> Početnik </h5>";
    }
    else if(input == 1) {
        document.getElementById("rangeLabel")
            .innerHTML = "<h5><i class=\"fa-solid fa-person-skiing\"></i> Rekreativac </h5>";
    }
    else {
        document.getElementById("rangeLabel")
            .innerHTML = "<h5><i class=\"fa-solid fa-person-snowboarding\"></i> Napredan skijaš</h5>";
    }
}
