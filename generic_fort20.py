import sys
import numpy as np
#open 2 river data as well as output file
#sabine data
fin=open(sys.argv[1],"r").readlines()
#Neches data
fin2=open(sys.argv[2],"r").readlines()
#output file
fout=open(sys.argv[3],"w")

#here are river widths
#later we want to move this to input file
#CTXCS Grid
'''
Sabine_widths=[488.046,488.046,250.411,361.643,250.859,266.651,265.028,273.689,268.756,229.424,217.918,193.579,194.853,172.255,166.739,90.818, \
108.008,149.442,86.8381,88.599,74.0266,101.769,84.4466,96.9384,113.196,125.052,99.2895,135.284,105.932,130.603,110.383,129.799,102.216, \
129.561,151.549,110.030,115.991,114.599,92.603,133.289,117.559,135.284,136.470,126.845,152.457,161.231,163.047,160.144,201.821,186.474,181.957, \
183.048, 199.901,194.597,274.230,352.729,362.245,366.253,369.829,392.562,413.403,413.403]
Neches_widths=[254.764,254.764,221.785,187.000,170.076,144.279,124.169,106.935,73.2164,64.4595,99.3828,82.0913,103.425,84.8619,84.5372,72.0187,73.0171, \
55.5249,54.7419,77.3667,82.4546,89.0668,115.38,120.409,145.808,200.052,198.987,186.312,253.120,393.064,335.283,355.462,586.138,683.803,734.230,877.442,784.245,817.524,845.659,845.659]

#S2G Without Sturct Grid
'''

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

Neches_widths=[253.28210637,253.28210637,229.51334896,184.25720509,152.6360373,141.35303714, \
128.00336078,107.62326407,77.97999916,76.17882781,84.93966397, \
86.21038049,97.46593677,86.57784155,87.57754727,70.57901057, \
44.44027719,44.86424298,38.86314323,33.71002058,34.23575529, \
36.31969575,40.7760784,41.57180514,30.66811953,75.17554085, \
84.50749946,112.70455174,112.80057831,173.89309276,171.37699695, \
194.56705241,189.93705693,259.36533854,338.49142446,364.48071666, \
485.60224231,481.57653258,662.63709747,496.88508799,583.94393411, \
498.53380442,540.46399235,599.14592551,557.36002973,721.86191049, \
721.86191049]
'''
S2G With Struct Grid
Sabine_widths=[219.25788707,219.25788707,301.28994942,200.49433194,263.92059266,215.26069913, \
169.72282892,140.16653626,155.46299174,159.25662387,165.77234015, \
133.01755605,119.30248883,116.38857543,108.02999733,100.51199394, \
86.09307968,100.34214857,73.46640606,72.86176107,62.246014,\
64.62657398,62.65480668,70.92344682,105.25135155,103.17090111, \
99.99210232,110.69906382,96.96399835,90.96094292,87.99437554, \
113.19660012,130.98642798,116.72522976,117.88034993,115.06472551,\
114.74903777,114.66747678,100.3912705,61.96913276,60.12222371, \
60.55938016,58.35724401,94.99141095,111.43083282,134.58801331, \
133.07718614,123.38624903,119.82928352,109.33549532,113.10006434, \
125.06396358,122.03731205,128.00691883,132.39832281,139.19832831, \
155.77421431,144.13456378,149.50602053,180.06237064,209.39260131, \
179.56526357,171.78849154,171.02667908,177.2724092,181.16270882, \
229.9220254,249.92517143,277.95263736,252.13705218,225.14031349, \
268.37932141,358.01753991,419.89296152,401.69741754,414.15911993, \
414.15911993]

Neches_widths=[253.28210637,253.28210637,229.51334896,184.25720509,152.6360373,141.35303714, \
128.00336078,107.62326407,77.97999916,76.17882781,84.93966397, \
86.21038049,97.46593677,86.57784155,87.57754727,70.57901057, \
44.44027719,44.86424298,38.86314323,33.71002058,34.23575529, \
36.31969575,40.7760784,41.57180514,30.66811953,75.17554085, \
84.50749946,112.70455174,112.80057831,114.36692289,142.0328169, \
150.93851559,198.07808492,189.93705693,259.36533854,382.67475586, \
334.55204667,373.45789386,481.57653258,452.62284978,595.96211205, \
583.94393411,498.53380442,855.35123059,826.90647276,857.38371225, \
857.38371225]
'''




