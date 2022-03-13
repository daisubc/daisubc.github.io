---
layout: publication
title: "Process Monitoring using Domain-Adversarial Probabilistic Principal Component Analysis: A Transfer Learning Framework"
type: "paper"
order: 162
year: 2022
authors: "Atefeh Daemi, Bhushan Gopaluni, Biao Huang"
journal: "IEEE Transactions on Industrial Informatics"
pdf: "2022J1_Daemi_TII.pdf"
thumbnail: "2022J1_Daemi_TII.png"
thumbnail_caption: >
  Figure 1: A schematic of the proposed method for process monitoring via transfer learning.
image: "/assets/thumbnails/2022J1_Daemi_TII.png"
description: "Probabilistic principal component analysis (PPCA) is a feature extraction method that has been widely used in the field of process monitoring. However, PPCA assumes that training and testing data are drawn from the same input feature space with the same distributions. This assumption is not valid for complex processes that exhibit multiple operating modes and generate data with different distributions. We propose a novel transfer learning approach to monitoring processes with data from multiple distributions. To this end, we introduce a novel extension of probabilistic principal component analysis, which is we refer to as the Domain Adversarial Probabilistic Principal Component Analysis (DAPPCA). DAPPCA algorithm auto- matically learns feature representations that are relevant across different operational modes. The algorithm extracts the most informative shared fault features and improves the accuracy of the fault detection model in a new operating mode using the knowledge transferred from previously known modes. The parameters of DAPPCA are estimated using a variational inference approach, and the monitoring statistics are calculated using the proposed model. We demonstrate the efficacy and real-time applicability of the proposed method with simulated and industrial examples."
---