--How to Run the Leukemia Detection Project – Step-by-Step Guide.--

-Step 1: Install Python
 Install Python 3.8+ from https://www.python.org/downloads/

-Step 2: Project Folder Structure
 Ensure these files are in one folder:

 project/
 ├── app.py           ← Streamlit App
 ├── xxxxx.h5         ← Trained CNN Model
 ├── eda.ipynb        ← Exploratory Data Analysis (optional)
-Step 3: Install Required Python Packages
 Open Terminal / Command Prompt and run:

-pip install streamlit tensorflow pillow numpy matplotlib

-Step 4: Run the Detection App
 In the same folder where app.py is located, run:

 streamlit run app.py

-Step 5: Upload Image and Get Report
 A browser window will open.

 Upload a .jpg blood smear image.

 The system will display prediction & generate a diagnostic report.

 You can Print or Download the report as .txt.



((OR ANOTHER PROCESS))



**Run Leukemia Detection System via CMD (No Python Needed)**

-Step 1: Prepare Your Project Folder
 Create a folder like this:

 leukemia_project/
 ├── app.py           ← Streamlit App
 ├── xxxxx.h5         ← Trained CNN Model
 ├── eda.ipynb        ← (optional – for analysis only)

-Step 2: Install Python & Add to PATH (One-Time Only)
 Download & install Python 3.8+ from:  https://www.python.org/downloads/

 During installation,  check "Add Python to PATH".

-Step 3: Open CMD & Install Required Packages
 In CMD (Windows) or Terminal (Linux/macOS), type:

 pip install streamlit tensorflow pillow numpy matplotlib

-Step 4: Run the Application
 Go to the folder in CMD:

 cd path\to\leukemia_project
 Then launch the app:

 streamlit run app.py

-Step 5: Use the App in Browser
 The browser will open automatically.

 Upload a .jpg blood smear image.

 You’ll get the prediction + downloadable diagnostic report.



