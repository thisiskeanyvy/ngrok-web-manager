import os, shutil

def set_clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def set_drop_cache():
    if os.path.exists("__pycache__"):
        try:
            shutil.rmtree("__pycache__")
            print("Cache successfully emptied.")
        except:
            print("Unable to delete the cache.")
    else:
        print("No cache.")
