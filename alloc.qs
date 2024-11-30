operation AllocateTwoQubits() : (Qubit, Qubit) {
    using ((qubit1, qubit2) = (Qubit(), Qubit())) {
        return (qubit1, qubit2);
    }
}
