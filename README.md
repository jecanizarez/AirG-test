
# AirG Test


Question 1 -> script_1.py
Question 2 -> script_2.py
Question 3 -> script_3.py
## Question 2 answers
**If you had to generate a large number of rows (millions or more), is there 
anything you would do differently to handle this? 
Modify your script to handle this requirement.**

I will handle it by writing rows in batches. It will help with time efficiency. Setting a custom buffering will also helps but it depends on the machine specs

**If this script had to run in a production environment, what tests would you 
include to ensure it's running correctly? Add the tests.**
I would test that the file in generated with the specific filename and the numbers of rows

**If you were having this code reviewed, what else would you do with your code 
to ensure the code is clean and well-formatted?**
I would use code linters like Black, MyPy, Isort and Flake. I would use implement a CI Pipeline in order to mantain code quality. 
## Tech Stack

**Python:** 3.10

**Virtual Environment**: Poetry 

## Dependencies
Poetry installation: https://python-poetry.org/docs/

Install dependencies
```bash
  poetry install
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/jecanizarez/AirG-test.git
```

Go to the project directory

```bash
  cd AirG-test
```

Run script

```bash
  python script_x.py
```


## Tests
```bash
  poetry run pytest
```