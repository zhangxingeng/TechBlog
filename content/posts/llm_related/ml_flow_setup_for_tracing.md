---
title: "ml_flow_setup_for_tracing"
date: 2024-10-05
---

# Setup MLFlow for Tracing

### env
- pip install `mlflow` and `SQLAlchemy`

### Random Notes
- `itertools.starmap()`: Applies a function to arguments taken from tuples, "unpacking" them.
- `more_itertools.consume()`: Efficiently consumes an iterator, advancing it to its end.

### Example code of mlflow logging system 
- Experiments can have multiple runs.
  ```python
  import mlflow
  import random
  import time
  
  # Simulated content generator based on prompt
  def fake_llm(prompt):
      return f"Generated content for '{prompt}': " + ''.join(random.choices("abcdefg", k=20))
  
  # Evaluation function using DeepEval
  def fake_eval_function(prompts, responses):
      eval_results = prompts == responses # eval is done here
      return eval_results
  
  # Logging the evaluation and results to MLflow
  def log_results_to_mlflow(prompts, responses, eval_results, tags, run_name):
      mlflow.set_tracking_uri("http://localhost:5000")
      mlflow.set_experiment("evaluation_experiment")
      with mlflow.start_run(run_name=run_name, tags=tags):
          for i, (prompt, response) in enumerate(zip(prompts, responses)):
              mlflow.log_param(f"prompt_{i}", prompt)
              mlflow.log_param(f"generated_content_{i}", response)
          for metric, value in eval_results.items():
              mlflow.log_metric(metric, value)
          mlflow.log_metric("total_prompts", len(prompts))
  
  # Main function simulating the process
  def main():
      prompts = [
          "Tell me a story about a dragon.",
          "Other prompts"
      ]
      responses = [fake_llm(prompt) for prompt in prompts]
      eval_results = fake_eval_function(prompts, responses)
      
      # Set run name and tags
      run_name = f'eval_test_{time.strftime("%Y_%m_%d_%H_%M_%S")}'
      tags = {"author": "Shane", "environment": "DEV"}
      
      # Log to MLflow
      log_results_to_mlflow(prompts, responses, eval_results, tags, run_name)
      print("Evaluation and results logged in MLflow!")
  
  if __name__ == "__main__":
      main()
  ```
