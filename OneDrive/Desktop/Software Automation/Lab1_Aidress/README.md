# Lab 1: Secure Password Generator

## **Course**: INFT 1207  
**Instructor**: Md Al Maruf  
**Group**: INFT1207-SoftwareAutomation  
**Members**: Aidress Qadeer, [Partner's Name]

---

## **Objective**
This lab focuses on developing a **Random Secure Password Generator** in Python. The program allows users to define password length and composition, ensuring security constraints are met while following best coding practices and implementing unit testing.

---

## **Features**
- **User Input Validation**:
  - Minimum length: **8 characters**
  - Specify number of **letters, digits, and special characters**
  - Ensure inputs are valid and do not exceed total length
- **Password Constraints**:
  - Includes **uppercase, lowercase, digits, and special characters**
  - Characters are **randomly distributed**
- **Error Handling**:
  - Handles incorrect inputs gracefully
- **Modular Code**:
  - Organized into functions for clarity and reusability
- **Unit Tests**:
  - Ensures program reliability by validating inputs and output correctness

---

## **Project Structure**
```
INFT1207-SoftwareAutomation/
├── src/
│   ├── password_generator.py
│   └── __init__.py
├── tests/
│   ├── test_password_generator.py
│   └── __init__.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
```

---

## **Setup Instructions**
### **1. Clone the Repository**
```bash
git clone https://github.com/Idris-1205/INFT1207-SoftwareAutomation.git
cd INFT1207-SoftwareAutomation
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Program**
```bash
python src/password_generator.py
```

### **4. Run Unit Tests**
```bash
python -m unittest discover tests
```

---

## **Sample Input & Output**
### **Example 1**
**Input:**
```
Enter password length: 12
Enter number of letters: 6
Enter number of digits: 3
Enter number of special characters: 3
```
**Output:**
```
Generated Password: Xr@4!pQ3y$7
```

### **Example 2**
**Input:**
```
Enter password length: 10
Enter number of letters: 4
Enter number of digits: 3
Enter number of special characters: 3
```
**Output:**
```
Generated Password: A1@r4m#P9
```

---

## **Version Control & GitHub**
This project follows best Git practices:
- **Frequent commits with meaningful messages**
- **Proper use of .gitignore to exclude unnecessary files**
- **Regular pushes to GitHub**

To push changes to GitHub:
```bash
git add .
git commit -m "Updated project files"
git push origin master
```

---

## **Video Presentation**
**Video Submission**: 

---

## **Contributors**
- **Aidress Qadeer** - [GitHub Profile](https://github.com/Idris-1205)

---

## **License**
This project is licensed under the MIT License.
