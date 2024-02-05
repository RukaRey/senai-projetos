function calcular(){
    const peso = parseFloat(document.getElementById('peso').value)
    const altura= parseFloat(document.getElementById('altura').value)
    let result = peso/(altura**2)

    let estadao = document.getElementById('estadao')

    if (peso < 600 && peso > 20 && altura < 3 && altura > 0.50){
        if (result < 18.5) {
            estadao.textContent = "Abaixo do Peso"
        }
        else if (result > 18.5 && result < 24.9){
            estadao.textContent = "Peso normal"
            alert("Peso normal")
        }
        else if (result > 25.0 && result < 29.9){
            estadao.textContent = "Sobrepeso"
            alert("Sobrepeso")
        }
        else if (result > 30.0 && result < 34.9){
            estadao.textContent = "Obesidade grau I"
            alert("Obesidade grau I")
        }
        else if (result > 35.0 && result < 39.9){
            estadao.textContent = "Obesidade grau II"
            alert("Obesidade grau II")
        }
        else if (result > 40.0){
            estadao.textContent = "Obesidade grau III"
            alert("Obesidade grau III")
        }      
    }
}
