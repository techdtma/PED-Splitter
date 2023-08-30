Dict = {
    1010: 'Legislature', 
    1040: 'Legislature', 
    
    1110: 'Sheriff', 
    3110: 'Sheriff', 
    3150: 'Sheriff', 
    3989: 'Sheriff', 
    
    1165: 'District Attorney',
    
    1170: 'Public Defender',

    1185: 'Health Dept',
    4010: 'Health Dept',
    4082: 'Health Dept',

    1230: 'County Executive',

    1340: 'Budget',

    1175: 'Finance',
    1310: 'Finance',
    1355: 'Finance',
    6610: 'Finance',

    1315: 'Comptroller',

    1345: 'Purchasing',

    1410: 'County Clerk',

    1420: 'County Attorney',

    1430: 'Personnel',
    9060: 'Personnel',

    1450: 'Board of Elections',

    1490: 'Highway & Bridges',
    5010: 'Highway & Bridges',
    5020: 'Highway & Bridges',
    5110: 'Highway & Bridges',
    5130: 'Highway & Bridges',

    1620: 'Buildings & Grounds',
    1640: 'Buildings & Grounds',
    5650: 'Buildings & Grounds',
    7110: 'Buildings & Grounds',

    1680: 'Information Services',

    1710: 'Self Insurance',
    1910: 'Self Insurance',

    3020: 'Emergency Communications',
    3410: 'Emergency Communications',
    3411: 'Emergency Communications',

    3140: 'Probation_Alt Sentencing',
    3155: 'Probation_Alt Sentencing',

    3411: 'Arson Task Force',

    3620: 'Safety Office',

    4310: 'Mental Health',
    4320: 'Mental Health',

    5630: 'UCAT',

    6010: 'Department of Social Services',

    6290: 'Office of Employment & Training',

    6410: 'Tourism',

    6510: 'Veterans',

    6772: 'Office for the Aging',

    7310: 'Youth_Human Rights',
    8040: 'Youth_Human Rights',

    8020: 'Planning',

    8090: 'Environmental Control',

    8021: 'Economic Development'
    }

res = {
    "Legislature":[],
    "Sheriff":[],
    "Board of Elections":[],
    "District Attorney":[],
    "Public Defender":[],
    "Health Dept":[],
    "County Executive":[],
    "Budget":[],
    "Finance":[],
    "Comptroller":[],
    "Purchasing":[],
    "County Clerk":[],
    "County Attorney":[],
    "Personnel":[],
    "Highway & Bridges":[],
    "Buildings & Grounds":[],
    "Information Services":[],
    "Self Insurance":[],
    "Emergency Communications":[],
    "Probation_Alt Sentencing":[],
    "Arson Task Force":[],
    "Safety Office":[],
    "Mental Health":[],
    "UCAT":[],
    "Department of Social Services":[],
    "Office of Employment & Training":[],
    "Tourism":[],
    "Veterans":[],
    "Office for the Aging":[],
    "Youth_Human Rights":[],
    "Planning":[],
    "Environmental Control":[],
    "Economic Development":[]
    }


# importing required modules
import PyPDF2
  
# creating a pdf file object
pdfFileObj = open('report.pdf', 'rb')
  
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)


i = 0
deptName = ""

for page in pdfReader.pages:
    #PDF parsing stuffets
    text = page.extract_text()
    text = text.split("\n")
    #Look for work location in page
    for elem in text:
        if "WORK LOC" in elem:
            #print(elem[9:13])
            workloc = elem[9:13]
            deptName = Dict.get(int(workloc))
    
    print(deptName)
    #append page number to work location dictionary
    for key, val in res.items():
        if (key == deptName):
            val.append(i)

    i += 1


print(res)
#from PyPDF2 import PdfFileReader, PdfFileWriter
for key, val in res.items():
    pdfWriter = PyPDF2.PdfWriter()
    if val != []:
#        #reader = PdfFileReader(infile)
#        pdfWriter = PdfFileWriter()
        for elem in val:
            pdfWriter.add_page(pdfReader.pages[elem])

        with open('./generated/' + key + ' PED.pdf', 'wb') as outfile:
            pdfWriter.write(outfile)
        print(val)
  
# closing the pdf file object
pdfFileObj.close()
