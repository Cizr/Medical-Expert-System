# This script is an implementation of a medical expert system for disease diagnosis.
# It utilizes a knowledge base consisting of symptoms, descriptions, and treatments for various diseases.

# Initialize empty lists and dictionaries to store disease-related information.
diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

# Function to preprocess and load data from files into memory.
def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    
    # Read the list of diseases from a file.
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    
    # Iterate through each disease and load its symptoms, descriptions, and treatments.
    for disease in diseases_list:
        # Load symptoms from the corresponding file.
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        
        # Load descriptions from the corresponding file.
        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        
        # Load treatments from the corresponding file.
        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()

# Function to identify the disease based on provided symptoms.
def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    return symptom_map[str(symptom_list)]

# Function to get details (description) of a specific disease.
def get_details(disease):
    return d_desc_map[disease]

# Function to get treatments recommended for a specific disease.
def get_treatments(disease):
    return d_treatment_map[disease]

# Function to display information if the identified disease does not match any in the knowledge base.
def if_not_matched(disease):
    print("\n---------------------------------------------")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("\nThe most probable disease that you have is %s\n" % (id_disease))
    print("\nA short description of the disease is given below:\n")
    print(disease_details + "\n")
    print("\nThe common medications and procedures suggested by other real doctors are: \n")
    print(treatments)
    print("---------------------------------------------\n")

# Main function to interact with the user and perform disease diagnosis.
def main():
    print("\nHello, it's Dr. Yar. I am here to help you diagnose your health condition.")
    print("Please answer the following questions with YES or NO.")
    
    # Preprocess and load disease-related data into memory.
    preprocess()
    
    # List of predefined symptoms for the user to respond to.
    symptoms = [
        "headache", "back_pain", "chest_pain", "cough", "fainting", "sore_throat",
        "fatigue", "restlessness", "low_body_temp", "fever", "sunken_eyes", "nausea", "blurred_vision"
    ]
    
    # User input for each symptom.
    lis = []
    for symptom in symptoms:
        answer = input(f"Do you have {symptom.replace('_', ' ')}? (YES/NO): ").lower()
        while answer not in ["yes", "no"]:
            print("Please answer with YES or NO.")
            answer = input(f"Do you have {symptom.replace('_', ' ')}? (YES/NO): ").lower()
        lis.append(answer)

    # Identify the disease based on the provided symptoms.
    identified_disease = identify_disease(*lis)
    
    # Display information if the identified disease is not found in the knowledge base.
    if_not_matched(identified_disease)

# Execute the main function if this script is run directly.
if __name__ == "__main__":
    main()
