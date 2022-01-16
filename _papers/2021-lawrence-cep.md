---
layout: publication
title: "Deep Reinforcement Learning with Shallow Controllers: An Experimental Application to PID Tuning"
type: "paper"
order: 159
year: 2021
authors: "Nathan P. Lawrence, Michael G. Forbes, Philip D. Loewen, Daniel G. McClement, Johan U. Backström, R. Bhushan Gopaluni"
journal: "Control Engineering Practice"
pdf: "2021J6_Lawrence_CEP.pdf"
thumbnail: "lawrence_cep_2021.jpg"
image: "/assets/thumbnails/lawrence_cep_2021.jpg"
external_url: "https://www.sciencedirect.com/science/article/pii/S0967066121002963?dgcid=author"
description: "Deep reinforcement learning (RL) is an optimization-driven framework for producing control strategies for general dynamical systems without explicit reliance on process models. Good results have been reported in simulation. Here we demonstrate the challenges in implementing a state of the art deep RL algorithm on a real physical system. Aspects include the interplay between software and existing hardware; experiment design and sample efficiency; training subject to input constraints; and interpretability of the algorithm and control law. At the core of our approach is the use of a PID controller as the trainable RL policy. In addition to its simplicity, this approach has several appealing features: No additional hardware needs to be added to the control system, since a PID controller can easily be implemented through a standard programmable logic controller; the control law can easily be initialized in a 'safe' region of the parameter space; and the final product—a well-tuned PID controller—has a form that practitioners can reason about and deploy with confidence."
---
