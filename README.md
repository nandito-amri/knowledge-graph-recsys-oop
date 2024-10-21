
# Music Recommendation System Using Knowledge Graph

This research aims to develop a music recommendation system using a
knowledge graph to represent the relationships between users and music entities.
The knowledge graph is transformed into vectors through the TransM model, which
acts as the graph embedder. To tackle the cold-start problem, the knowledge graph
is supplemented with users' background information, while the Bounded-Greedy
Selection (BGS) algorithm is employed to address diversity issues. By utilizing
information in vector form, the system can calculate the similarity between entities, enabling it to generate recommendations.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DATASET_FOLDER_PATH`


## Installation

Set your environment variables.

```python
DATASET_FOLDER_PATH='<project-path>/database/datasets'
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all modules and packages.

```bash
pip install -r requirements.txt
```

Run the codes in `database` folder. These codes is used for data preparation.
```bash
python src/database
```

Run the codes in root `src` folder to execute this projects. 
```bash
python scr
```
    
## Authors

- [Nandito Fatoni Amri](https://www.github.com/nandito-amri): nandito.f.amri@gmai.com


## Features

- Graph Building
- Graph Embedding Using TransM
- Recommendation Module
- Diversity Module


## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

