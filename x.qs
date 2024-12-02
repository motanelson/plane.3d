import Std.Logical.Xor;
import Std.Convert.IntAsBigInt;
import Std.Convert.IntAsDouble;
import Std.Math;
operation Main() : Unit {
    use q = Qubit[4];
    X(q[0]);
    X(q[1]);
    Controlled X([q[0],q[1]],q[2]);
    let i = M(q[2]);
    Reset(q[0]);
    Reset(q[1]);
    Reset(q[2]);
    Reset(q[3]);

    // Imprimir o resultado da medição
    Message($"{i}");
}
