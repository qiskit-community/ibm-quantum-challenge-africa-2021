# Frequently Asked Questions
## General
#### How do I submit an answer?

Within each exercise notebook, on the [challenge portal](http://ibm.co/ibmQuantumAfrica21), you will find guidelines to submit an answer. For example in the lab 1 notebook, for exercise 1a:

```python
# Submit your answer using following code
from qc_grader import grade_ex1a
grade_ex1a(qiskit_module_names)
```

#### Can I run the exercise notebooks on a local computer?

Yes it is possible. But we strongly recommend you solve the exercises on the [challenge portal](http://ibm.co/ibmQuantumAfrica21). If you really want to run the exercises locally, you can download the notebooks from the [challenge repository](https://github.com/qiskit-community/ibm-quantum-challenge-africa-2021) and run using Jupyter notebook.

#### Can we check answers on a local computer?

Yes it is possible. But similar to the above question, we strongly recommend you solve the exercises and check answers on the [challenge portal](http://ibm.co/ibmQuantumAfrica21). If you really want to check answers on a local computer, you need to install the [grading client](https://github.com/qiskit-community/Quantum-Challenge-Grader) in addition to downloading the notebooks.

#### Do we need to download the notebooks from github?

No, you can run all exercises on the [challenge portal](http://ibm.co/ibmQuantumAfrica21) itself.

#### Do I need to take the exercises in order?

We encourage you complete the exercises in the given order as this is the intended structure for the challenge. However, you may complete labs 2 and 3 in any order as they are independent. The first lab introduces you to quantum computing at an applications level, and thus it is suggested that you complete lab 1 first.

#### I encountered “Server error”. What should I do?

We have a lot of participants at the moment. Please be patient, wait and try again.

#### I encountered this error `401 : Unauthorized You are not Authenticated to do this (1)` What should I do?

Please try the following on a notebook on Quantum Lab?
```python
import os
os.environ['QXToken'] = 'your token'
print(os.getenv('QXToken'))
```
You can find your token here: https://quantum-computing.ibm.com/account. Make sure the output matches the token you copied from the account page.

Run the code below to check if authentication is working. If you see a long string in the output, it means 401 error has been resolved.

```python
from qc_grader.api import get_access_token
get_access_token()
```
