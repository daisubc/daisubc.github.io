---
layout: "publication"
title: "Empowering Neural Networks with Control and Planning Abilities"
type: "conference"
order: 208
year: 2024
authors: "Shuyuan Wang, Philip D Loewen, Bhushan Gopaluni, Michael Forbes"
journal: "In NeurIPS 2024 Workshop on Behavioral ML (non-archival)"
pdf: "2024C08_shuyuan_nips.pdf"
thumbnail: "2024C08_shuyuan_nips.png"
image: "/assets/thumbnails/2024C08_shuyuan_nips.png"
thumbnail_caption: "Figure 1: An overview of iLQR, and AutoDiff vs our proposed planner with implicit differentiation. As shown in the flowchart, autodiff must backpropagate through each layer of the LQR process, which leads to significantly increased memory usage to store intermediate gradients and computational load. In contrast, our proposed planner, using implicit differentiation, only needs to handle the final layer. This results in constant computational costs and memory usage, making our method much more efficient."
description: Learning effective behaviors requires both adaptability and structured planning, traditionally split between model-free and model-based methods. Differentiable control combines the strengths of both, but iLQR, a powerful nonlinear controller, lacks differentiability, limiting its use in end-to-end learning. Differentiating through extended iterations introduces scalability challenges, further hindering its application. We propose a framework that enables iLQR to function as a trainable and differentiable module, either as or within a neural network, by using implicit differentiation to compute accurate gradients with constant backward cost. On behavior imitation tasks across standard benchmarks, our method achieves up to 128x speedup (minimum 21x) over automatic differentiation and improves learning efficiency by 106x compared to conventional neural policies. This framework equips neural networks with control and planning abilities, bridging control theory and behavioral learning.
---