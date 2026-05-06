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

Due to size constraints, datasets are not included in this repository.

They can be downloaded automatically using:

```bash
pip install requests
python code/data/download_datasets.py
```

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

## Third-Party Assets and Licenses

This project builds upon several existing open-source libraries and publicly available datasets.

### Libraries and Frameworks

- **MOA (Massive Online Analysis)**  
  Website: https://moa.cms.waikato.ac.nz/  
  License: GNU General Public License (GPL v3)  
  Citation: Bifet et al., 2010

- **CapyMOA**  
  Website: https://capymoa.org/  
  License: Apache License 2.0  
  Citation: Gomes et al., 2025

- **NumPy**  
  License: BSD 3-Clause License

- **PyTorch**  
  License: BSD-style license

- **JPype1**  
  License: Apache License 2.0

### Datasets

The benchmark uses publicly available datasets and synthetic generators.

- **INSECTS Dataset**  
  Source: Souza et al., 2020  
  License: please refer to the original dataset distribution and terms of use.

- **Synthetic Streams**
  - AgrawalGenerator
  - RandomTreeGenerator
  - SEA Generator
  - SineGenerator

These generators are distributed through MOA and follow the corresponding MOA licensing terms.

Datasets are not redistributed in this repository. Users should download them from the original sources and comply with their respective licenses and terms of use.

## Citation
