# Chicken Disease Classification 
This project serves as a classification project based on the Deep Learning Model. It classifies whether there is Coccidiosis disease or not. It uses the concept of Modular coding.

## Workflows
Generally follow the below steps to create any project with the modular coding concepts.
1. **Update Configuration Files:**
   - Update `config.yaml`
   - Update `secrets.yaml` (Optional)
   - Update `params.yaml`

2. **Update Entity:**
   - Update the entity

3. **Update Configuration Manager:**
   - Update the configuration manager in `src/config`

4. **Update Components:**
   - Update the components

5. **Update Pipeline:**
   - Update the pipeline

6. **Update Main Script:**
   - Update `main.py`

7. **Update DVC Configuration:**
   - Update `dvc.yaml`

## How to Run?

### Steps:

1. **Clone the Repository:**
```bash
https://github.com/varundesai27/Chicken-Disease-Classification.git
```

2. **Create a environment:**

```bash
conda create -n your_env_name python=3.8 -y
conda activate your_env_name
```

3. **Install Requirements:**

```bash
pip install -r requirements.txt
```
4. **Run the project on your terminal:**

```bash
python main.py
```

or
      
- Initialize DVC: 
```bash
dvc init
```
- Reproduce DVC:
```bash
dvc repro
```
- Generate DVC DAG
```bash
dvc dag
```

5. **Run the Application:**

```bash
python app.py
```


***Additional Steps:***
- Open Local Host and Port:
- Open your local host and port in the browser. This project is currently running on the 8080 port.

## To Create Docker Image:

```bash
docker build -t your_image_name .
```
## RESULTS: RESULT BASED ON THE FECAL IMAGE

1. **Disease identified as the Coccidiosis**
<img width="1470" alt="Screenshot 2024-02-28 at 5 38 52 PM" src="https://github.com/varundesai27/Chicken-Disease-Classification/assets/72991104/ec129249-587c-441f-84ae-be0f963d0df7">


2. **Healthy chicken fecal**
<img width="1470" alt="Screenshot 2024-02-28 at 5 39 18 PM" src="https://github.com/varundesai27/Chicken-Disease-Classification/assets/72991104/9c491ff3-0e8c-4e3c-a82d-52c21ac3d591">


