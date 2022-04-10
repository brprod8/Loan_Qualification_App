# *Loan Qualifier App*
![](R.jpg)

*Overall this app determines if you qualify for a loan by iterating through data and performing numerous calculation.This is made easy for the user and companies.Clients can see which banks are right for them once applications is filled out digitally.*
```
New updates allowed the ability to prompt the user to save qualifying loans as a new csv file enhancing user experience..
```
>*As high priority feature request
emerge more updates will continuously arise enhancing the user experience*
---


## Technologies
 This app is built and excuted using `Python version 3.10`
Iterating through the csv file allows this program to be stable.
```Python
credit_score_approval_list = []
    for bank in bank_list:
        if credit_score >= int(bank[4]):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list 
 ```
 Using the `For` condiational statement it allow us to iterate through the csv file known as bank_list nested in the `For` statement is a `If` statement which tells the computer if the credit score is greater or equal to the bank min approval credit score then appened the bank to a list called credit_score_approval_list.
 >During this process the computer is giving more specific instruction when iterating `int(bank[4])`
  *This specifically tells the computer to iterate bank[4]which is all the bank min credit score this information is givin through csv file* 
  ```Python
  int is a function in python because we are getting information through a csv file the number is technically a `string` using int() we coverted it to a integer 
  ```

##
Describe the technologies required to use your project such as programming languages, libraries, frameworks, and operating systems. Be sure to include the specific versions of any critical dependencies that you have used in the stable version of your project.

---

## Installation Guide

In this section, you should include detailed installation notes containing code blocks and screenshots.

---

## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.

---

## Contributors

In this section, list all the people who contribute to this project. You might want recruiters or potential collaborators to reach you, so include your contact email and, optionally, your LinkedIn or Twitter profile.

---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.
