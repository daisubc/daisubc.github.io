---
layout: publication
title: Meta-Reinforcement Learning for Adaptive Control of Second Order Systems
type: conference
order: 171
year: 2022
authors: Daniel G. McClement, Nathan P. Lawrence, Michael G. Forbes, Philip D. Loewen, Johan U. Backström, R. Bhushan Gopaluni
journal: In Proceedings of the 7th International Symposium on Advanced Control of Industrial Processes (AdCONIP)
pdf: "2022C5_AdCONIP_McClement.pdf"
thumbnail: "2022C5_AdCONIP_McClement.png"
image: "/assets/thumbnails/2022C5_AdCONIP_McClement.png"
video: "https://vimeo.com/743323651"
thumbnail_caption: >
  Fig 2. The structure of the RL agent. The control policy used online is shown in the grey box while the critic used during offline training is shown in green.
description: Meta-learning is a branch of machine learning which aims to synthesize data from a distribution of related tasks to efficiently solve new ones. In process control, many systems have similar and well-understood dynamics, which suggests it is feasible to create a generalizable controller through meta-learning. In this work, we formulate a meta reinforcement learning (meta-RL) control strategy that takes advantage of known, offline information for training, such as a model structure. The meta-RL agent is trained over a distribution of model parameters, rather than a single model, enabling the agent to automatically adapt to changes in the process dynamics while maintaining performance. A key design element is the ability to leverage model-based information offline during training, while maintaining a model-free policy structure for interacting with new environments. Our previous work has demonstrated how this approach can be applied to the industrially-relevant problem of tuning proportional-integral controllers to control first order processes. In this work, we briefly reintroduce our methodology and demonstrate how it can be extended to proportional-integral-derivative controllers and second order systems.
---

