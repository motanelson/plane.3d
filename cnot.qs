import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;

operation Main() : Unit {
    use q = Qubit[2];
    CNOT(q[0],q[1]);
    
    let i = M(q[1]);
    Reset(q[0]);
    Reset(q[1]);

    // Imprimir o resultado da medição
    Message($"{i}");
}
