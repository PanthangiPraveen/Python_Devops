import os

# Mapping of day folders to their subtopics
roadmap = {
    "Day_01_Fundamentals": [
        "1.1_Variables_Constants_Comments",
        "1.2_Data_Types",
        "1.3_Input_Output",
        "1.4_Syntax_Indentation"
    ],
    "Day_02_Data_Types_IO_Syntax": [
        "1.2_Data_Types",
        "1.3_Input_Output",
        "1.4_Syntax_Indentation"
    ],
    "Day_03_Operators": [
        "2.1_Arithmetic",
        "2.2_Comparison",
        "2.3_Logical",
        "2.4_Bitwise",
        "2.5_Identity",
        "2.6_Membership"
    ],
    "Day_04_Control_Flow": [
        "3.1_Conditional_Statements",
        "3.2_Loops",
        "3.3_Loop_Control"
    ],
    "Day_05_Data_Structures_1": [
        "4.1_Lists",
        "4.2_Tuples"
    ],
    "Day_06_Data_Structures_2": [
        "4.3_Dictionaries",
        "4.4_Sets",
        "4.5_Strings"
    ],
    "Day_07_Functions": [
        "5.1_Defining_Functions",
        "5.2_Arguments",
        "5.3_Lambda",
        "5.4_Recursion"
    ],
    "Day_08_Modules_and_Packages": [
        "6.1_Importing",
        "6.2_Standard_Libraries",
        "6.3_Installing_with_pip"
    ],
    "Day_09_File_Handling": [
        "7.1_Open_Close_Files",
        "7.2_Read_Write",
        "7.3_Context_Managers"
    ],
    "Day_10_OOP_1": [
        "8.1_Classes_Objects",
        "8.2_Methods_Attributes",
        "8.3_Constructor_init"
    ],
    "Day_11_OOP_2": [
        "8.4_Inheritance_Polymorphism",
        "8.5_Special_Methods"
    ],
    "Day_12_Error_Handling": [
        "9.1_Try_Except",
        "9.2_Raise_Exceptions",
        "9.3_Custom_Exceptions"
    ],
    "Day_13_Comprehensions": [
        "10.1_List_Comprehensions",
        "10.2_Dict_Comprehensions",
        "10.3_Set_Comprehensions"
    ],
    "Day_14_Iterators_and_Generators": [
        "11.1_Iterators",
        "11.2_Generators",
        "11.3_Generator_Expressions"
    ],
    "Day_15_Decorators_and_Closures": [
        "12.1_Functions_as_Objects",
        "12.2_Nested_Functions",
        "12.3_Closures",
        "12.4_Decorators"
    ]
}

# Create subfolders
for day_folder, subtopics in roadmap.items():
    for topic in subtopics:
        path = os.path.join(day_folder, topic)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")
