import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import cv2
import pandas as pd


# Set the path to the Tesseract OCR executable (if required)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract the name from a specific region in the screenshot
def extract_name_from_region(image, x, y, width, height):
    # Crop the image to the specified region
    region = image[y:y+height, x:x+width]
    # Convert the region to grayscale
    region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    # Perform OCR to extract text from the region
    extracted_text = pytesseract.image_to_string(region)
    cv2.imwrite("region_image.png", region)
    return extracted_text.strip()  # Remove leading/trailing whitespace


js_code = '''
function addRow(name, power, totalKills, totalKillsT4, totalKillsT5) {
  var table = document.querySelector('table');
  var row = table.insertRow(-1);
  var nameCell = row.insertCell(0);
  var powerCell = row.insertCell(1);
  var totalKillsCell = row.insertCell(2);
  var t4KillsCell = row.insertCell(3);
  var t5KillsCell = row.insertCell(4);

  nameCell.textContent = name;
  powerCell.textContent = power;
  totalKillsCell.textContent = totalKills;
  t4KillsCell.textContent = totalKillsT4;
  t5KillsCell.textContent = totalKillsT5;
}
'''
idsA = []
powerA = []
totalKillsA = []
totalKillsT4A = []
totalKillsT5A = []
deathA = []
namesA = []
df = pd.read_csv('FullData.csv')

for x in range(295):
    print(x)
    if(x == 162 or x == 269):
        x = x + 1

    # Set the path to the screenshot image file
    screenshot_path = 'ScreenShot' + str(x) + '.png'
    screenshot_path1 = 'ScreenShot' + str(x) + '-1.png'
    screenshot_path2 = 'ScreenShot' + str(x) + '-2.png'
    # Load the screenshot image
    screenshot_image = cv2.imread(screenshot_path)
    screenshot_image1 = cv2.imread(screenshot_path1)
    screenshot_image2 = cv2.imread(screenshot_path2)
    # Specify the region coordinates and dimensions for extracting the name
    name_x = 880  # x-coordinate of the name region
    name_y = 284  # y-coordinate of the name region
    name_width = 238  # Width of the name region
    name_height = 45  # Height of the name region

    names_x = 485  # x-coordinate of the name region
    names_y = 168  # y-coordinate of the name region
    names_width = 280  # Width of the name region
    names_height = 60  # Height of the name region




    power_x = 1047  # x-coordinate of the name region
    power_y = 435  # y-coordinate of the name region
    power_width = 199  # Width of the name region
    power_height = 40  # Height of the name region

    totalKills_x = 1283  # x-coordinate of the name region
    totalKills_y = 440  # y-coordinate of the name region
    totalKills_width = 249  # Width of the name region
    totalKills_height = 33  # Height of the name region

    t5_x = 1013  # x-coordinate of the name region
    t5_y = 735  # y-coordinate of the name region
    t5_width = 172  # Width of the name region
    t5_height = 36  # Height of the name region

    t4_x = 1013  # x-coordinate of the name region
    t4_y = 695  # y-coordinate of the name region
    t4_width = 172  # Width of the name region
    t4_height = 36  # Height of the name region

    death_x = 1340  # x-coordinate of the name region
    death_y = 520  # y-coordinate of the name region
    death_width = 200  # Width of the name region
    death_height = 55  # Height of the name region

    # Extract the name from the region
    name = extract_name_from_region(screenshot_image, name_x, name_y, name_width, name_height)
    name = ''.join(filter(str.isdigit, name))
    power = extract_name_from_region(screenshot_image, power_x, power_y, power_width, power_height)
    totalKills = extract_name_from_region(screenshot_image, totalKills_x, totalKills_y, totalKills_width,totalKills_height)

    totalKillsT4 = extract_name_from_region(screenshot_image1, t4_x, t4_y, t4_width, t4_height)
    totalKillsT5 = extract_name_from_region(screenshot_image1, t5_x, t5_y, t5_width, t5_height)

    death = extract_name_from_region(screenshot_image2, death_x, death_y, death_width, death_height)
    names = extract_name_from_region(screenshot_image2, names_x, names_y, names_width, names_height)

    power = power.replace(",", "")
    name = name.replace(",", "")
    name = name.replace(" ", "")
    totalKills = totalKills.replace(",", "")
    death = death.replace(",", "")
    totalKillsT4 = totalKillsT4.replace(",", "")
    totalKillsT5 = totalKillsT5.replace(",", "")
    totalKillsT5 = totalKillsT5.replace(".", "")
    totalKillsT5 = totalKillsT5.replace(" ", "")
    print(name)
    print(power)
    print(totalKills)
    print(death)
    print(names)
    #js_code += f"addRow('{name}', {power}, {totalKills}, {totalKillsT4}, {totalKillsT5});\n"

# Write the JavaScript code to a separate file
#with open('stats.js', 'w') as js_file:
    #js_file.write(js_code)

# Create a list to store the values of x
    namesA.append(names)
    idsA.append(name)
    powerA.append(power)
    totalKillsA.append(totalKills)
    totalKillsT4A.append(totalKillsT4)
    totalKillsT5A.append(totalKillsT5)
    deathA.append(death)
    if(int(name) == 21302679):
        break;


# Create a DataFrame from the values list
#df = pd.DataFrame({'name': namesA, 'Ids': idsA, 'Power': powerA, 'Total Kills': totalKillsA, 'T4 Kills': totalKillsT4A, 'T5 Kills': totalKillsT5A, 'Deaths': deathA})

# Save the DataFrame to an Excel file

    #df.loc[df['Ids'] == int(name), 'Total-Kills-BP5'] = totalKills
    #df.loc[df['Ids'] == int(name), 'T4-Kills-BP5'] = totalKillsT4
    #df.loc[df['Ids'] == int(name), 'T5-Kills-BP5'] = totalKillsT5
    #df.loc[df['Ids'] == int(name), 'Deaths-BP5'] = totalKillsT5
