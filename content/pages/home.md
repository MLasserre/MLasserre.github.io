Title: Research
Date: 2022-05-30 00:58
Author: Marvin Lasserre
<!--Subtitle: Ph.D in computer science-->
<!--URL:-->
<!--save_as: index.html-->
<!--status: hidden-->

# Subject

My research work focuses on the use of copula theory for learning **non-parametric
continuous Bayesian networks**. In particular, we have proposed several algorithms
(see my publications) for learning the structure of a Copula Bayesian Network (CBN).
These algorithms are all available in the OTaGrUM plugin for OpenTURNS which makes
use of the graphical models implemented in aGrUM.

Recently, we are trying to implement inference algorithms for CBNs.
We have some interesting results that still wait to be published.
Stay tuned if you want to know more about it 😉.

More generally, I have interest in the following subjects:  

 - Bayesian networks,
 - Probabilistic graphical models,
 - Copula theory,
 - Information theory,
 - Independence testing,
 - Reasoning with uncertainties,
 - Knowledge representation,
 - Probability theory,
 - Statistics (Bayesian and classic),
 - Artificial intelligence,
 - Machine learning.

# What are Bayesian networks ?

A Bayesian network is a structure that allows to encode the independences of
a multivariate probability distribution through an acyclic directed graph:
the nodes of the graph represent the random variables while the arcs
represent the dependencies.
To each node of the graph, a conditional probability of distribution (CPD) is
associated. The joint distribution can then be written as the product of these
CPD.
In addition to facilitating the visualization of dependencies, the use of the graph
allows the implementation of efficient algorithms for model selection (learning) and
prediction (inference). Bayesian networks are at the interface of several fields
such as statistics, artificial intelligence and information theory.

# What are copulas ?

Copula theory, through the use of Sklar's theorem, allows to decompose a
multivariate distribution into a copula function and a set of univariate marginal
distributions.
The copula function encodes the dependence relations between the random variables
while the marginals encode their individual behavior.

# What are Copula Bayesian Networks ?

Copula Bayesian networks,
[introduced by Gal Elidan in
2010](https://www.semanticscholar.org/paper/Copula-Bayesian-Networks-Elidan/a27f18a60ca61c7a997e87589bf13930493da139),
are Bayesian networks whose conditional probability distributions are parameterized
by copula functions.
This allows: more freedom for modelisation, to remove the marginal behavior of the
random variables for the structure learning and to have a coherent model between
structure learning (test independences) and the parameter learning.
In our case, we use the empirical Bernstein copula which is a non-parametric estimation
of the copula from a data set.

# Contributions to open source projects

- [**OTaGrUM**](https://openturns.github.io/otagrum/master/index.html),
*main contributor*: The otagrum module links Bayesian networks built
with aGrUM to distributions defined with OpenTURNS. Among other things, it allows
to learn and manipulate Copula Bayesian networks. parameterized by local conditional copula
functions for each node ([Copula Bayesian Network]()).

- [**aGrUM**](https://agrum.gitlab.io/), *secondary contributor*:
aGrUM is a C++ library for graphical models.
It is designed to easily
build applications using graphical models such as such as Bayesian networks,
influence diagrams, decision trees, GAI networks or Markov decision processes.
pyAgrum is a Python wrapper for the aGrUM C++ library (using the SWIG interface
generator).

# Miscellaneous

- **2022**: Co-organizer of the first
[aGrUM/pyAgrum Users Day](https://agrum.gitlab.io/pages/apud22.html).
- **2022-....**: Community manager for aGrUM/pyAgrum on
[Linkedin](https://linkedin.com/company/pyagrum).
