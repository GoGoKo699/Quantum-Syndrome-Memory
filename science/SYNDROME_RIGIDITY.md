# Rigidity under sublinear homomorphism advice

## Theorem

Fix a finite abelian label group $G$, an iid law $p$, and a finite pure-record ensemble $\mathcal E=\lbrace p_x,|f_x\rangle\rbrace _{x\in G}$. Before processing the records, the detector receives $H=A_nX^n$, where $A_n:G^n\to K_n$ is a predetermined group homomorphism and

$$
\ell_n=\log_2|\mathrm{im}A_n|=o(n).
$$

The detector may apply an arbitrary $H$-controlled collective operation and retain unlimited classical data $C$ and a register $Q$ satisfying $\log_2\dim Q\le m_n$. Let $G_{\mathcal E}$ be the [no-advice frontier](MODEL_AND_FRONTIER.md). Uniformly in the memory budget for this *fixed* source,

$$
\boxed{I(X^n;H,C,Q)\ \le\
nG_{\mathcal E}(m_n/n)+o(n).}
$$

Ignoring $H$ attains the reverse asymptotic inequality at each memory rate. The conclusion includes all memory budgets, from a fully measured detector to one that preserves the whole average record. It does not assume sparse checks, an efficient syndrome decoder, or a product record measurement.

The proof uses an information-theoretic sampling operation *on an auxiliary Gram state*. It is a converse device, not a proposed detector circuit.

## Syndrome pinching and phase twirling

The source Gram state is

