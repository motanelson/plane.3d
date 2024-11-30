operation Main() : Unit {
    // Chamar a operação para medir e retornar o qubit
    let (measurementResult, _) = MeasureAndReturnQubit();

    // Imprimir o resultado da medição
    Message("Resultado da medição: ", measurementResult);
}
operation MeasureAndReturnQubit() : (Result, Qubit) {
    // Alocar um qubit
    using (qubit = Qubit()) {
        // Medir o qubit
        let result = M(qubit);

        // Retornar o resultado da medição e o qubit (embora ele já esteja marcado para liberação)
        return (result, qubit);
    }
}
