---
layout: "publication"
title: "Guiding Reinforcement Learning with Incomplete System Dynamics"
type: "conference"
order: 207
year: 2024
authors: "Shuyuan Wang, Jingliang Duan, Nathan P. Lawrence, Philip D. Loewen, Michael G. Forbes, R. Bhushan Gopaluni, Lixian Zhang"
journal: "In Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2024, To Appear)"
arxiv: https://arxiv.org/abs/2410.16821
pdf: "2024C07_shuyuan_iros.pdf"
video: https://www.youtube.com/watch?v=xGNNiuYJh98
presentation: https://www.youtube.com/watch?v=8rhK_ne4vqk
thumbnail: "2024C07_shuyuan_iros.png"
image: "/assets/thumbnails/2024C07_shuyuan_iros.png"
thumbnail_caption: "Figure 2: Schematic diagram for our policy network with partial knowledge control module inside."
description: "Model-free reinforcement learning (RL) is inher- ently a reactive method, operating under the assumption that it starts with no prior knowledge of the system and entirely depends on trial-and-error for learning. This approach faces several challenges, such as poor sample efficiency, generaliza- tion, and the need for well-designed reward functions to guide learning effectively. On the other hand, controllers based on complete system dynamics do not require data. This paper addresses the intermediate situation where there is not enough model information for complete controller design, but there is enough to suggest that a model-free approach is not the best approach either. By carefully decoupling known and unknown information about the system dynamics, we obtain an embedded controller guided by our partial model and thus improve the learning efficiency of an RL-enhanced approach. A modular design allows us to deploy mainstream RL algorithms to refine the policy. Simulation results show that our method signifi- cantly improves sample efficiency compared with standard RL methods on continuous control tasks, and also offers enhanced performance over traditional control approaches. Experiments on a real ground vehicle also validate the performance of our method, including generalization and robustness."
---