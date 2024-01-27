import pandas as pd
from io import StringIO

# Function to process the text into a structured format
def process_text_to_csv(text):
    # Splitting the text by state names
    states_data = re.split(r'\n([A-Z][a-z]+) Facts\n', text)[1:]

    # Initializing lists to hold the data
    states = []
    criminalization = []
    ssp_except = []

    for i in range(0, len(states_data), 2):
        state = states_data[i].strip()
        data = states_data[i + 1]

        # Extracting criminalization and program authorization information
        crim = "Y" if "Criminalization" in data else "N"
        auth = "Y" if "ssp_except" in data else "N"

        # Adding to lists
        states.append(state)
        criminalization.append(crim)
        ssp_except.append(auth)

    # Creating a DataFrame
    df = pd.DataFrame({
        'State': states,
        'Paraphernalia mentioned?': criminalization,
        'With SSP exception?': ssp_except,
        

        
    })

    # Converting the DataFrame to CSV format
    csv_data = df.to_csv(index=False)
    return csv_data

# Processing the text to CSV format
csv_output = process_text_to_csv(plain_text)
print(csv_output[:500]) # Displaying the first 500 characters of the CSV data for review


