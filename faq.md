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
You will receive the IBM Quantum Challenge Africa 2021 Achievement digital badge for participating in the IBM Quantum Challenge Africa 2021 and successfully completing all three of the Labs by the deadline of 20 Sept, midnight UTC. More details will be shared once the challenge has completed. 

#### Replay of Live Q&A

We hosted a live Q&A prior to the challenge start with a panel consisting of content developers and mentors. [Watch the replay here](http://ibm.co/AfricaChallenge_QA).

#### Still have more questions?

Please let us know if you have any additional questions in the [#challenge-africa-2021](https://qiskit.slack.com/archives/C02C8MKP153) in the [Qiskit Slack](https://ibm.co/joinqiskitslack) workspace. 

## IBM Quantum Lab

### Why am I seeing the error "Failed: 401 Client Error: Unauthorized for URL"?

The challenge platform requires that you are logged in with a full IBMid, and not a social-media account like GitHub. If you are not using an IBMid to login, please register an account **using the same email you registered with.** This should resolve the above error.

### Why am I seeing the error "Login with some authorized provider required."?

This error is shown if you are logging in with a social-media account like GitHub. Please see the solution given for the above question, `Why am I seeing the error "Failed: 401 Client Error: Unauthorized for URL"?`

### Why am I seeing the error "Your request cannot be processed. The System cannot process your request."?

This error may occur if you have two accounts and one is logging in automatically. To resolve this, navigate to [ibm.com](https://ibm.com), disable auto login, logout, close all IBM tabs except one, and re-login to the challenge website.

### Why am I seeing the error "Failed: Gateway Time-out"?

To resolve this issue, try restarting your Python kernel by pressing the refresh icon at the top of the Jupyter notebook/IBM Quantum Lab interface. However, keep in-mind that this will reset all of your Python variables, so you will have to re-run your notebook code cells. If this does not resolve the issue, ping @africa_mentor or @africa_admin in the challenge Slack channel: [#challenge-africa-2021](https://qiskit.slack.com/archives/C02C8MKP153).

### Why am I seeing "Error 524" when I load the IBM Quantum Lab?

The IBM Quantum Lab and IBM Quantum Challenge Africa 2021 teams may need to update the platform at certain points during the challenge. If you encounter this error, you should wait about 5-10 minutes before trying again. By that stage, the server should have successfully updated.

### Why am I seeing "File Save Error for lab-xxxx, Invalid Response: 403"?

Try logging out and back in on the IBM Quantum platform and the challenge website. This should resolve this issue.
