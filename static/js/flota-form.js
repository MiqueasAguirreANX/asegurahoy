function hideElem(elem) {
    elem.style.display = "none"
}
function showElem(elem) {
    elem.style.display = "block"
}

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

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

var page = 0
var cantidadAutos = 1
var autos = []

document.addEventListener("DOMContentLoaded", ()=>{


    const button = document.querySelector("#form-flota .form-button button")
    const form = document.getElementById("data-form")
    const input = document.querySelector("#form-flota #id_cantidad")
    const cantidadElems = document.getElementsByClassName("cantidad-elem")
    const autoElems = document.getElementsByClassName("auto-elem")

    for (let i = 0 ; i < autoElems.length ; i++) {
        hideElem(autoElems[i])
    };

    

    form.onsubmit = (ev)=>{
        ev.preventDefault()
    }
    button.onclick = (ev) => {
        cantidadAutos = parseInt(input.value)
        console.log("click")
        console.log(ev)
        console.log(page)
        console.log(cantidadAutos)
        if (page == 0) {
            
            for (let i = 0 ; i < autoElems.length ; i++) {
                showElem(autoElems[i])
            };
            for (let i = 0 ; i < cantidadElems.length ; i++) {
                hideElem(cantidadElems[i])
            };
            page += 1

        } else {
            if (page <= cantidadAutos) {
                const formData = new FormData(form);
                let data = {}
                for(let elem of formData.entries()) {
                    if (elem[0] == "csrfmiddlewaretoken" || elem[0] == "cantidad") {
                        continue
                    } else if (elem[0] == "año") {
                        data[elem[0]] = parseInt(elem[1])
                    } else {
                        data[elem[0]] = elem[1]
                    }
                    
                }
                autos.push(data)
                console.log(data)
                page += 1
                if (page > cantidadAutos) {
                    const data = JSON.stringify({
                        cantidad: cantidadAutos,
                        autos: autos,
                    })
                    console.log(data)
                    const csrftoken = getCookie('csrftoken');
                    fetch("/guardar-seguro/?tipo=flota", {
                        method: "POST",
                        body: data,
                        headers: {
                            'X-CSRFToken': csrftoken,
                            "Accept": 'application/json;charset=utf-8',
                            'Content-Type': 'application/json;charset=utf-8'
                        }
                    })
                    .then(res => res.json())
                    .then(res => {
                        console.log(res)
                        window.location.assign("/guardar-seguro/?tipo=flota")
                    })
                    .catch(err => console.log(err))
                }
            } else {
                button.setAttribute("disabled", true)
            }
        }
        
    }

    const tipo = "auto"
    const marcaSelect = document.getElementById("id_marca")
    
    
    let getModelosURL = "/get-modelos-by-marca/?tipo=" + tipo
    let getVersionesURL = "/get-versiones-by-modelo/?tipo=" + tipo

    let value = marcaSelect.options[marcaSelect.selectedIndex].value;

    if (value !== "OTRO") {
        fillModeloSelect(value, getModelosURL, getVersionesURL)
    } else {
        const modeloSelect = document.getElementById("id_modelo")
        while (modeloSelect.firstChild) {
            modeloSelect.removeChild(modeloSelect.firstChild);
        }
        console.log(modeloSelect)
        modeloSelect.appendChild(createOption("OTRO", "OTRO"))
        const versionSelect = document.getElementById("id_version")
        while (versionSelect.firstChild) {
            versionSelect.removeChild(versionSelect.firstChild);
        }
        versionSelect.appendChild(createOption("-", "-"))
    }
    marcaSelect.onchange = (event)=>{
        const versionSelect = document.getElementById("id_version")
        while (versionSelect.firstChild) {
            versionSelect.removeChild(versionSelect.firstChild);
        }
        versionSelect.appendChild(createOption("-", "-"))
        const marcaValue = marcaSelect.options[marcaSelect.selectedIndex].value;
        fillModeloSelect(marcaValue, getModelosURL, getVersionesURL)
    }
})