#1 is sabine 2 is neches for hardcoded case, this defines length of loops later on
numnodes_1=len(Sabine_widths)-1
numnodes_2=len(Neches_widths)-1
print(numnodes_1)
print(numnodes_2)
#also hardcoded just for this specific mesh we will be outputting only 0s to these nodes
numnodes_other=26
#required inputs we would eventually like to move this to an input file
flow_unit=str(input("Please input unit of flow (cfs or cms)\n "))
data_interval=float(input("Please input amount of time in sec. between data points (ie one hour would be 3600):\n"))
startdate=str(input("Please input start time of simulation e.g(8/17/17 00:00) \n"))
length_sim=float(input("Please input length of simulation in days: \n"))
#this  defines loop size
numsets=int(length_sim*86400/data_interval+1)
num_outlines=numsets*(numnodes_1+numnodes_2+numnodes_other)
#needs this for fort.20 format
fout.write(str(int(data_interval)))
fout.write('\n')
#seeing how many lines in input files
#numlines1 = len(fin)
#numlines2=len(fin2)
numlines1=len(open(sys.argv[1],"r").readlines())
numlines2=len(open(sys.argv[2],"r").readlines())
if numlines1 != numlines2:
	print("Warning: Length of files are different \n")
if numlines1 < numsets*numnodes_1 or numlines2 < numsets*numnodes_2:
	print("Warning: Not enough data for entire simulation, repeating first and/or last data points to fill timeseries \n")



#cms_flow1=[[0 for x in range(numnodes_1)] for y in range(numlines1)]
#cms_flow2=[[0 for x in range(numnodes_2)] for y in range(numlines2)]
cms_flow1=np.zeros((numlines1,numnodes_1))
cms_flow2=np.zeros((numlines2,numnodes_2))
iter1=0
#reading and storing
for a in range(len(fin)):
	fin[a]=fin[a].strip().split(",")
	for b in range(len(fin[a])):
		cms_flow=float(fin[a][b])
		cms_flow1[a,b]=cms_flow
for a in range(len(fin2)):
	fin2[a]=fin2[a].strip().split(",")
	for b in range(len(fin2[a])):
		cms_flow=float(fin2[a][b])
		cms_flow2[a,b]=cms_flow
if flow_unit=="cfs":
	cms_flow1=cms_flow1/35.315
	cms_flow2=cms_flow2/35.315 
#now time to write out fort.20 data
#313 is a 13 day delay for Sabine data (HEC-RAS Sabine model starts at 8/17/17 @ 1)
#552 is a 23 day delay for Neches data (HEC-RAS Neches model starts at 8/27/17 @0 )

for x in range(numsets):
    if x<313:
        for a1 in range(numnodes_1):
            fout.write(str(cms_flow1[0,a1]/((Sabine_widths[a1]+Sabine_widths[a1+1])/2)))
            fout.write("\n")
        for a2 in range(numnodes_2):
            fout.write(str(cms_flow2[0,a2]/((Neches_widths[a2]+Neches_widths[a2+1])/2)))
            fout.write("\n")
        for a3 in range(numnodes_other):
            fout.write("0 \n")
    if x>=313 and x<552:
        for a1 in range(numnodes_1):
            fout.write(str(cms_flow1[x-313,a1]/((Sabine_widths[a1]+Sabine_widths[a1+1])/2)))
            fout.write("\n")
        for a2 in range(numnodes_2):
            fout.write(str(cms_flow2[0,a2]/((Neches_widths[a2]+Neches_widths[a2+1])/2)))
            fout.write("\n")
        for a3 in range(numnodes_other):
            fout.write("0 \n")
    if x>=552 and x<808:
        for a1 in range(numnodes_1):
            fout.write(str(cms_flow1[x-313,a1]/((Sabine_widths[a1]+Sabine_widths[a1+1])/2)))
            fout.write("\n")
        for a2 in range(numnodes_2):
            fout.write(str(cms_flow2[x-552,a2]/((Neches_widths[a2]+Neches_widths[a2+1])/2)))
            fout.write("\n")
        for a3 in range(numnodes_other):
            fout.write("0 \n")
    if x>=808:
        for a1 in range(numnodes_1):
            fout.write(str(cms_flow1[x-313,a1]/((Sabine_widths[a1]+Sabine_widths[a1+1])/2)))
            fout.write("\n")
        for a2 in range(numnodes_2):
            fout.write(str(cms_flow2[-1,a2]/((Neches_widths[a2]+Neches_widths[a2+1])/2)))
            fout.write("\n")
        for a3 in range(numnodes_other):
            fout.write("0 \n")
		
	
fout.close()
#check file length
if len(open(sys.argv[3]).readlines())==1+num_outlines:
	print("this should be correct \n")
