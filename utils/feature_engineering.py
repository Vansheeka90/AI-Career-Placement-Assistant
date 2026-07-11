branch_data = {
    "CSE": {
        "companies": ["Google", "Microsoft", "Amazon"],
        "salary": "8-25 LPA"
    },
    "IT": {
        "companies": ["Infosys", "TCS", "Accenture"],
        "salary": "5-15 LPA"
    },
    "ECE": {
        "companies": ["Qualcomm", "Intel"],
        "salary": "6-15 LPA"
    },
    "EE": {
        "companies": ["Siemens", "ABB"],
        "salary": "5-12 LPA"
    },
    "ME": {
        "companies": ["Bosch", "Mahindra"],
        "salary": "4-10 LPA"
    },
    "Civil": {
        "companies": ["L&T", "DLF"],
        "salary": "4-8 LPA"
    }
}

def get_branch_data(branch):
    return branch_data.get(branch)