import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;

operation Main() : Unit {
    use q = Qubit();
    let i = M(q);

    

    // Imprimir o resultado da medição
    Message($"{i}");
}
