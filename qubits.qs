import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;

operation Main() : Unit {
    use q = Qubit();
    X(q);
    
    let i = M(q);
    Reset(q);
    

    // Imprimir o resultado da medição
    Message($"{i}");
}
