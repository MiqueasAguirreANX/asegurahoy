
window.addEventListener('DOMContentLoaded', (event) => {
    let biciSelect = document.getElementById("bici-select")
    let monopatinElems = document.querySelectorAll(".monopatin-elem")
    let biciElems = document.querySelectorAll(".bici-elem")
    console.log(monopatinElems)
    console.log(biciElems)
    monopatinElems.forEach((val) => {
        val.style.display = "none"
    })

    biciSelect.onchange = (event) => {
        let tipo = biciSelect.options[biciSelect.selectedIndex].value;
        console.log(tipo)
        if (tipo === "bici") {
            monopatinElems.forEach((val) => {
                val.style.display = "none"
            })
            biciElems.forEach((val) => {
                val.style.display = "flex"
            })
        } else {
            biciElems.forEach((val) => {
                val.style.display = "none"
            })
            monopatinElems.forEach((val) => {
                val.style.display = "flex"
            })
        }
    }
})