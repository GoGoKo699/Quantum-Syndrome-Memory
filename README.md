# Quantum Syndrome Memory

**Can a few early syndrome bits replace a coherent quantum memory?** For a fixed iid source of pure, nonorthogonal error records, a detector may learn a predetermined linear syndrome before deciding what to preserve. It may retain unlimited classical data and at most $m$ qubits. The main result shows that an $o(n)$-bit syndrome leaves the *entire* asymptotic retained-information versus quantum-memory frontier unchanged, even when the detector processes all $n$ records jointly.

| Result | Scope | Reader route |
| --- | --- | --- |
| Homomorphism-advice rigidity | Fixed finite pure ensemble; iid labels in a finite abelian group; predetermined syndrome with $\log_2\lvert\mathrm{im}A_n\rvert=o(n)$ | [Theorem and proof](science/SYNDROME_RIGIDITY.md) |
| Quantitative binary bound | Binary prior $0<p<1$, fixed overlap $0<s<1$, rank $L$ checks; excess information $O_{p,s}(\sqrt{n(L+1)})$, uniformly over memory budgets | [Finite-block statement](science/SYNDROME_RIGIDITY.md#binary-finite-block-bound) |
| Phase-channel consequence | Commuting phase errors with pure records; arbitrary data encoders and decoders; free early and late access to the stipulated syndrome | [Channel and code converse](science/PHASE_CHANNEL.md) |

The theorem concerns a **temporal interface**: the detector sees the quantum records and the specified early checks before its persistent quantum memory is limited. Every coherent system crossing that interface counts toward the memory budget. The syndrome is granted as a free classical genie, so the converse does not presume an uncharged physical extraction circuit. In particular, this is not a general assertion about conventional QEC, which may have a linear number of checks.

## Read the science

1. [Model and the inherited no-advice frontier](science/MODEL_AND_FRONTIER.md)
2. [Syndrome rigidity and its proof](science/SYNDROME_RIGIDITY.md)
3. [Phase-channel translation and arbitrary-code converse](science/PHASE_CHANNEL.md)
4. [Interpretation, assumptions, and open boundaries](science/INTERPRETATION.md)
5. [Related work and attribution](references/RELATED_WORK.md)

The [scientific map](science/README.md) connects the claims and proof dependencies. The helper/source-compression frontier, coherence properties and entropy inequalities used below are attributed to their sources. The proposed contribution is the stability theorem under sublinear homomorphism advice, with its quantitative binary and channel consequences. The [checks](verification/README.md) reproduce finite-dimensional structural identities and numerical examples; they do not replace the analytical proof.

## Learn the result

The [30 understanding milestones](learning/MILESTONES.md) progress through background and preliminaries (M01–M12), then the project’s argument and interpretation (M13–M30). They are a common map of the science, independent of any reader’s prior knowledge or progress. The single educational anchor is John Watrous’s *The Theory of Quantum Information* (2018); the [Watrous bridge](learning/WATROUS_BRIDGE.md) selects relevant chapters, translates notation, and identifies the steps supplied by this project. Specialists can go directly to the [theorem and proof](science/SYNDROME_RIGIDITY.md).

## Status and use

This repository records an analytical research result at its stated assumptions. Its literature comparison is a focused primary-source screen, not an exhaustive priority certification. The model does not optimize arbitrary nonlinear or adaptive advice, mixed or correlated records, noncommuting errors, hardware thresholds, or peak circuit workspace.

The repository is available under the [MIT License](LICENSE).

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
