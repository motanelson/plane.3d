import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;

operation Main() : Unit {
   struct Ints {
        num1 : Int ,
        num2 : Int
       
    }
    let i =  Ints(5,7) ;

    

    // Imprimir o resultado da medição
    Message($"{i.num1}");
}
