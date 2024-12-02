@EntryPoint()
operation Main() : Unit {
    // Chamar a operação para medir e retornar o qubit
    let (measurementResult) = AllocateTwoQubits();

    // Imprimir o resultado da medição
    Message($"{measurementResult}");
}
operation AllocateTwoQubits() : (Qubit) {
    use qubit1 = Qubit() {
        return qubit1;
    }
}
