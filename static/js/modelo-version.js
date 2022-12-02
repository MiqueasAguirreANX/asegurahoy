function fillModeloSelect(marca, modelosURL, versionURL)  {
    let modeloSelect = document.getElementById("id_modelo")
    while (modeloSelect.firstChild) {
        modeloSelect.removeChild(modeloSelect.firstChild);
    }
    modeloSelect.appendChild(createOption("OTRO", "OTRO"))

    

    fetch(modelosURL+"&marca="+marca)
    .then(result => result.json())
    .then(result => {
        console.log(result)
        result.data.forEach(element => {
            modeloSelect.appendChild(createOption(element.modelo, element.modelo))
        });
        modeloSelect.onchange = (event)=>{
            let modeloVal = modeloSelect.options[modeloSelect.selectedIndex].value;
            fillVersionSelect(marca, modeloVal, versionURL)
        }
    })
}

function fillVersionSelect(marca, modelo, versionURL)  {
    let versionSelect = document.getElementById("id_version")
    while (versionSelect.firstChild) {
        versionSelect.removeChild(versionSelect.firstChild);
    }
    versionSelect.appendChild(createOption("-", "-"))
    

    fetch(versionURL+"&marca="+marca+"&modelo="+modelo)
        .then(result => result.json())
        .then(result => {
            console.log(result)
            result.data.forEach(element => {
                versionSelect.appendChild(createOption(element.version, element.version))
            });
        })
}

function createOption(val, label) {
    let option = document.createElement("option");
    option.setAttribute("value", val);
    option.innerHTML = label;
    return option;
}

window.addEventListener('DOMContentLoaded', (event) => {
    let dataForm = document.getElementById("data-form")
    const tipo = dataForm.getAttribute("tipo")
    let marcaSelect = document.getElementById("id_marca")
    
    
    let getModelosURL = "/get-modelos-by-marca/?tipo=" + tipo
    let getVersionesURL = "/get-versiones-by-modelo/?tipo=" + tipo

    let value = marcaSelect.options[marcaSelect.selectedIndex].value;

    if (value !== "OTRO") {
        fillModeloSelect(value, getModelosURL, getVersionesURL)
    } else {
        let modeloSelect = document.getElementById("id_modelo")
        while (modeloSelect.firstChild) {
            modeloSelect.removeChild(modeloSelect.firstChild);
        }
        modeloSelect.appendChild(createOption("OTRO", "OTRO"))
        let versionSelect = document.getElementById("id_version")
        while (versionSelect.firstChild) {
            versionSelect.removeChild(versionSelect.firstChild);
        }
        versionSelect.appendChild(createOption("-", "-"))
    }
    marcaSelect.onchange = (event)=>{
        let versionSelect = document.getElementById("id_version")
        while (versionSelect.firstChild) {
            versionSelect.removeChild(versionSelect.firstChild);
        }
        versionSelect.appendChild(createOption("-", "-"))
        let marcaValue = marcaSelect.options[marcaSelect.selectedIndex].value;
        fillModeloSelect(marcaValue, getModelosURL, getVersionesURL)
    }
});