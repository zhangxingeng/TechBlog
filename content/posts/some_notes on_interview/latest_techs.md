---
date: 2024-05-24
title: "Notes on Latest ML Techs for ML Interviews"
---

- vector database: DB for vectors, function as a similarity search engine -- they are basically a memeory for a machine learning model.
  - fast retrieval of data using similarity search
  - Different types of search algorithms:
    - Approximate nearest neighbor search (ANN)?
    - Partitioning to reduce search space: KD-tree, Ball-tree, Voronoi diagram
    - Hashing based: LSH: close vectors likely to have same hash
    - Graph based: Navigable small world graph (close data are connected)
- LangChain: chaining