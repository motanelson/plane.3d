import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;

operation Main() : Unit {
    use q = Qubit[2];
    H(q[0]);
    
    let i = M(q[0]);
    Reset(q[0]);
    

    // Imprimir o resultado da medição
    Message($"{i}");
}
