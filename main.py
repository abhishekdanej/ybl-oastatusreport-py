from Record import *

opr_node_file_path = "/root/ybl-report-py/opr_node.txt"
hc_config_file_path = "/root/ybl-report-py/hc_config.txt"
output_report_path = "/root/ybl-report-py/OA_status_report.csv"

def readNode():
    f = open(opr_node_file_path, "r")
    recordList = []
    content = f.readlines()
    f.close()
    for line in content:

        if ("------" in line):
            continue
        
        if (line.startswith("Node Ci ID")):
            r = Record()
            r.nodeId = line.split("=")[1].strip()
        
        if (line.startswith("Ci Type")):
            r.ciType = line.split("=")[1].strip()
        
        if (line.startswith("Ci Name")):
            r.ciName = line.split("=")[1].strip()
       
        if (line.startswith("Primary DNS Name")):
            r.primaryDnsName = line.split("=")[1].strip()
        
        if (line.startswith("Operating System")):
            r.operatingSystem = line.split("=")[1].strip()
    
        if (line.startswith("IP Address")):
            r.addIP(line.split("=")[1].strip())

        if (line.startswith("OA Version")):
            r.oaVersion = line.split("=")[1].strip()
            recordList.append(r)

    filteredList = []
    for r in recordList:
        if (r.ciType == "unix" or r.ciType == "nt"):
            filteredList.append(r)

    return filteredList
        
def enrichRecords(recordList):
    nodeSet = set()
    for r in recordList:
        nodeSet.add(r.nodeId)

    print("Set size: ", len(nodeSet))

    f = open(hc_config_file_path, "r")
    lines = f.readlines()
    f.close
    # lineIndex = 0
    matchFound = 0
    for line in lines:

        if(line.startswith("Node Ci ID")):
            matchFound = 0
            toMatchNode = line.split("=")[1].strip()
            if( toMatchNode in nodeSet):
                matchFound = 1

        if(matchFound == 1 and line.startswith("State")):
            for r in recordList:
                if (r.nodeId == toMatchNode):
                    r.oaStatus = line.split("=")[1].strip()

def printReport(recordList):
    f = open(output_report_path, "w")
    for r in recordList:
        f.write(" ".join(r.ipAddList))
        f.write(",")
        f.write(r.ciName)
        f.write(",")
        f.write(r.operatingSystem)
        f.write(",")
        f.write(r.oaVersion)
        f.write(",")
        f.write(r.oaStatus)
        f.write("\n")
    f.close()

def main():
    recordList = []
    recordList = readNode()
    print("Windows and Unix objects: ", len(recordList))

    enrichRecords(recordList)

    printReport(recordList)

    # for x in range(4):
    #     print(recordList[x])
    print("Application closing.")
    
if __name__=="__main__":
    main()