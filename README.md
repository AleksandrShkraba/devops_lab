# My application for GitHub!

This application give you information about all pull requests for specific repository. By default it get only title of pull requests. You can choose repository using two required parameters --owner and --repo. 

You can get next information for all pull requests: 
 - login of user who made request (--user param)
 - number of commits for this pull requests (--com param)
 - state of pull requests (--state)
 - number of comments for pull requests (--comment)

All of this parameters are not required, and you can choose any that you want or don't use anyone.

Example of using:

	python ./git_info --owner alenaPy --repo devops_lab --state --comm


# IMPORTANT

You have to enter your credentials in variable credentials like

		credentials = GitHub("USERNAME, PASSWORD")


