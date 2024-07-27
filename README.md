## How to Run the application in Docker:
1. Go to the path `Flask_website`
2. Type command `docker build --tag resume-flask-docker .`
3. Type command `docker run -d -p 5001:5000 resume-flask-docker`
4. Access from the host's browser: http://localhost:5001

## Tutorial Reference:
- https://www.youtube.com/watch?v=w6Ui_DVxluc&list=PL7yh-TELLS1EyAye_UMnlsTGKxg8uatkM&index=3 <br>
- https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX <br>

The project is not fully following the above tutorials, consider just using Flask for a simple website consisting of a few web pages. If we want to create a website with complete functionality, use Django instead. <br>
The project mainly considers the following features of Flask:<br>
- Use Template for html file<br>
- Use static files and CSS
- Create routes<br>
- Use Docker to containanize the project<br>


**Note: the webpage design template is credited to:**<br>
Template Name: MyResume<br>
Template URL: https://bootstrapmade.com/free-html-bootstrap-template-my-resume/<br>
Author: BootstrapMade.com<br>
License: https://bootstrapmade.com/license/<br>


## Next Step
- Deploy the application to Amazon Cloud
