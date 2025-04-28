# disease_diagnosis_expert_system.py

def get_yes_no(prompt):
    return input(prompt + " (yes/no): ").strip().lower() == "yes"

def diagnose(symptoms):
    # Rule 1: Flu
    if symptoms["fever"] and symptoms["cough"] and symptoms["sore_throat"]:
        return "You might have **Flu**."

    # Rule 2: Measles
    if symptoms["fever"] and symptoms["rash"] and symptoms["red_eyes"]:
        return "You might have **Measles**."

    # Rule 3: Migraine
    if symptoms["headache"] and symptoms["nausea"] and symptoms["light_sensitivity"]:
        return "You might have **Migraine**."

    # Rule 4: Asthma
    if symptoms["chest_pain"] and symptoms["shortness_of_breath"]:
        return "You might have **Asthma**."

    # Rule 5: Dengue
    if symptoms["fever"] and symptoms["joint_pain"] and symptoms["rash"]:
        return "You might have **Dengue**."

    return "Sorry, we couldn't determine your illness based on the given symptoms. Please consult a doctor."

def main():
    print("\n=== Disease Diagnosis Expert System ===")
    print("Answer the following questions honestly.")

    symptoms = {
        "fever": get_yes_no("Do you have fever?"),
        "cough": get_yes_no("Do you have cough?"),
        "sore_throat": get_yes_no("Do you have sore throat?"),
        "rash": get_yes_no("Do you have skin rash?"),
        "red_eyes": get_yes_no("Do you have red eyes?"),
        "headache": get_yes_no("Do you have headache?"),
        "nausea": get_yes_no("Do you feel nausea?"),
        "light_sensitivity": get_yes_no("Are you sensitive to light?"),
        "chest_pain": get_yes_no("Do you feel chest pain?"),
        "shortness_of_breath": get_yes_no("Do you experience shortness of breath?"),
        "joint_pain": get_yes_no("Do you feel joint pain?")
    }

    result = diagnose(symptoms)
    print("\nDiagnosis Result:")
    print(result)

if __name__ == "__main__":
    main()
