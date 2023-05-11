
window.addEventListener('DOMContentLoaded', (event) => {
    let acopladoCheck = document.getElementById("id_tipo_bici")
    document.getElementById("id_marca_modelo_bici").removeAttribute("required")
    document.getElementById("id_valor_bici").removeAttribute("required")
    let acopladoDataChecks = document.querySelectorAll(".form-container .form-elem:has(#id_marca_modelo_bici),.form-container .form-elem:has(#id_valor_bici)")
    acopladoDataChecks.forEach((val) => {
        val.style.display = "none"
    })
    acopladoCheck.onchange = (event) => {
        if (event.target.value === "SI") {
            acopladoDataChecks.forEach((val) => {
                val.style.display = "flex"
            })
        } else {
            acopladoDataChecks.forEach((val) => {
                val.style.display = "none"
            })
        }
    }
})

