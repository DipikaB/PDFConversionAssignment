# py -m venv vnev

# pip install camelot-py
# pip install camelot-py[cv]
# pip install PyPDF2
# pip install --upgrade PyPDF2==2.12.1
# https://ghostscript.com/releases/gsdnld.html
# Ghostscript AGPL Release download and install
# pip install PyCryptodome
# pip install coverage


import camelot as cm
import pandas as pd
import PyPDF2
import fitz
import traceback


def main(file_path, output_path, file_name_without_extension, password=None):
    """
    file_path: takes complete input path
    output_path: folder to store output file
    file_name_without_extension: takes file name without extension
    password: password to decrypt the pdf file
    returns: returns None but creates CSV file in output folder
    """
    try:
        try:
            tables = cm.read_pdf(file_path,flavor="lattice",line_scale =20,password=password)
        except FileNotFoundError:   
            print("File Not Found")
            exit(1)

        table_number = len(tables)
        print(f"Num of tables: {table_number}")
        
        st=[]
        if table_number > 0:
            for i in range(table_number):
                a =  tables[i].df
                print(tables[i].parsing_report)
                accuracy = tables[i].parsing_report.get("accuracy")
                if accuracy > 50:
                    st.append(a)
        if len(st)>0:
            pd.concat(st).to_csv(f'{output_path}{file_name_without_extension}.csv',index=False, header=False)
            print("PDF converted to CSV successfully")
        else:
            print("CSV File not created. Please check if file is corrupted")
    except Exception as e:
        print("Error occured in main file")
        print(f"{traceback.format_exc()}")


if __name__ == "__main__":
    input_file_name = input("Please enter filename with extension: ")
    password = input("Enter password if pdf is decrypted (else hit enter): ")

    file_path = f"../input/{input_file_name}"
    file_name_without_extension = input_file_name.split(".")[0]
    output_path = f"../output/"
    main(file_path, output_path, file_name_without_extension, password=password)
