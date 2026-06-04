from pathlib import Path

# Project name
PROJECT_NAME = "brain-tumor-segmentation-pipeline"

# Files and folders to create
files = [
    # src
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_preprocessing.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",

    # pipelines
    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/pipeline/predict_pipeline.py",

    # utils
    "src/utils/__init__.py",
    "src/utils/common.py",

    # config
    "config/config.yaml",
    "config/params.yaml",

    # data
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",

    # artifacts
    "artifacts/models/.gitkeep",
    "artifacts/reports/.gitkeep",
    "artifacts/predictions/.gitkeep",

    # notebooks
    "notebooks/eda.ipynb",
    "notebooks/exp_notebook.ipynb",

    # api
    "api/main.py",

    # app
    "app/app.py",

    # tests
    "tests/__init__.py",
    "tests/test_api.py",

    # ci/cd
    ".github/workflows/ci.yml",
    ".github/workflows/retrain.yml",
    ".github/workflows/deploy.yml",

    # root files
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    "dvc.yaml",
]

for file in files:
    path = Path(file)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
        print(f"Created: {path}")

print(f"\n{PROJECT_NAME} initialized successfully.")