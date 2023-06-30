from itertools import cycle, islice

import numpy as np
import scipy.sparse as sp

from constrained_composite_site import *

config, groups, dofs, ops, labels, coeffs, basis = load_dofs_and_basis()

quarks = groups["quark"]
rishons = groups["rishon"]
flavors = config["quark"]["indices"]["flavor"]
colors = config["quark"]["indices"]["color"]
rishon_reps = dict(zip(config["rishon"]["basis"], config["rishon"]["qnums"]))
cycle_colors = [islice(cycle(colors), i, None) for i in range(len(colors))]


# region quantum numbers


@extend_by_linearity
def get_qnums(label):
    """returns: (R rishon, L rishon, u quarks, d quarks)"""
    ilabel = iter(label.split(maxsplit=3))
    next(ilabel)  # discard coeff
    lnk = tuple(rishon_reps[next(ilabel)[-1]] for _ in rishons)
    mat = next(ilabel, "")
    mat = tuple(mat.count(f) for f in flavors)
    return [lnk + mat]


basis_qnums = [list(set(get_qnums(lbl))) for lbl in labels]
basis_qnums = np.squeeze(basis_qnums)

# endregion

# region off-diagonal operators


hopping_ops = {
    f"{f}{r}_hc": linsum(*(compose(ops[f + c], hc(ops[r + c])) for c in colors))
    for r in rishons
    for f in flavors
}

liquid_ops = {}
# deuteron
liquid_ops["uuuddd"] = compose(*(ops[q] for q in quarks))
# delta ++ & -
liquid_ops |= {f * 3: compose(*(ops[f + c] for c in colors)) for f in flavors}
# proton & neutron
liquid_ops |= {
    fs: linsum(*(compose(*(ops[f + c] for f, c in zip(fs, cs))) for cs in cycle_colors))
    for fs in ("uud", "udd")
}

# endregion

# region matrix elements

diag_mels = dict(zip(("Rlnk", "Llnk", "Nu", "Nd"), basis_qnums))
diag_mels |= {
    "Nlnk": np.count_nonzero(basis_qnums[..., :2], 1),
    "JW": 1 - 2 * (basis_qnums[..., 2:].sum(1) % 2),
}
diag_mels |= {f * 2: basis_qnums[..., 2 + i] for i, f in enumerate(flavors)}
diag_mels |= {
    r * 2: np.exp(1.0j * 2 / 3 * np.pi * basis_qnums[..., i])
    for i, r in enumerate(rishons)
}
diag_mels |= {r * 2 + "_hc": diag_mels[r * 2].conj() for r in rishons}
diag_mels = {k: sp.diags(d) for k, d in diag_mels.items()}

hopping_mels = {k: matrix_elems(op, basis) for k, op in hopping_ops.items()}
hopping_mels |= {
    r + f + "_hc": hopping_mels[f + r + "_hc"].transpose().conjugate()
    for r in rishons
    for f in flavors
}

liquid_mels = {k: matrix_elems(op, basis) for k, op in liquid_ops.items()}

# endregion

dump_ops(diag_mels | hopping_mels | liquid_mels)
