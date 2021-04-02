class Record:
    
    def __init__(self):
        self.nodeId = ""
        self.ciType = ""
        self.ciName = ""
        self.primaryDnsName = ""
        self.ipAddList = []
        self.operatingSystem = ""
        self.oaVersion = ""
        self.oaStatus = ""

    def __str__(self):
        return ("ID:% s CIType:% s CIName:% s PrimaryDNS:% s OS:% s OAVersion:% s Status:% s IPAddList:% s" \
        % (self.nodeId, self.ciType, self.ciName, self.primaryDnsName, self.operatingSystem, self.oaVersion, self.oaStatus, self.ipAddList))

        
    def addIP(self, ipAddress):
        self.ipAddList.append(ipAddress)


## OPR_NODE
# ----------------------------------------------------
# Node Ci ID		= 46dc74d9fcfdc72392fe9df379f51656
# Ci Type			= router
# Ci Name			= bl-00841-r03
# Primary DNS Name	= bl-00841-r03
# Operating System	= 
# Processor Family	= 
# IP Address		= 172.30.9.157
# IP Address		= 178.30.40.22
# IP Address		= 10.9.24.2
# IP Address		= 10.25.10.131
# IP Address		= 10.241.74.194
# Core ID			= 
# OA Version		= 
# ----------------------------------------------------

## HC_CONFIG
# ----------------------------------------------------
# Node Ci ID		= 4e1476e12bf7080da89a8e6f9258fdc6
# Ci Type			= nt
# Ci Name			= blpvdrflx03
# Primary DNS Name	= blpvdrflx03
# HealthCheck		= DEFAULT,AGENT_AND_SERVER
# Intervals (in sec)	= 1800
# Grace Period (in sec)	= 300
# State			= DOWN
# Last Life Sign		= 2021-03-26T18:00:21.173+0530
# ----------------------------------------------------