$$
\rho=\sum_{x,x'}\sqrt{p_xp_{x'}}
\langle f_{x'}|f_x\rangle|x\rangle\langle x'|.
$$

Write $P_h=\sum_{x^n:A_nx^n=h}|x^n\rangle\langle x^n|$. The pure ensemble with the syndrome appended as an orthogonal classical flag has Gram state

$$
\sigma_n=\sum_hP_h\rho^{\otimes n}P_h.
$$

The syndrome's information is included *once*: for any record processor, the relevant label–output information is $I(X^n;H,C,Q)$, and the pure-ensemble mixed-roof representation applies to $\sigma_n$.

Let $V_n$ be the annihilator of $\ker A_n$ in the character group of $G^n$. Then $|V_n|=|\mathrm{im}A_n|$. For a character $b$ of $G$, let $Z_b$ be its diagonal unitary in the label basis and $\rho_b=Z_b\rho Z_b^\dagger$. Fourier orthogonality gives the exact identity

$$
\boxed{\sigma_n=\frac1{|V_n|}\sum_{v\in V_n}
\bigotimes_{i=1}^{n}\rho_{v_i}.}
$$

Indeed, the average kills a matrix element $|x^n\rangle\langle x'^n|$ precisely when some character in $V_n$ distinguishes $x^n-x'^n$, which is equivalent to $A_nx^n\ne A_nx'^n$. Thus a syndrome creates a mixture of at most $2^{\ell_n}$ *product phase patterns*. This exact product-orbit representation is where the homomorphism assumption enters.

## Learn the orbit on sacrificed sites

Only the local state $\rho_b$ matters, so quotient characters by the stabilizer $K=\lbrace b:\rho_b=\rho\rbrace $. If the orbit has one element, $\rho$ is diagonal and there is no coherence to protect. Otherwise choose a fixed finite rank-one informationally complete POVM on the single-site Gram space. It gives distinct distributions $P_b$ on distinct orbit states. Since the orbit is finite, its least pairwise Hellinger separation is positive:

$$
\kappa=\min_{\rho_b\ne\rho_c}
\left(1-\sum_y\sqrt{P_b(y)P_c(y)}\right)>0.
$$

Select $k$ sites uniformly *without replacement*, measure the chosen Gram sites destructively, and take the maximum-likelihood $v\in V_n$ from their outcomes. Call it $\hat v$; ties may be broken arbitrarily. Let $D(v,w)$ count positions with inequivalent local orbit states and put $d=D(v,w)/n$. Conditional on a sampled subset with $r$ positions where $v,w$ differ, the Bhattacharyya bound on the likelihood error is at most $(1-\kappa)^r$. Averaging over the hypergeometric sample, Maclaurin's inequality for elementary symmetric means gives

$$
\Pr[\text{likelihood}(w)\ge\text{likelihood}(v)\mid v]
\le (1-d\kappa)^k\le e^{-kd\kappa}.
$$

There are at most $2^{\ell_n}$ competitors. A union bound, including likelihood ties, yields

$$
\Pr[D(v,\hat v)>\varepsilon n]
\le\min\lbrace 1,2^{\ell_n}e^{-k\kappa\varepsilon}\rbrace .
$$

Integrating this tail gives, for $\eta_n=\min\lbrace 1,(\ell_n\ln2+1)/(k\kappa)\rbrace $,

$$
\mathbb E[D(v,\hat v)]\le n\eta_n.
$$

The expectation includes the posterior average after the sampling transcript. Errors on unmeasured sites are no more numerous. The use of elementary symmetric means avoids a false independence assumption about sampling without replacement.

## Coherence potential for every memory price

For $0\le t\le1$, define $g_t$ and its mixed-decomposition convex roof $J_t$ as in the [frontier page](MODEL_AND_FRONTIER.md):

$$
g_t(\tau)=S(\Delta\tau)-tS(\tau),\qquad
J_t(\tau)=\inf_{\tau=\sum_jq_j\tau_j}\sum_jq_j g_t(\tau_j).
$$

The following properties hold in arbitrary finite dimensions.

**Strong superadditivity.** For a bipartite state $\tau_{AB}$, measure $A$ in its label basis, producing $U$ and conditional states $\tau_{B|u}$. The diagonal chain rule and data processing of conditional entropy imply

$$
g_t(\tau_{AB})\ge g_t(\tau_A)+
\sum_u p_u g_t(\tau_{B|u})
\ge J_t(\tau_A)+J_t(\tau_B).
$$

Apply this to every component of a mixed decomposition and use convexity on the marginals. Hence $J_t(\tau_{AB})\ge J_t(\tau_A)+J_t(\tau_B)$; product decompositions show equality on products.

**Strong monotonicity for incoherent operations.** An efficient, single-Kraus incoherent instrument satisfies strong monotonicity of $C_r$ and $\sum_jp_jS(\tau_j)\le S(\tau)$. The latter follows by purifying the input: the conditional output entropy equals a conditional reference entropy, whose average is bounded by concavity. Since $g_t=C_r+(1-t)S$, $g_t$ is strongly monotone. Apply this inequality to an optimal mixed decomposition and use the induced decompositions of each output to obtain

$$
J_t(\tau)\ge\sum_jp_j J_t(\tau_j).
$$

A destructive rank-one measurement has Kraus operators $|j\rangle\langle\phi_j|$, with at most one nonzero row, and so is incoherent. The sampled measurements, classical transcript, disposal of the sampled systems, and diagonal corrections $Z_{\hat v_i}^\dagger$ all qualify. No coherent storage is hidden in this proof operation.

**Uniform local continuity.** At fixed one-letter dimension $d$, $J_t$ has a continuity modulus $\mu_d(u)\to0$ for half trace distance $u\to0$, *uniformly* in $t\in[0,1]$. To see this, choose nearby purifications by Uhlmann's theorem, apply to both the instrument realizing a nearly optimal mixed decomposition, and bound the resulting conditional entropies $S(\Delta R|C)-tS(R|C)$. The bounds depend on $\dim R=d$, not the number of outcomes; repeat in the opposite direction. A standard, deliberately loose choice is $2f_d(\min\lbrace 1,\sqrt{2u}\rbrace )$, capped at $\log_2d$, where

$$
f_d(v)=2v\log_2d+(1+v)h_2\left(\frac{v}{1+v}\right).
$$

After estimating $v$, correct every unsampled site by $Z_{\hat v_i}^\dagger$. Its conditional marginal equals $\rho$ when the orbit symbol is correct. If $e_i$ is the posterior probability of an inequivalent estimate, its half trace distance from $\rho$ is at most $e_i$. Strong monotonicity, superadditivity, continuity, and Markov's inequality give

$$
J_t(\sigma_n)\ge(n-k)J_t(\rho)-
n\left[\mu_d(\sqrt{\eta_n})+\sqrt{\eta_n}\log_2d\right].
$$

For example, take $k=\lceil\sqrt{n(\ell_n+1)}\rceil$; for all sufficiently large $n$ it is strictly below $n$. As $\ell_n=o(n)$, both $k/n$ and $\eta_n$ tend to zero. Since $0\le J_t(\rho)\le\log_2d$, this proves

$$
\inf_{0\le t\le1}\big[J_t(\sigma_n)-nJ_t(\rho)\big]\ge-o(n).
$$

For any permitted syndrome-controlled processor the actual $Q$ has $I(X^n;Q|H,C)\le m_n$. Applying the support bound to the syndrome-augmented pure ensemble,

$$
I(X^n;H,C,Q)\le nH(p)-J_t(\sigma_n)+(1-t)m_n.
$$

Minimizing over $t\in[0,1]$ and using the no-advice support formula proves the theorem. The zero-memory accessible-information result alone would give only a coarse bound at positive memory; the entire family $J_t$ is what retains the shape of the frontier.

## Binary finite-block bound

For $G=\mathbb Z_2$, let $0<p<1$, $0<s=|\langle f_0|f_1\rangle|<1$, and let the syndrome matrix have rank $L$. Put

$$
a_{\max}=2\sqrt{p(1-p)},\quad a=a_{\max}s,\quad
C(a)=h_2\left(\frac{1+\sqrt{1-a^2}}2\right),\quad
\kappa_a=1-\sqrt{1-a^2}.
$$

Put $b=2p-1$. The two local orbit states are $\rho_{\pm a}=(I+bZ\pm aX)/2$, in the Gram label basis, and $Z\rho_aZ=\rho_{-a}$. An $X$-basis measurement reads their phase through a binary symmetric channel with success probability $(1+a)/2$, hence the displayed $\kappa_a$. The estimate from the previous section becomes

$$
\mathbb E[D/n]\le
\min\left(1,\frac{L\ln2+1}{k\kappa_a}\right).
$$

At a fixed diagonal $p$, $x\mapsto J_t(\rho_x)$ is even and convex. The pure endpoint $x=a_{\max}$ has value $h_2(p)$, while $J_t\ge0$. A supporting slope at $a$ is therefore no greater than $h_2(p)/(a_{\max}-a)$, uniformly in $t$. Correcting with posterior phase-error probability $e$ loses at most $B_\star e$, where

$$
B_\star=\frac{2a h_2(p)}{a_{\max}-a}
=\frac{2s h_2(p)}{1-s}.
$$

Consequently, **for every** $1\le k\le n$, every syndrome-controlled collective processor, and every $m\ge0$,

$$
\boxed{I(X^n;H,C,Q)
\le nG_{\mathcal E}(m/n)+kC(a)
+\frac{B_\star n(L\ln2+1)}{k\kappa_a}.}
$$

When $L=o(n)$, selecting $k$ on the order of $\sqrt{n(L+1)}$ yields the stated $O_{p,s}(\sqrt{n(L+1)})$ correction. Constants are fixed-source constants; $B_\star$ diverges as $s\to1$. The $s=0,1$ endpoints can be handled directly.

At $m=0$, the sharper coherence-of-formation tangent is available. Set

$$
B_a=2aC'(a),\qquad
C'(a)=\frac{a \mathrm{atanh}\sqrt{1-a^2}}
{\sqrt{1-a^2}\ln2},\qquad B_a\le\frac2{\ln2}.
$$

Then the same finite bound holds with $B_\star$ replaced by $B_a$, and its no-advice term is $nI_{\rm acc}$. This also proves directly that sublinear early linear checks cannot unlock extensive *classical* accessible information from this iid source. The homogeneous finite-alphabet theorem is stronger because it holds for all coherent-memory budgets.

## Scope of the proof

The twirl identity requires a predetermined homomorphism. The orbit-learning constants require a fixed finite source; they need not be uniform for ensembles approaching singular overlaps as $n$ changes. Adaptive checks, arbitrary nonlinear advice, correlated or mixed flags, and quantum feedback from later data remain separate questions. These qualifications are part of the theorem, not mere implementation caveats. See [interpretation](INTERPRETATION.md) and [attribution](../references/RELATED_WORK.md).
