# DnsPython Example Tests

Just some simple tests of using DNSPython (https://www.dnspython.org/) to validate that infrastructure is configured to a given standard.

The list of domains to verify are sourced from a seperate file with the expected result being hard coded in the test itself.  You'll need to modify this to your requirements.

## How to Run

**Create a virtual environment**

This is optional but can help you keep all your projects seperate. Change into the repo directory and run:

`python -m venv venv`

On Windows activate the environment:

`venv\scripts\activate`

**Install the dependencies**

A couple of additional modules are needed to run the tests, these can be installed using PIP.

From the repo directory run:

`pip install -r requirements.txt`

**Setup an environments file**

Create a ".env" file inside the src directory, this should contain a single line specifying the path to a file containing the list of domains to test:

`DOMAIN_LIST_FILE=<full-path-to-file>`

**Create the file with the list of dmains**

Each domain should be listed on a line by itself:

````
  google.com
  microsoft.com
  redhat.com
````

**Run the tests**

From the src directory run the below command:

`python -m unittest discover -s tests`

