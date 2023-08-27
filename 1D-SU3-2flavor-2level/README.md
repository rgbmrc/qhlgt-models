# 1D-SU3-2flavor-2level

(1+1)D 2-flavor hardcore QCD

## Model:
- SU(3)-color gauge group
- gauge rishon space: **1** (singlet) ⊕ **3** (fundamental) ⊕ **3*** (antifundamental)
- 6 staggered fermion matter fields (flavors: up, down; colors: r, g, b)

The gauge space is truncated to the preimage of the 2 lowest Casimir eigenvalues (0, 4/3).

## Requirements:
- python distribution with scipy
- only to generate the operators from scratch: [constrained-composite-site](../constrained-composite-site/) (provided as a submodule)

## Contents:
- `out/*.npz` local operators (one file for each), load via [scipy.sparse.load_npz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.load_npz.html)
- `res/` input files to generate the operators via `python generate.py`
    - `dofs.yaml` matter and rishon degrees of fredoom and their operator algebras
    - `basis.txt` gauge invariant local computational basis

## Attribution:
