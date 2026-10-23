# Pure records and the no-advice memory frontier

## Temporal interface

Let $X_1,\ldots,X_n$ be iid labels with law $p$ on a fixed finite alphabet. Conditional on $X^n=x^n$, the detector receives the pure product record $|f_{x^n}\rangle=\bigotimes_i|f_{x_i}\rangle$. It processes all records collectively before later data-dependent decoding. It may retain a classical register $C$ of unrestricted size and a quantum register $Q$ with the *hard* dimension constraint

$$
\log_2\dim Q\le m.
$$

Any other persistent coherent register, including a share of preshared entanglement used across this cut, is counted in $Q$. Arbitrary temporary preprocessing workspace is allowed. Encoders of the later quantum data do not know the error labels. The source is fixed as $n$ grows; no statement uniform in an $n$-dependent ensemble is intended.

The no-advice operational quantity is

$$
G_{\mathcal E}(M)=\sup\limsup_{n\to\infty}\frac1n I(X^n;CQ),
\qquad \log_2\dim Q\le nM.
$$

For a pure ensemble, let its Gram state in the label basis be

$$
\rho=\sum_{x,x'}\sqrt{p_xp_{x'}}\langle f_{x'}|f_x\rangle
|x\rangle\langle x'|,\qquad
\Delta\rho=\sum_xp_x|x\rangle\langle x|.
$$

Zero-probability letters are omitted. The Gram state has the same nonzero spectrum as the average record state. For a record instrument with an efficient outcome $c$, a corresponding mixed-state decomposition $\rho=\sum_c p_c\rho_c$ satisfies

$$
I(X;C)=H(p)-\sum_c p_c S(\Delta\rho_c),\qquad
I(X;Q|C)=\sum_c p_c S(\rho_c).
$$

The residual output states for each $x,c$ are pure. Any mixed-output instrument can be coherently dilated when deriving an information upper bound; the dilation's environment is **not** silently counted as free memory. The actual $Q$ separately satisfies $I(X;Q|C)\le\log_2\dim Q$.

## Mixed-roof support functions

For $0\le\eta\le1$, define a convex roof over *mixed* decompositions:

$$
g_\eta(\tau)=S(\Delta\tau)-\eta S(\tau),\qquad
J_\eta(\rho)=\inf_{\rho=\sum_c p_c\rho_c}
\sum_c p_c g_\eta(\rho_c).
$$

The endpoint $J_0=C_f$ is coherence of formation: refining to pure components cannot increase average diagonal entropy. The endpoint $J_1=C_r=S(\Delta\rho)-S(\rho)$ is relative entropy of coherence, which is already convex. For a fixed single-copy ensemble,

$$
\max_{\mathrm{instruments}}\lbrace I(X;C)+\eta I(X;Q|C)\rbrace 
=H(p)-J_\eta(\rho).
$$

Every mixed decomposition of $\rho$ is induced by an efficient instrument on a purification; a dilation bounds inefficient instruments. The no-advice frontier has the dual form

$$
G_{\mathcal E}(M)=\min_{0\le\eta\le1}
\left[H(p)-J_\eta(\rho)+(1-\eta)M\right].
$$

One derivation uses the one-copy instrument region and conditional Schumacher compression. If an efficient instrument yields $c=I(X;C)$ and $q=I(X;Q|C)$, product instruments and classical-outcome-controlled compression achieve $c+q$ with a common memory of dimension at most $2^{n(q+\epsilon)}$, up to vanishing error. Conversely, the [strong superadditivity and product equality](SYNDROME_RIGIDITY.md#coherence-potential-for-every-memory-price) $J_\eta(\rho^{\otimes n})=nJ_\eta(\rho)$ bound the support function of any collective instrument; its actual output separately obeys $I(X^n;Q|C)\le m$. Time sharing and convex duality give the display. Its support slopes lie in $[0,1]$: the curve is nondecreasing, concave, and $G(M)\le I_{\rm acc}(\mathcal E)+M$. Here the last bound follows from $I(X^n;C)\le nI_{\rm acc}(\mathcal E)$ for the iid no-advice source and $I(X^n;Q|C)\le m$; it does not assume quantum information is equivalent to an accessible classical measurement.

This baseline frontier is a reparametrization of Hsieh and Watanabe's quantum-helper source-compression region. The new question begins when early advice makes the label source conditional and correlated; one cannot simply apply the iid helper formula to each syndrome fiber.

## Binary example

For $p=\Pr(X=0)\in(0,1)$ and $s=|\langle f_0|f_1\rangle|\in(0,1)$, choose phases so the overlap is $s$, and put

$$
a=2\sqrt{p(1-p)}s,\qquad
\rho=p|0\rangle\langle0|+(1-p)|1\rangle\langle1|
+\frac a2\bigl(|0\rangle\langle1|+|1\rangle\langle0|\bigr),
\qquad
C(a)=h_2\left(\frac{1+\sqrt{1-a^2}}2\right).
$$

Then $I_{\rm acc}=h_2(p)-C(a)$. The average-record Holevo information is $\chi=S(\rho)$; for an irreducible nonorthogonal binary pair, full information needs $M=\chi$. A convenient parameterization of the inherited binary frontier uses $b=2p-1$, $a=2\sqrt{p(1-p)}s$, and $H_{\ast}(z)=h_2((1+z)/2)$. For $d\in[|b|,\sqrt{1-a^2}]$,

$$
M(d)=H_{\ast}\left(\sqrt{a^2+d^2}\right),\qquad
G_{\mathcal E}(M(d))=M(d)+1-H_{\ast}(d)-[1-h_2(p)].
$$

Equivalently, the flagged phase-channel rate at that memory is $R(d)=M(d)+1-H_{\ast}(d)$. At $M=0$, $G=I_{\rm acc}$; at $M=\chi$, $G=\chi$. This evaluation uses an inherited binary entropy concavity inequality (see [attribution](../references/RELATED_WORK.md)); it is not claimed as a new universal frontier.

### Proof dependencies

The one-letter mixed-decomposition representation is the helper-region input. The chain rule in $X_1,\ldots,X_n$ and concavity tensorize its converse for arbitrary collective processing. Conditional compression is used only for achievability and is not a free quantum side channel. The [syndrome proof](SYNDROME_RIGIDITY.md) bounds $J_\eta$ of the *pinched* $n$-copy Gram state uniformly in $\eta$, which is precisely what the whole-frontier extension needs.
