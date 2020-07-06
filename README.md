# Mail Merge

########## This is a simple code to send personalised emails to people. There are some add-ons available on Gmail but most of them are paid. I have created my own mail merge for ease of use. Putting it on gitHub so that others can use this too. 

Please make sure: 
1. Email ID and Password for the email through which you want to send the emails are in a file called `credentials` separated by a new line character. 

For e.g.: 

sample@example.com
sample_password

2. The file `rcpt` contains the records of the recipients. The format is: Name{tab space}Recipient ID.

For e.g.,

Sample_Name1\tsample_rcpt1@example.com
Sample_Name2\tsample_rcpt2@example.com

(Tip: If your records are on excel or Google sheets and there are two separate columns for Name and Recipient Email ID, you can directly copy paste the records onto `rcpt`, they will get pasted with the tab space.)
