# vonage-exercise
## Running
To run the script a reasonably recent version of Python is needed. 3.8+ should suffice. Required modules are specified in `requirements.txt`

When run directly the scripts will take input from the file `project.yaml` and save the output to `Dockerfile`. When calling the script's main function you can provide optionally arguments to use different files:
```
def main(input_file="project.yaml",
         output_file="Dockerfile",
         template_file="templates/Dockerfile.jinja")
```

## Testing

To test the script `pytest` module is needed. To run tests just run `pytest` from terminal when in script's directory. Some test cases are stored in `/test` directory. To add more they need to be added to `testdata` list in `test_make_template.py`
