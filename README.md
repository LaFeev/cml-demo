## cml-demo
Simulating a production machine vision model that is classifying handwritten digits.  This demo is leveraging iterative.ai's [CML](https://cml.dev/) and [DVC](https://dvc.org/) projects to implement an automated continuous learning pipeline.  An (abstracted) upstream ETL process would feed new data to a branch of this repo, triggered by any number of events, such as:  
- degrading performance of production model (could be triggered automatically by an external process monitoring the production model metrics)
- time based (refresh the dataset and update the model weekly/monthly/etc)
- scope creep, e.g. client wants coverage of additional case(s)
<br>
Upon a push of new data, the Github Actions workflow is initiated automatically, pulling the new data from cloud storage, training a new model, outputing metrics/plots, and then comparing the new model to the live model.  The comparison report is added automatically to a comment within the generated pull request.  This was simulated by adding new data (the digit "6") to the dataset, where the original model was trained only on digits 0-5.  Review the [commit comment](https://github.com/LaFeev/cml-demo/commit/5ed97757efcb88a116ace4cbc7a41d7b7f3241db) to see the generated report.
  
#### Benefits
- Cloud storage platform agnostic - including distributed file systems
- Cloud compute from AWS, GCP, Azure, Kubernetes all supported
- Version control for datasets
- Full MLOps pipeline capability, not fully demonstrated here
- Customizable reports (only a very basic implementation here)
- No new systems or platforms, integrates smoothly with Git

#### Demo Caveats
- This demo lacks an output of the original model performance on the new data, which probably could be added to this pipeline, but is assumed to have taken place in some upstream process (such as the monitoring process that triggered this pipeline).  This is discussed [here](https://github.com/LaFeev/cml-demo/issues/1).

Original model, original dataset (digits 0-5):
![confusion matrix](https://github.com/LaFeev/cml-demo/blob/main/confusion_matrix.png?raw=true)  
Original model, new dataset (digits 0-6):
![confusion matrix](https://user-images.githubusercontent.com/5534875/275410943-2ffb35d3-44ab-47ee-bccc-e229d88b2ba7.png)  

- This demo utilized Google Drive as a quick and free illustration of cloud storage.  DVC can integrate with any major cloud provider as well as the Hadoop distributed file system.
- This demo leveraged the free compute resources available through Github Actions, and as such implemented a lightweight logistic regression classifier.  With "runners" available to spin up compute resources from any major provider or on-premise GPUs, this need not be a limiter.
