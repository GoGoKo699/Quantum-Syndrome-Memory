# Interpretation and boundaries

The theorem asks a temporal question: before the detector can use later data for decoding, how much quantum information must its nonorthogonal error records retain? A fixed, sublinear number of *predetermined linear* facts about the error labels can be supplied early for free. Those facts alter the conditional distribution and might in principle help a collective record measurement. For iid pure records, their product-character structure prevents an extensive improvement anywhere on the information versus coherent-memory curve.

The result is specific enough to be testable. In the binary example the fixed-source finite-block penalty is at most of order $\sqrt{n(L+1)}$; the ratio vanishes if $L/n\to0$. For commuting phase errors, this becomes a bound on arbitrary data codes, with the syndrome also available to the final decoder. The converse charges every coherent system that persists across the record-memory cut.

| Assumption | Why it matters |
| --- | --- |
| Fixed iid finite **pure** record ensemble | The Gram-state decomposition gives both the product phase orbit and the one-copy helper frontier. |
| Predetermined group homomorphism $A_n$ | Fourier pinching is a mixture of at most $\lvert\operatorname{im}A_n\rvert$ product character rotations. |
| $\log_2\lvert\operatorname{im}A_n\rvert=o(n)$ | A sublinear sample learns the orbit on almost all coordinates; positive-rate advice is a different problem. |
| Unlimited classical storage, hard quantum dimension | The theorem prices the persistent coherent register, not preprocessing gates, peak workspace, time, or classical computation. |
| No uncounted entanglement across the cut | Such a system could carry coherent information across the same interface. |
| Commuting phase errors for the channel corollary | Orthogonal phase-Bell labels give the exact channel relative-entropy expression. |

The theorem makes no claim about arbitrary nonlinear or adaptively chosen checks, correlated or mixed records, quantum feedback from the data, ensembles that change with block length, noncommuting error alphabets, or general QKD security. General information locking shows why merely counting classical advice bits would be insufficient in other settings. The proof instead uses the exact homomorphism twirl and the fixed product source. The physical consequence is conditional on an architecture realizing the stated early-information and storage boundary.

The no-advice frontier and coherence ingredients are inherited; [related work](../references/RELATED_WORK.md) lists their sources and the closest syndrome-disclosure discussion. A targeted source screen supports a provisional distinction for the stability theorem, but does not certify priority.
