# Benchmarking Framework for Concept Drift Detectors

This repository contains the **reference implementation** of the experimental framework presented in the paper:

**Yet Another Concept Drift Benchmark? A Principled Framework for Evaluating Drift Detectors**  
*NeurIPS E&D 2026 (under review)*

The goal of this framework is to provide a **reproducible and principled benchmark** for evaluating **concept drift detectors** under well-defined alarm semantics and evaluation metrics.

---

## What is Included

- A unified **benchmarking pipeline** for concept drift detectors
- Formal **alarm semantics** (true detections, false alarms, repeated alarms)
- Normalized **evaluation metrics** and composite scores
- A **deterministic reference learner** (Sliding Heatmap) used as a controlled performance observer
- Integration with **MOA** and **CapyMOA**

> Sliding Heatmap is **not** proposed as a state-of-the-art classifier.  
> It is intentionally simple and deterministic, and is used only to ensure observability.

---

## Repository Structure

code:
- moa_java/ # Java (MOA) components
- python/ # Python wrappers and evaluation
- experiments/ # Benchmark scripts
- requirements.txt

---

## Dataset Setup

For double-blind review, datasets are not redistributed from an author-owned archive. Please download them from the original public sources following the instructions in `code/data/download_datasets.py`. A permanent archival mirror will be added after the review period.

---

## Setup

### 1. Create Environment

```bash
conda create -n shm-paper -c conda-forge python=3.11 -y
conda activate shm-paper
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Building Java Components

```bash
cd code/moa_java
mvn -DskipTests clean package
cp target/slidingheatmap-moa-1.0.0.jar ../python/slidingheatmap_capymoa/jars/
```

## Python Dependencies
```makefile
numpy==1.26.4
torch==2.2.2
capymoa==0.12.0
jpype1==1.6.0
typing_extensions
```

## License

This repository is released under the MIT License.

The project depends on third-party libraries and frameworks, including MOA and CapyMOA, which are distributed under their own respective licenses. Users must comply with the license terms of these external dependencies.

## Third-Party Assets and Licenses

This project builds upon several existing open-source libraries and publicly available datasets.

### Libraries and Frameworks

- **MOA (Massive Online Analysis)**  
  Website: https://moa.cms.waikato.ac.nz/  
  License: GNU General Public License (GPL v3)  
  Citation: Bifet, Albert, et al. Machine learning for data streams: with practical examples in MOA. MIT press, 2023.

- **CapyMOA**  
  Website: https://capymoa.org/  
  License: Apache License 2.0  
  Citation: Gomes, Heitor Murilo, et al. "Capymoa: Efficient machine learning for data streams in python." arXiv preprint arXiv:2502.07432 (2025).

- **NumPy**  
  License: BSD 3-Clause License

- **PyTorch**  
  License: BSD-style license

- **JPype1**  
  License: Apache License 2.0

### Datasets

The benchmark uses publicly available datasets and synthetic generators.

- **INSECTS Dataset**  
  License: please refer to the original dataset distribution and terms of use.  
  Citation: Souza, Vinicius MA, et al. "Challenges in benchmarking stream learning algorithms with real-world data." Data Mining and Knowledge Discovery 34.6 (2020): 1805-1858.  

- **Synthetic Streams**
  - AgrawalGenerator
  - RandomTreeGenerator
  - SEA Generator
  - SineGenerator

These generators are distributed through MOA and follow the corresponding MOA licensing terms.

Datasets are not redistributed in this repository. Users should download them from the original sources and comply with their respective licenses and terms of use.

## Citation
