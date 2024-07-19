---
layout: "publication"
title: "Deep Hankel matrices with random elements"
type: "conference"
order: 203
year: 2024
authors: "Nathan P. Lawrence, Philip D. Loewen, Shuyuan Wang, Michael G. Forbes, R. Bhushan Gopaluni"
journal: "In Proceedings of the 6th Annual Learning for Dynamics & Control Conference (L4DC)"
pdf: "2024C05_lawrence_l4dc.pdf"
thumbnail: "2024C05_lawrence_l4dc.png"
image: "/assets/thumbnails/2024C05_lawrence_l4dc.png"
thumbnail_caption: "Figure 1: For a fixed-size dataset, adjusting the depth of the input-output Hankel matrices dramatically improves self-consistency. Results are for L = 2, 5, 10, 20 and each color corresponds to 50 rollouts with different output noise instances but a fixed input sequence."
description: "Willems’ fundamental lemma enables a trajectory-based characterization of linear systems through data-based Hankel matrices. However, in the presence of measurement noise, we ask: Is this noisy Hankel-based model expressive enough to re-identify itself? In other words, we study the output prediction accuracy from recursively applying the same persistently exciting input sequence to the model. We find an asymptotic connection to this self-consistency question in terms of the amount of data. More importantly, we also connect this question to the depth (number of rows) of the Hankel model, showing the simple act of reconfiguring a finite dataset significantly improves accuracy. We apply these insights to find a parsimonious depth for LQR problems over the trajectory space."
---