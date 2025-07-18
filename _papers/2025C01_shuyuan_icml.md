---
layout: "publication"
title: "Empowering Neural Networks with Control and Planning Abilities"
type: "conference"
order: 214
year: 2025
authors: "Shuyuan Wang, Philip D. Loewen, Michael Forbes, Bhushan Gopaluni, Wei Pan"
journal: "Poster session, Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)"
pdf: "2025C01_shuyuan_icml.pdf"
thumbnail: "2025C01_shuyuan_icml.gif"
url: "https://icml.cc/virtual/2025/poster/44176"
image: "/assets/thumbnails/2025C01_shuyuan_icml.gif"
code: "https://github.com/josef-w/Differentiable-iLQR"
thumbnail_caption: "Rocket landing demo."
description: While differentiable control has emerged as a powerful paradigm combining model-free flex- ibility with model-based efficiency, the iterative Linear Quadratic Regulator (iLQR) remains un- derexplored as a differentiable component. The scalability of differentiating through extended it- erations and horizons poses significant challenges, hindering iLQR from being an effective differen- tiable controller. This paper introduces DiLQR, a framework that facilitates differentiation through iLQR, allowing it to serve as a trainable and dif- ferentiable module, either as or within a neural network. A novel aspect of this framework is the analytical solution that it provides for the gradient of an iLQR controller through implicit differenti- ation, which ensures a constant backward cost re- gardless of iteration, while producing an accurate gradient. We evaluate our framework on imitation tasks on famous control benchmarks. Our analyti- cal method demonstrates superior computational performance, achieving up to 128x speedup and a minimum of 21x speedup compared to auto- matic differentiation. Our method also demon- strates superior learning performance (106x) com- pared to traditional neural network policies and better model loss with differentiable controllers that lack exact analytical gradients. Furthermore, we integrate our module into a larger network with visual inputs to demonstrate the capacity of our method for high-dimensional, fully end-to- end tasks. Codes can be found on the project homepage https://sites.google.com/view/dilqr/.
---