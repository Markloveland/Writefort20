import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import sys
import numpy as np

#on command line please have in following format:
#python executable Sabinedatafile(in csv) Nechesdatafile(in excel) outputname

Sabine_widths=[ 219.25788707,219.25788707,301.28994942,200.49433194,263.92059266,215.26069913, \
169.72282892,140.16653626,155.46299174,159.25662387,165.77234015, \
133.01755605,119.30248883,116.38857543,108.02999733,100.51199394, \
86.09307968,100.34214857,73.46640606,72.86176107,62.246014, \
64.62657398,62.65480668,72.50305245,74.5339724, 64.46769296, \
112.89423286,99.99210232,92.25148538,103.91839421,98.15566031, \
87.99437554,113.19660012,130.98642798,116.72522976,117.88034993, \
115.06472551,114.74903777,114.66747678,100.3912705,61.96913276, \
60.12222371,60.55938016,58.35724401,94.99141095,111.43083282, \
134.58801331,133.07718614,123.38624903,119.82928352,109.33549532, \
113.10006434,125.06396358,122.03731205,128.00691883,132.39832281, \
149.10991363,135.81459784,144.13456378,149.50602053,180.06237064, \
209.39260131,179.56526357,171.78849154,171.02667908,177.2724092, \
181.16270882,229.9220254,249.92517143,277.95263736,324.40349024, \
362.08273119,374.92070802,382.04661786,401.69741754,414.15911993, \
414.15911993]


#this section reads the Neches data from a spreadsheet
df = pd.read_excel(sys.argv[2])
#hard coded distances between flow nodes specific to Sabine Mesh
Node_dist=np.array([53.1773436,48.62884656,49.25680386,60.41414085,53.21983043,61.87610794])
#Now calculate effective "node width" to convert from volume/sec to area/sec
Node_width=np.array([Node_dist[0]/2,0,0,0,0,0,Node_dist[-1]/2])
Node_width[1:6]=(Node_dist[0:5]+Node_dist[1:6])/2
#Also declare node depths
nodedepth=np.array([-.9525,0.4476,9.08685,5.334,-.762,-.5334,-.476])
#want everything to be positive
adj_depth=np.add(nodedepth,abs(min(nodedepth))+0.1*abs(min(nodedepth)))
#create vector with sum =1
node_dist=adj_depth/sum(adj_depth)
#assumes excel file is in format date,node1,node2....
numnodes=7
#for now data frequency is hard coded (needs to be in sec)
tstep=3600
#open output file and start writing
fout=open(sys.argv[3],"w")
fout.write(str(tstep)+"\n")
#Now we want to convert excel columns into fort20 format

#for neches file
#Also considering data is in cfs, switch to 1 if already in cms
#cfactor=1
cfactor=.02832

#this section reads the Sabine data from a csv file and writes the fort20
#Please note this is hardcoded for the weird format specific for a 42 day harvey run
#Harvey run is Aug 4 2017 00 to Sep 15 2017 00
#Neches data goes from Aug 27 2017 00 to Sep 7 17 00
#Sabine data goes from Aug 17 2017 1:00 to Sep 15 00
RNDAY=42
total_steps=int(RNDAY*60*60*24/tstep + 1)
Neches_start=int(23*60*60*24/tstep)
Sabine_start=int(13*60*60*24/tstep + 60*60/tstep)
Neches_end=int(34*60*60*24/tstep)


#read in sabine data to a numpy array
Sabinenodes=76
Sabinerows=total_steps-Sabine_start+1
print(Sabinerows)
Sabineflow=np.zeros((int(Sabinerows),int(Sabinenodes)))
Sabinecsv=open(sys.argv[1],"r").readlines()

#reading and storing
for a in range(int(Sabinerows)):
        Sabinecsv[a]=Sabinecsv[a].strip().split(",")
        for b in range(len(Sabinecsv[a])):
                temp=float(Sabinecsv[a][b])
                Sabineflow[a,b]=temp
#the sabine data is given in cfs, convert to cms
Sabineflow=Sabineflow*cfactor
#acces the data inside the data frame for Neches
Nechesdata=df['Flow (cfs)']
Lastrow=df.iloc[[-1]]
Lastflow=Lastrow['Flow (cfs)']

#Now write row by row, order goes Sabine,Neches, and then 26 empty lines
for t in range(int(total_steps)):
    if t < Sabine_start:
        for a in range(Sabinenodes):
            flowval=Sabineflow[0][a]/((Sabine_widths[a]+Sabine_widths[a+1])/2)
            fout.write(str(flowval)+"\n")
        for b in range(numnodes):
            flowval=Nechesdata[0]*cfactor*node_dist[b]/Node_width[b]
            fout.write(str(flowval)+"\n")
        for c in range(26):
            fout.write("0"+"\n")
    if t >= Sabine_start and t < Neches_start:
        for a in range(Sabinenodes):
            flowval=Sabineflow[t-Sabine_start][a]/((Sabine_widths[a]+Sabine_widths[a+1])/2)
            fout.write(str(flowval)+"\n")
        for b in range(numnodes):
            flowval=Nechesdata[0]*cfactor*node_dist[b]/Node_width[b]
            fout.write(str(flowval)+"\n")
        for c in range(26):
            fout.write("0"+"\n")
    if t>= Neches_start and t < Neches_end:
        for a in range(Sabinenodes):
            flowval=Sabineflow[t-Sabine_start][a]/((Sabine_widths[a]+Sabine_widths[a+1])/2)
            fout.write(str(flowval)+"\n")
        for b in range(numnodes):
            flowval=Nechesdata[t-Neches_start]*cfactor*node_dist[b]/Node_width[b]
            fout.write(str(flowval)+"\n")
        for c in range(26):
            fout.write("0"+"\n")
    if t >= Neches_end:
        for a in range(Sabinenodes):
            flowval=Sabineflow[t-Sabine_start][a]/((Sabine_widths[a]+Sabine_widths[a+1])/2)
            fout.write(str(flowval)+"\n")
        for b in range(numnodes):
            flowval=84921.34*cfactor*node_dist[b]/Node_width[b]
            fout.write(str(flowval)+"\n")
        for c in range(26):
            fout.write("0"+"\n")

fout.close()

