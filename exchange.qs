import Std.Logical.Xor;
import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;
import Std.Math;
operation Main() : Unit {
    use q = Qubit[2];
    X(q[1]);
    SWAP(q[1], q[0]);
    let i = M(q[0]);
    Reset(q[0]);
    Reset(q[1]);

    // Imprimir o resultado da medição
    Message($"{i}");
}
