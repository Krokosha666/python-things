
import docx
import docx2pdf
import os
import sys
from python_docx_replace import docx_replace

def run_document_fill_script(verbose,template_file_path,output_file_path,variables):
   
    if verbose:
        print("DOCX_TEMPLATE_FILLER // Reading file: ", template_file_path)
    template_document = docx.Document(template_file_path)

    docx_replace(template_document,**variables)
    
    if verbose:
        print("DOCX_TEMPLATE_FILLER // Saving file: ", output_file_path)
    template_document.save(output_file_path)



def _replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)


if __name__ == '__main__':

    template_file_path = 'input.docx'
    output_file_path = "output.docx"
    verbose = False
    verbose_extra = False

# this is an example
    variables = {
        "${EMPLOYEE_NAME}": "Example guy",
        "${EMPLOYEE_TITLE}": "Homeless",
        "${EMPLOYEE_ID}": "123456789",
        "${EMPLOYEE_ADDRESS}": "Local landfill",
        "${EMPLOYEE_PHONE}": "8 800 555 3535",
        "${EMPLOYEE_EMAIL}": "example@example.com",
        "${START_DATE}": "01 Jan, 2077",
        "${SALARY}": "1 bobux",
    }
    variables_overriden = False
    
    def safepop(array,index):
        if len(array) > 0:
            return sys.argv.pop(index)
    while len(sys.argv) > 0: # pop errors if array is empty
        s = sys.argv.pop(0)
        if s == "-v":# verbose
            verbose = True
        if s == "-v2":# is extra verbose
            verbose = True
            verbose_extra = True
        elif s == "-i":
            template_file_path = safepop(sys.argv,0) or template_file_path
        elif s == "-o":
            output_file_path = safepop(sys.argv,0) or output_file_path
        elif s == "-var":#variable overrides
            if not variables_overriden:
                variables.clear()
                variables_overriden = True
            is_index = True
            index_storage = ""
            while len(sys.argv) > 0: # pop errors if array is empty
                s = sys.argv.pop(0)
                if s == "-var_end":
                    break
                else:
                    if is_index:
                        index_storage = s
                        is_index = False
                    else:
                        variables[index_storage] = s
                        is_index = True



    if verbose:
        print("Running verbose docx template filler.")
        print("Input template path: ",template_file_path)
        print("Output path: ",output_file_path)
        if variables_overriden:
            print("Variables: {")
            for a in variables:
                print("\t",a,": ",variables[a])
            print("}")
        else:
            print("Variables are not override, switching to demo with the employee.")


    run_document_fill_script(verbose,template_file_path,output_file_path,variables)


