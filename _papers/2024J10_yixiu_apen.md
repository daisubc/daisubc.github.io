---
layout: "publication"
title: "Long Short-Term Memory Network with Transfer Learning for Lithium-ion Battery Capacity Fade and Cycle Life Prediction"
type: "paper"
order: 189
year: 2023
external_url: "https://www.sciencedirect.com/science/article/abs/pii/S0306261923010243"
authors: "Yixiu Wang, Jiangong Zhu, Liang Cao, Bhushan Gopaluni, Yankai Cao"
journal: "Applied Energy"
pdf: "2024J10_yixiu_apen.pdf"
thumbnail: "2024J10_yixiu_apen.png"
image: "/assets/thumbnails/2024J10_yixiu_apen.png"
thumbnail_caption: "Figure 5: Flowchart of transfer learning."
description: "Machine Learning (ML) is a promising technique for battery health estimation and prediction. However, with more and more types of batteries entering the market, building an ML model from scratch for each new battery requires collecting a large amount of data, which is very expensive and time-consuming. This paper proposes a transfer learning approach to reduce the amount of data that needs to be recollected for a new battery. The key idea is to train an ML model for a new battery of interest (i.e., target battery) with a limited amount of data by transferring the knowledge contained in a well-studied battery (i.e., source battery) with sufficient data. We illustrate this approach using two types of batteries, i.e., the battery with Li0.86Ni0.86Co0.11Al0.03O2-based positive electrode (NCA battery, source battery) and the battery with Li0.84Ni0.83Co0.11Mn0.07O2-based positive electrode (NCM battery, target battery), which have similar degradation patterns but dramatically different cycle life. Specifically, we first pre-train a long shortterm memory (LSTM) network, using cycling data of 20 NCA cells at 25 ◦C and at 45 ◦C, to predict the following capacity fade based on the previous capacity sequence. Then, to make the model applicable to NCM cells, we employ the transfer learning method to retrain the model, using cycling data of only 2 NCM cells at 25 ◦C, and propose a two-stage approach to further improve the model performance. The proposed two-stage model can predict the cycle life of NCM cells at 45 ◦C using the capacities of the first 13 cycles and obtain a cycle life root-mean-squared-error (RMSE) of 25.23 cycles and a capacity trajectory RMSE of 17.80 mAh (0.51 %)."
---