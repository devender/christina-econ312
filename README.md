# christina-econ312

## Step 1

`mkdir test-py-prj`

## Step 2

`cd test-py-prj`

## Step 3 

Create a environment specific to this project
`python -m venv venv`

## Step 4

Enter that env
`source venv/bin/activate`

# WHY ?

so that when you do a `pip install` it will keep those files just in this env.

then you can install
`pip install loguru`

## what libs have you installed
`python -m pip freeze > requirements.txt`