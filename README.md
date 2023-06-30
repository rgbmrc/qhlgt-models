# QHLGT-models: Quantum Hamiltonian Lattice Gauge Theory models database

Collection of input data for simulating HLGT models within TN or quantum technologies [1].

In studing HLGT, we typically:
- adopt the Kogut-Susskind formulation of LGT, with staggered fermion matter fields [2]
- truncate the gauge links in irreps space [3]
- split each link in two rishon semilinks [4] and impose local Abelian link constraints [5]
- fuse each matter site with its neigbouring semilinks and use the gauge invariant states as local computational basis [6]

For each model we generally include the local operator algebra of the computational site and, eventually, resources that allow its generation.
The recipe and the included data might vary on a model to model basis. 
Check model specific README files more details.

[1] 
[Simulating lattice gauge theories within quantum technologies](https://doi.org/10.1140/epjd/e2020-100571-8)

[2] 
[Hamiltonian formulation of Wilson's lattice gauge theories](https://doi.org/10.1103/PhysRevD.11.395)

[3] 
[Formulation of lattice gauge theories for quantum simulations](https://doi.org/10.1103/PhysRevD.91.054506)

[4] 
[QCD as a quantum link model](https://doi.org/10.1103/PhysRevD.60.094502)

[5] 
[Lattice gauge tensor networks](https://doi.org/10.1088/1367-2630/16/10/103015), 

[6]
[Finite-density phase diagram of a (1+1)-d non-abelian lattice gauge theory with tensor networks](https://doi.org/10.22331/q-2017-04-25-9), 
[Tensor network simulation of an SU(3) lattice gauge theory in 1D](https://doi.org/10.1103/PhysRevD.100.074512)


## Content:

### Software:
- `constrained-composite-site`: 

    computational spaces constructed as a subspace of the tensor product of some "elementary" degrees of freedom
    
    ```
    pip install ./constrained-composite-site
    ```


## Attribution:
If you use any of the content in this repository, please credit the authors according to the instructions in model specific README or CITATION files.
