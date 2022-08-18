---
layout: publication
title: "Meta-Reinforcement Learning for the Tuning of PI Controllers: An Offline Approach"
type: "paper"
order: 168
year: 2022
authors: "Daniel G. McClement, Nathan P. Lawrence, Johan U. Backström, Philip D. Loewen, Michael G. Forbes, R. Bhushan Gopaluni"
journal: "Journal of Process Control"
pdf: "2022J5_jpc_mcclement.pdf"
thumbnail: "2022J5_jpc_mcclement.png"
image: "/assets/thumbnails/2022J5_jpc_mcclement.png"
thumbnail_caption: >
  Appendix A2: Performance of the meta-RL agent with and without cost regularization.
description: "Meta-learning is a branch of machine learning which trains neural network models to synthesize a wide variety of data in order to rapidly solve new problems. In process control, many systems have similar and well-understood dynamics, which suggests it is feasible to create a generalizable controller through meta-learning. In this work, we formulate a meta reinforcement learning (meta-RL) control strategy that can be used to tune proportional- integral controllers. Our meta-RL agent has a recurrent structure that accumulates “context” to learn a system’s dynamics through a hidden state variable in closed-loop. This architec- ture enables the agent to automatically adapt to changes in the process dynamics. In tests reported here, the meta-RL agent was trained entirely offline on first order plus time delay systems, and produced excellent results on novel systems drawn from the same distribu- tion of process dynamics used for training. A key design element is the ability to leverage model-based information offline during training in simulated environments while maintaining a model-free policy structure for interacting with novel processes where there is uncertainty regarding the true process dynamics. Meta-learning is a promising approach for constructing sample-efficient intelligent controllers."
---

