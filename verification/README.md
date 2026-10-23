# Structural verification

Run from the repository root:

    python3 verification/check_structure.py

The standard-library script deterministically compares every matrix element of the binary syndrome pinching with the character twirl for a five-site example; exhaustively sums a sampled maximum-likelihood phase estimate for a separate eight-site example and checks a nontrivial tail-integral bound; and checks the endpoints and monotonicity of the inherited binary frontier. It exits nonzero if an identity or bound fails.

These small-block checks are reproducible illustrations. They do **not** numerically optimize a coherence convex roof, prove the asymptotic theorem, verify the novelty assessment, or replace the analytical and primary-source arguments in [science](../science/README.md).
