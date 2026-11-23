# ML + NLP Challenge — Predicting the political orientation of news articles

Course page: <https://augustedebroise.github.io/teaching/ml-nlp-challenge>

## The task

Build an end-to-end pipeline that combines Natural Language Processing and a Machine-Learning
classifier to predict the political orientation of news articles from their title and text.
There are five classes: `left`, `lean left`, `center`, `lean right`, `right`.

- **Teams:** up to 2 students.
- **In class (3 hours):** a runnable prototype that trains a model and predicts on the test set.
  About 15 minutes before the end, each team announces its best model and its validation macro-F1.
- **Afterwards:** refine your work, without instructor input, and submit it on Lola by
  **25 November 2026, 23:59** (one submission per group).

## Data

You receive a folder with the starter notebook and two files:

| File | Rows | Labels | Use |
|---|---|---|---|
| `data/train_dataset.csv` | 5,600 | yes (`Bias`) | everything you need to build and evaluate your models |
| `data/test_dataset.csv` | 2,183 | **no** | predict every row; your score is computed on its hidden labels |

Columns: `id`, `Title`, `Text`, `Bias` (`Bias` only in the training set).

- The articles were **scraped from the web** from several US news outlets, in 2025.
- Each outlet was given a political orientation by a media-bias rating service, and every
  article inherits the rating of the outlet that published it.
- Both files are **raw**: they have **not been cleaned**. Inspecting and cleaning them is part of the challenge.

## Getting started

1. Unzip the folder you received.
2. Install the packages: `pip install pandas scikit-learn jupyter` (add whatever else you use).
3. Open `starter_notebook.ipynb`. It loads the data, contains a **baseline model**
   (TF-IDF + logistic regression on the raw text) and the sections you have to complete:
   exploration, cleaning, preprocessing, train/validation split, your models, final predictions,
   critical thinking, conclusion.

## Rules

- `test_dataset.csv` has no labels: to compare your models, **split `train_dataset.csv` yourselves**.
- Text repairs (cleaning, preprocessing) must be applied identically to the training and the test texts.
  You may remove rows from the training set, **never from the test set**: predict **every** test row.
- The notebook must run top to bottom (*Restart & Run All*) without manual edits, and reproduce your results
  (fix the random seed).
- Using any other copy of this dataset or of its labels is **cheating**. Notebooks may be re-run to check
  that they reproduce the submitted predictions.
- Document any external resource you use (pre-trained models, embeddings, extra libraries) in your notebook.

## Submission

**Deadline: 25 November 2026, 23:59**, on **Lola**, **one submission per group**. Upload two files:

1. **The completed notebook** (`.ipynb`), runnable top to bottom, with the team members' names at the top.
2. **`test_dataset_predicted.csv`**: `test_dataset.csv` with an added `Bias` column holding your
   prediction for every row (the notebook writes it to `data/` for you).

You do not need to include the training and test datasets.

## Evaluation

- **Performance:** macro-F1 on the hidden labels of the test set (accuracy also reported), compared
  with the baseline. Test rows that contain no usable article are not graded.
- **Correctness:** the code runs end to end and reproduces the submitted predictions.
- **Pipeline completeness:** cleaning, preprocessing, training, prediction, saved model.
- **Documentation and reproducibility:** package versions recorded, readable notebook
  (Markdown cells explaining *why*, one logical step per cell).
- **Critical thinking:** short discussion of how the labels were produced, what your model may really be
  learning, the limits of the data and possible misuse.

## Tips

- Start from the baseline, beat it, then try more complex models if time allows.
- Keep a table of what you tried and the validation score of each attempt.
- Use `sklearn.pipeline.Pipeline` so that the same preprocessing is applied at training and prediction time.
- Remove stray prints and debugging code before submitting.
