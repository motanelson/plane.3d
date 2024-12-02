open Microsoft.Quantum.Intrinsic;
open Microsoft.Quantum.Measurement;

operation Main() : Unit {
    use q = Qubit[8];  // Reservar 8 qubits

    // Aplicar a porta H a cada qubit
    for b in 0 .. 7 {
        H(q[b]);
    }

    // Medir cada qubit e armazenar os resultados
    mutable intResult = 0; // Variável mutável para armazenar o número inteiro
    for b in 0 .. 7 {
        let result = Measure([PauliZ], [q[b]]); // Medir no Z-basis
        if result == One {
            set intResult += 1 <<< b; // Atualizar o inteiro usando deslocamento de bits
        }
        Reset(q[b]); // Resetar o qubit
    }

    // Imprimir o número inteiro resultante
    Message($"Número inteiro formado pelas medições: {intResult}");
}
