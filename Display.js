class Display {
    constructor(displayValorAnterior, displayValorAtual) {
        this.displayValorAtual = displayValorAtual;
        this.displayValorAnterior = displayValorAnterior;
        this.calculador = new Calculadora();
        this.tipoOperacion = undefined;
        this.valorAtual = '';
        this.valorAnterior = '';
        this.sinais = {
            somar: '+',
            dividir: '÷',
            multiplicar: 'x',
            subtracao: '-', 
        }
    }

    apagar() {
        this.valorAtual = this.valorAtual.toString().slice(0,-1);
        this.imprimirValores();
    }

    apagarTudo() {
        this.valorAtual = '';
        this.valorAnterior = '';
        this.tipoOperacion = undefined;
        this.imprimirValores();
    }

    computar(tipo) {
        this.tipoOperacion !== 'igual' && this.calcular();
        this.tipoOperacion = tipo;
        this.valorAnterior = this.valorAtual || this.valorAnterior;
        this.valorAtual = '';
        this.imprimirValores();
    }

    addNumero(numero) {
        if(numero === '.' && this.valorAtual.includes('.')) return
        this.valorAtual = this.valorAtual.toString() + numero.toString();
        this.imprimirValores();
    }

    imprimirValores() {
        this.displayValorAtual.textContent = this.valorAtual;
        this.displayValorAnterior.textContent = `${this.valorAnterior} ${this.sinais[this.tipoOperacion] || ''}`;
    }

    calcular() {
        const valorAnterior = parseFloat(this.valorAnterior);
        const valorAtual = parseFloat(this.valorAtual);

        if( isNaN(valorAtual)  || isNaN(valorAnterior) ) return
        this.valorAtual = this.calculador[this.tipoOperacion](valorAnterior, valorAtual);
    }
}