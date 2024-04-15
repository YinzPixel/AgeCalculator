# Quick Setup Guide for Pyscripts

Welcome to the quick setup guide for Pyscripts. As this tool is continually updated, please refer to the most recent [documentation](https://pyscript.net/) if this guide appears outdated.

## Step 1: Create the Configuration File

Create a file named `pyscript.json` in your project directory. This file will serve as your configuration hub. Structure it as shown below:

```json
{
    "packages": ["python-dateutil"],
    "files": {"/pyscripts/utils.py": "utils.py"}
}
```

# Details
Packages: List all Python packages your project requires.
Files: Include any additional Python files your project uses.

## Step 2: Interact with the DOM

To manipulate the DOM, add the following import at the beginning of your Python script:
 ```python
 from pyscript import document
```

## Handling Events
Modify event handler attributes in HTML for compatibility with Pyscripts:

Replace onClick with py-click for handling click events. 


example: 
```HTML 
<button py-click="submit_button"><img src="icon-arrow.svg" ></button>
 ```  
instead of
 ```HTML
<button OnClick="submitButton()"><img src="icon-arrow.svg" ></button>
```

# Running code in HTML
For running Scripts inside your HTML use **py-script** instead of **script** tags for embedding Python directly within your HTML

```HTML 
<py-script>
    # python code
    print("Hello World")
</py-script>
 ```  
instead of
 ```HTML
<script>
    // javascript code
    console.log("Hello World")
</script>
```


This guide provides the basics to get you started with Pyscripts. For a comprehensive understanding and advanced features, please consult the [official documentation]([http://](https://pyscript.net/)).
