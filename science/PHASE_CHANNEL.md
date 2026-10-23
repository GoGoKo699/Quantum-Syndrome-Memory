# From record information to phase-error correction

## Flagged phase channel

For $n$ data qubits, let the classical phase-error string $X^n=x$ have product law $p_x$. A channel that passes the data and a possibly mixed processed record to the decoder has the form

$$
\mathcal T(\tau)=\sum_{x\in\{0,1\}^n}
p_x Z^x\tau Z^x\otimes\omega_x.
$$

The side states $\omega_x$ may be correlated, mixed, and include both the freely given syndrome $H$ and the retained $C,Q$. The early detector acts on records and $H$ alone: it does not interact with the unknown data state. The final decoder may use the data and all of $H,C,Q$.

Let $D=2^n$, $\bar\omega=\sum_xp_x\omega_x$, and $\Phi_x=(I\otimes Z^x)\Phi_D(I\otimes Z^x)$. The normalized Choi state is

$$
J_{\mathcal T}=\sum_xp_x\Phi_x\otimes\omega_x.
$$

The vectors $\Phi_x$ are orthogonal. Thus the coherent information of the maximally mixed data input is exactly

$$
I(A\rangle BW)_{J_{\mathcal T}}
=n-H(X^n)+\chi(\{p_x,\omega_x\}),
$$

where $\chi(\{p_x,\omega_x\})=S(\bar\omega)-\sum_xp_xS(\omega_x)=I(X^n;W)$. In the detector model $W=HCQ$.

## Converse for arbitrary data codes

This phase channel is covariant under data Pauli teleportation corrections (which act trivially on the side output). Its Choi state simulates the channel by teleportation. Compare it across the reference versus data-and-side-output cut with the separable state

$$
\zeta=\frac1D\sum_{j=0}^{D-1}|jj\rangle\langle jj|\otimes\bar\omega.
$$

On the maximally correlated data subspace, $\zeta$ is $I/D\otimes\bar\omega$, so

$$
D(J_{\mathcal T}\Vert\zeta)
=n-H(X^n)+I(X^n;W).
$$

Teleportation simulation and monotonicity of relative entropy of entanglement upper bound any quantum communication protocol using this block channel, including arbitrary CPTP encoders and decoders and even two-way classical assistance. More concretely, suppose a code transmits a $K$-dimensional logical system with entanglement fidelity at least $1-\epsilon$. Test the recovered state against $\Phi_K$; every separable comparison state passes that test with probability at most $1/K$. Binary relative entropy yields the weak finite-block converse

$$
\boxed{(1-\epsilon)\log_2K-h_2(\epsilon)
\le n-H(X^n)+I(X^n;W).}
$$

No unproved monotonicity of coherent information under an arbitrary encoding map is used here. The inequality is weak for finite $\epsilon$; it is not a strong-converse or fault-tolerance threshold.

The lower asymptotic rate follows from coherent-information coding on repeated copies of this fixed block channel. Equivalently, the channel is degradable: a Stinespring complement depends only on the input's computational diagonal, which the data output preserves. Measuring that diagonal and preparing the corresponding environment is a degrading channel. The matching upper bound above shows that, per use of the fixed block,

$$
Q(\mathcal T)=Q_{\leftrightarrow}(\mathcal T)
=n-H(X^n)+I(X^n;W).
$$

This capacity identity applies to commuting phase errors with the distinct orthogonal phase operators used here; it is not asserted for arbitrary noncommuting Pauli noise.

## The memory and syndrome bound

For the iid binary pure records of the [model](MODEL_AND_FRONTIER.md), an arbitrary rank-$L$ early linear syndrome is granted free to the detector *and again* to the final decoder. Its Gram-state twirl obeys the [finite-block rigidity theorem](SYNDROME_RIGIDITY.md#binary-finite-block-bound). Inserting it into the code converse, for every $1\le k\le n$,

$$
\boxed{\begin{aligned}
(1-\epsilon)\log_2K-h_2(\epsilon)
&\le n\left[1-h_2(p)+G_{\mathcal E}(m/n)\right]\\
&\quad+kC(a)
+\frac{B_\star n(L\ln2+1)}{k\kappa_a}.
\end{aligned}}
$$

Here $a=2\sqrt{p(1-p)}s$, $C(a)=h_2((1+\sqrt{1-a^2})/2)$, $\kappa_a=1-\sqrt{1-a^2}$, and $B_\star=2s\,h_2(p)/(1-s)$. The bound holds for arbitrary data encoding, joint flag processing, and final decoding, with a hard $m$-qubit persistent record memory.

If $L=o(n)$, the correction is $o(n)$ uniformly in $m$. Ignoring the free syndrome and using the no-advice record-compression and channel coding protocol achieves the original asymptotic quantum-transmission versus memory curve. Therefore sublinear *predetermined linear* early checks do not change that curve.

At $m=0$, the no-advice information is $I_{\rm acc}=h_2(p)-C(a)$; at sufficient coherent memory, the record Holevo information is $\chi=S(\rho)$. A fixed improvement over the zero-memory digitized rate cannot be obtained from a vanishing rate of early checks with vanishing coherent-memory rate in this model.

## What the genie means

The proof gives the detector and decoder the syndrome without charging for its extraction. It therefore proves an obstruction despite that advantage. It does not claim that a hardware syndrome is instantaneous, that a physical interface has the stipulated timing, or that conventional fault-tolerant QEC lacks $\Theta(n)$ checks. Any architecture-specific application must justify its causal memory cut and account for coherent ancillas, entanglement, data access, and extraction timing.
