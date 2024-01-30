# # Run this py file before to download the requirement files
import subprocess

def install_libraries(requirements_file):
    with open(requirements_file, 'r') as file:
        libraries = [line.strip() for line in file.readlines() if line.strip()]

    for library in libraries:
        subprocess.call(['pip', 'install', library])

if __name__ == "__main__":
    # Installing the requirements
    requirements_file = "requirements.txt"
    install_libraries(requirements_file)



###########################################################################
#      Comment out the below to create the basic project structure        #
###########################################################################
# import os

# # Directories needed
# dirs = [os.path.join("data", "raw"),
#         os.path.join("data","processed"),
#         "etc",
#         "references",
#         "reports",
#         "notebooks",
#         "src"]

# # Creating the directories
# for dir in dirs:
#     if not os.path.exists(dir):
#         os.makedirs(dir, exist_ok=True)
#     else:
#         print(f"Directory '{dir}' already exists.")

# files = ['params.yaml',
#         '.gitignore', # Here we push all the files which we dont want to push into git
#         'requirements.txt',
#         os.path.join('src' , '__init__.py' ),
#         os.path.join('notebooks', 'analysis.ipynb')]

# # Creating some inistial files
# for file_ in files:
#     if not os.path.exists(file_):
#         with open(file_, "w") as f:
#             pass

# # Adding the .gitkeep files to the empty directories
# for dir in dirs:
#     if not os.listdir(dir):
#         with open(os.path.join(dir, '.gitkeep'), 'w') as f:
#             pass