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

#### Do I need an IBMid associated with my IBM Quantum Account?

Yes, you'll need an IBMid associated with your IBM Quantum account in order to complete some of the Labs. If you don't already have one, please [register a new IBMid](https://auth.quantum-computing.ibm.com/auth/idaas) using the SAME email address associated with your IBM Quantum account. If you have any questions or face any issues, please let us know in the [#challenge-africa-2021](https://qiskit.slack.com/archives/C02C8MKP153) Slack channel.

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

#### Will I receive a badge and what are the qualifications?
You will receive the IBM Quantum Challenge Africa 2021 Achievement digital badge for participating in the IBM Quantum Challenge Africa 2021 and successfully completing all three of the Labs by the deadline of 20 Sept, 23:00 UTC. More details will be shared once the challenge has completed. 

#### Replay of Live Q&A

We hosted a live Q&A prior to the challenge start with a panel consisting of content developers and mentors. [Watch the replay here](http://ibm.co/AfricaChallenge_QA).

#### Still have more questions?

Please let us know if you have any additional questions in the [#challenge-africa-2021](https://qiskit.slack.com/archives/C02C8MKP153) in the [Qiskit Slack](https://ibm.co/joinqiskitslack) workspace. 
