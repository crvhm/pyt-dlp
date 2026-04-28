import subprocess
import os

destinationDirectory = ""
url = ""

def run():
    print("Running the runner function")
    result = subprocess.run(["yt-dlp", url, "-P", destinationDirectory], capture_output=True, text=True)
    print(result.stdout)

def checkWritableDirectory(directory):
    try:
        test_file = os.path.join(directory, "test.txt")
        with open(test_file, 'w') as f:
            f.write("This is a test.")
        os.remove(test_file)
        print("Directory is writable.")
        return True
    except Exception as e:
        print(f"Directory is not writable: {e}")
        return False
    
def checkValidURL(url):
    if url.startswith("http://") or url.startswith("https://"):
        return True
    return False