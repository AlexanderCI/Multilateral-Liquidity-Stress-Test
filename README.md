# Student Project: Multilateral Liquidity Risk Model

This is a simplified academic simulation I built using the stochastic modelling and probability concepts from my UofT coursework. 

The goal of this script is to look at how a multi-currency defence balance sheet (like the upcoming DSRB) might handle random shocks and currency devaluations and capital delays over a basic 30-day window (assume 30 days for now...)

### Important Assumptions:
* Uses a basic random normal distribution to simulate non-CAD cash pools fluctuating.
* Uses a binomial trial to model a 10% chance of an allied nation delaying their funding injections.
* Calculates the resulting LCR across 2,000 randomized simulation runs.

*NOTE: This is purely a simplified undergraduate research prototype built for learning purposes.*
