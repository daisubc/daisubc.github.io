---
layout: "publication"
title: "A modular framework for stabilizing deep reinforcement learning control"
type: "conference"
order: 179
year: 2023
arxiv: https://arxiv.org/abs/2304.03422
external_url: "https://www.sciencedirect.com/science/article/pii/S240589632301306X"
authors: "Nathan P. Lawrence, Philip D. Loewen, Shuyuan Wang, Michael G. Forbes, R. Bhushan Gopaluni"
journal: "In Proceedings of the 22nd IFAC World Congress"
pdf: "2023C4_lawrence_ifac.pdf"
thumbnail: "2023C4_lawrence_ifac.png"
video: https://vimeo.com/849890644
image: "/assets/thumbnails/2023C4_lawrence_ifac.png"
slides: "2023C4_lawrence_ifac_slides.pdf"
thumbnail_caption: "Fig. 1: A stable nonlinear parameter Q interacts with its environment; collected input-output trajectories are used to construct a Hankel matrix. These ingredients yield an equivalent realization of the Youla-Kuˇcera parameterization."
description: "We propose a framework for the design of feedback controllers that combines the optimization-driven and model-free advantages of deep reinforcement learning with the stability guarantees provided by using the Youla-Kuˇcera parameterization to define the search domain. Recent advances in behavioral systems allow us to construct a data-driven internal model; this enables an alternative realization of the Youla-Kuˇcera parameterization based entirely on input-output exploration data. Using a neural network to express a parameterized set of nonlinear stable operators enables seamless integration with standard deep learning libraries. We demonstrate the approach on a realistic simulation of a two-tank system."
---