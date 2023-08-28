programa {
  inclua biblioteca Matematica-->mat
    funcao inicio() {
      real n,bin
      real arredonda
      escreva("Escolha seu número.\n")
      leia(n)
      real nI=n
      enquanto(n>=2){
      n=n/2
      }
      faca{
        bin=n%2
        n*=2
        arredonda = mat.arredondar(bin,0)
        se(bin>=1.000000001){
          bin=1
        }se(bin>=0.000000001 e bin<=0.999999999){
          bin=0
        }
        escreva(bin," ")
      }
    enquanto(n<=nI)
  }
}
