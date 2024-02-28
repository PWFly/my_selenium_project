# Hugh's automation test tools 
This is automation test tools for Hugh's project.

### Install selenium
`pip install selenium`

### Create new project directory
`mkdir your_project_name`

### Initialize Git repository
`git init`

### Virtual environment
`pip3 install virtualenv`
`virtualenv venv`
`source venv/bin/activate`
`deactivate`

### Configuration Environment
`pip install -r requirements.txt`

### Run
`python -m the.path.to.the.script`
`docker run -it --rm -p 8080:8080 mitmproxy/mitmproxy`

`docker run --rm \            
-v /Users/huli/Desktop/projects/my_selenium_project/helpers:/home/mitmproxy/helpers \
-v /Users/huli/Desktop/projects/my_selenium_project/sources:/home/mitmproxy/sources \
-p 8080:8080 \
mitmproxy/mitmproxy mitmdump -s /home/mitmproxy/helpers/mitmproxy_request_handler.py`

### Update the requirement.txt file
`pip freeze > requirements.txt`