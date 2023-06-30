# 1D-SU3-2flavor-2level

(1+1)D 2-flavor maximally truncated QCD

## model:
- SU(3)-color gauge group
- gauge rishon space: **1** (singlet) ⊕ **3** (fundamental) ⊕ **3*** (antifundamental)
- 6 staggered fermion matter fields (flavors: up, down, colors: r, g, b)

## requirements:
- python distribution with scipy
- only to generate the operators from scratch: [constrained-composite-site](../constrained-composite-site/) (provided as a submodule)

## contents:
- `out/*.npz` local operators (one file for each), load via [scipy.sparse.load_npz](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.load_npz.html)
- `res/` input files to generate the operators via `python generate.py`
    - `dofs.yaml` matter and rishon degrees of fredoom and their operator algebras
    - `basis.txt` gauge invariant local computational basis

## attribution: