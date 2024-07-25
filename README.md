# Kura Labs Cohort 5- Deployment Workload 1
## Intro to CI/CD

Welcome to Deployment Workload 1!  By now you’ve learned about system designs and the CI/CD Pipeline.  Let’s start putting it all together and see it in action.  

Be sure to document each step in the process and explain WHY each step is important to the pipeline.

## Instructions

1. Clone this repository to your GitHub account
2. Create an EC2

	a. Follow document: [AWS EC2 Quickstart Guide](https://github.com/kura-labs-org/AWS-EC2-Quick-Start-Guide/blob/main/AWS%20EC2%20Quick%20Start%20Guide.pdf) if needed
3. Install Jenkins onto the EC2

	a. Connect to the EC2 terminal

 	b. Enter the following commands to install Jenkins:

```
    $sudo apt update && sudo apt install fontconfig openjdk-17-jre software-properties-common && sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt install python3.7 python3.7-venv
    $sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    $echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
    $sudo apt-get update
    $sudo apt-get install jenkins
    $sudo systemctl start jenkins
    $sudo systemctl status jenkins

```

If successful, the last command should show the Jenkins service “active (running)”

4. Log into Jenkins

	a. Enter initial admin password

	b. Install suggested plugins

	c. Create first admin user

5. Create a Multi-Branch pipeline

	a. Click on “New Item” in the menu on the left of the page

	b. Enter a name for your pipeline
  
    c. Select “Multibranch Pipeline”
  
    d. Under “Branch Sources”, click “Add source” and select “GitHub”
  
    e. Click “+ Add” and select “Jenkins”
  
    f. Make sure “Kind” reads “Username and password”

    g. Under “Username”, enter your GitHub username

    h. Under “Password” ,enter your GitHub personal access token

To get the GitHub personal access token, first log into GitHub and click on your profile icon on the top right of the page.

i. On the dropdown menu, click on “Settings”

ii. Click on “<> Developer settings at the bottom of the menu on the left of the page

iii. Click on “Personal access tokens” on the menu on the left of the page and select “Tokens (classic)”

iv. Click “Generate new token” and select the classic option

v. Set an expiration date and then select the following "scopes": repo, admin:repo_hook

This token can only be viewed ONCE! Make sure you enter the token properly (or save it) before leaving the page otherwise a new token must be generated!

6. Connect GitHub repository to Jenkins

	a. Enter the repository HTTPS URL and click "Validate"
  
	b. Make sure that the "Build Configuration" section says "Mode: by Jenkinsfile" and "Script Path: Jenkinsfile"
  
	c. Click "Save" and a build should start automatically

Did the build stages successfully complete? If not, why? How did you resolve the issue?  What did each stage do?

7. After successfully completing the build (provide screenshot of successful build in documentation), download the contents of the repository (the one in your personal GitHub NOT the kuralabs repo!) and upload a zip file of the application it to AWS Elastic Beanstalk.
  
	a. First, follow the instructions in this [LINK](https://scribehow.com/shared/How_to_Create_an_AWS_IAM_Role_for_Elastic_Beanstalk_and_EC2__kTg4B7zRRxCp-aYTJc-WLg) for "How to Create an AWS IAM Role for Elastic Beanstalk and EC2" and create the two IAM roles as specified.

    b. Navigate to the AWS Elastic Beanstalk console page

    c. Navigate to the "Environments" page on the left side menu and click on "Create Environment"

    d. Create a "Web server environment" and enter the an Application name (Environment name should auto populate after that)

    e. Choose "Python 3.7" as the "Managed platform"

    f. "Upload your code" by choosing a "local file" and select the zipped application files you created earlier.

    g. Under "Presets", make sure that "Single instance (free tier eligible) is selected and then click "Next"

    h. Select the "Service role" and "EC2 profile" in the appropriate drop down menus and then click "Next"

    i. Select the default VPC and Subnet "us-east-1a" and then click "Next"

    j. Select "General Purpose (SSD) for "Root volume type" and assign it 10 GB.

    k. Ensure that "Single instance" is selected for the "Environment type" and that ONLY "t3.micro" is selected for instance types (remove all others if present) and then click "Next"

    l. Select 'BASIC' health reporting under the monitoring section. NOT "ENHANCED"!

    m. Continue to the "Review" page and then click "Submit".

    n. When the "environment is successfully launched", click on the link provided in the "Domain" and confirm that the application has deployed!

8. Document! All projects have documentation so that others can read and understand what was done and how it was done. Create a README.md file in your repository that describes:

	a. The "PURPOSE" of the Workload, 
	
	b. The "STEPS" taken (and why each was necessary/important, 
	
	c. A "SYSTEM DESIGN DIAGRAM" that is created in draw.io, 
	
	d. "ISSUES/TROUBLESHOOTING" that may or may have occured, 
	
	e. An "OPTIMIZATION" section for that answers the question: What are the benefits of using managed services for cloud infrastructure?  What are some issues that a retail bank would face choosing this method of deployment and how would you address/resolve them? What are other disadvantages of using elastic beanstalk or similar managed services for deploying applications?
	
	f. A "CONCLUSION" statement as well as any other sections you feel like you want to include.

The README.md is a markdown file that has unique formatting.  Be sure to look up how to write in markdown or use a txt to markdown converter. 
