# Operations Agent Status Report

This simple python script takes two files as inputs and produces a CSV report. The files are produced as output from Micro Focus Operations Bridge Manager (OBM) CLI as shown from below command. This is tested both for Windows or Linux systems. Script takes important fields from both the files and generates a CSV file, basis the unique 'Node Ci ID' field.

## 1. OPR_NODE file - `C:\HPBSM\opr\bin>opr-node.bat -ln -username admin -password Admin_123 >> c:\opr_node.txt`

Sample output: using the unique Node Ci ID, Ci Type, name, Operating System, OA Version and IP Address.
        ----------------------------------------------------
        Node Ci ID		= 486f0f1e8ce614dfa38083c963db9695
        Ci Type			= nt
        Ci Name			= obm
        Primary DNS Name	= obm.innovationai.in
        Operating System	= Windows Server 2016 10.0
        Processor Family	= x86_64
        IP Address		= fe80::a180:be08:a719:b39f
        IP Address		= 10.129.99.4
        Core ID			= e6d467c5-c17f-4725-9dd5-1a24b781a74d
        OA Version		= 12.12.010
        ----------------------------------------------------
        Node Ci ID		= 41f1411229ae410c90e137cd2f5ab1f3
        Ci Type			= host_node
        Ci Name			= i-02aa446712eb065e9
        Primary DNS Name	= ec2-54-237-26-100.compute-1.amazonaws.com
        Operating System	= 
        Processor Family	= 
        Core ID			= 
        OA Version		= 
        ----------------------------------------------------

## 2. HC_CONFIG file - `C:\HPBSM\opr\bin>opr-node-hc-config.bat -user admin -password Admin_123 -list_nodes -all -det >> c:\hc_config.txt`

Sample output: the Node Ci ID is the unique field with State field showing status of Operations Agent on the particular target VM (obm.innovationai.in)
        ----------------------------------------------------
        Node Ci ID		= 486f0f1e8ce614dfa38083c963db9695
        Ci Type			= nt
        Ci Name			= obm
        Primary DNS Name	= obm.innovationai.in
        HealthCheck		= DEFAULT,AGENT_AND_SERVER
        Intervals (in sec)	= 1800
        Grace Period (in sec)	= 300
        State			= UP
        Last Life Sign		= 2021-03-26T17:50:13.399+0530
        ----------------------------------------------------
        Node Ci ID		= 41f1411229ae410c90e137cd2f5ab1f3
        Ci Type			= host_node
        Ci Name			= i-02aa446712eb065e9
        Primary DNS Name	= ec2-54-237-26-100.compute-1.amazonaws.com
        HealthCheck		= NO
        ----------------------------------------------------