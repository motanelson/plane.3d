import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;

operation Main() : Unit {
    struct str {
        s : String,
        ss : String
    }
    let i =  str($"ssss", $"*****");

    

    // Imprimir o resultado da medição
    Message($"{i.s}");
}
