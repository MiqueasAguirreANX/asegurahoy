

window.addEventListener('DOMContentLoaded', (event) => {
    let acopladoCheck = document.getElementById("id_acoplado")
    document.getElementById("id_marca_modelo_acoplado").removeAttribute("required")
    document.getElementById("id_año_acoplado").removeAttribute("required")
    let acopladoDataChecks = document.querySelectorAll(".form-container .form-elem:has(#id_marca_modelo_acoplado),.form-container .form-elem:has(#id_año_acoplado)")
    acopladoDataChecks.forEach((val) => {
        val.style.display = "none"
    })
    acopladoCheck.onchange = (event) => {
        if (event.target.value === "Si") {
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